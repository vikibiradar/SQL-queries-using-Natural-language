import os
import sqlite3
import pandas as pd
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def get_database_schema(database):
    """Fetch the schema (table names and column names) of all tables in the database."""
    try:
        with sqlite3.connect(database) as conn:
            # Fetch all table names
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            # Fetch columns for each table
            schema = {}
            for table in tables:
                table_name = table[0]
                cursor = conn.execute(f"PRAGMA table_info({table_name});")
                columns = [row[1] for row in cursor.fetchall()]
                schema[table_name] = columns
            
            return schema
    except sqlite3.Error as e:
        st.error(f"Error fetching schema: {e}")
        return {}

def get_sql_query(user_query, schema, model_name):
    """Generate SQL query from user input using the database schema."""
    # schema to a string format for the prompt
    schema_info = "\n".join([f"Table: {table}, Columns: {', '.join(columns)}" for table, columns in schema.items()])
    
    groq_sys_prompt = ChatPromptTemplate.from_template(f"""
        You are an expert in converting English questions to SQL queries. 
        The database contains the following tables and columns:
        {schema_info}

        Rules to follow:
        1. Use the appropriate table and column names from the schema provided.
        2. Ensure the SQL query is valid and syntactically correct.
        3. Do not include any explanations or additional text—only the SQL query.
        4. If the question involves filtering, use the WHERE clause.
        5. If the question involves sorting, use the ORDER BY clause.
        6. If the question involves joining tables, use the appropriate JOIN syntax.
        7. If the question involves counting or aggregating, use the appropriate SQL functions (e.g., COUNT, SUM, AVG).

        Now, convert the following English question into a valid SQL query: {{user_query}}.
    """)
    
    llm = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name=model_name
    )

    chain = groq_sys_prompt | llm | StrOutputParser()
    try:
        response = chain.invoke({"user_query": user_query})
        return response
    except Exception as e:
        st.error(f"Error generating SQL query: {e}")
        return None

def return_sql_response(sql_query, database):
    """Execute the SQL query and return results."""
    try:
        with sqlite3.connect(database) as conn:
            data = pd.read_sql_query(sql_query, conn)
        return data
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

def main():
    st.set_page_config(page_title="Text To SQL", layout="wide")
    st.title("Talk to Your Database!")
    st.markdown("App to convert natural language to SQL queries and retrieve data from your database.")

    # Database selection 
    st.sidebar.header("Database Input")
    database_option = st.sidebar.radio("Choose database input method:", ("Upload Database", "Database URL", "Use Sample Database"))

    if database_option == "Upload Database":
        uploaded_file = st.sidebar.file_uploader("Upload your SQLite database", type=["db", "sqlite"])
        if uploaded_file is not None:
            # Save the uploaded file 
            with open("temp.db", "wb") as f:
                f.write(uploaded_file.getbuffer())
            database = "temp.db"
        else:
            st.sidebar.warning("Please upload a SQLite database file.")
            return
    elif database_option == "Database URL":
        database_url = st.sidebar.text_input("Enter your database URL:")
        if database_url:
            database = database_url
        else:
            st.sidebar.warning("Please enter a valid database URL.")
            return
    else:
        # Use the default sample database
        database = "student.db"
        st.sidebar.info("Using the sample student database.")

    # Fetch schema for all tables
    schema = get_database_schema(database)
    if schema:
        st.sidebar.header("Database Schema")
        for table, columns in schema.items():
            st.sidebar.write(f"**Table: {table}**")
            st.sidebar.write(f"Columns: {', '.join(columns)}")
    else:
        st.sidebar.write("No tables found or error fetching schema.")

    # Select Model
    st.sidebar.header("Model Selection")
    model_name = st.sidebar.selectbox(
        "Choose the LLM model:",
        options=["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"],
        index=0  # Default to the first option
    )
    st.sidebar.write(f"Selected model: **{model_name}**")

    # User input section
    user_query = st.text_input("Enter your question:", placeholder="e.g., Show all students in the Data Science course")
    submit = st.button("Generate and Execute Query")

    if submit and user_query:
        st.subheader("Generated SQL Query")
        sql_query = get_sql_query(user_query, schema, model_name)

        if sql_query:
            st.code(sql_query, language="sql")
            
            # Retrieve data
            st.subheader("Query Results")
            retrieved_data = return_sql_response(sql_query, database)

            if not retrieved_data.empty:
                st.dataframe(retrieved_data, use_container_width=True)

                # Downloading the reterived data
                csv = retrieved_data.to_csv(index=False)
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name="query_results.csv",
                    mime="text/csv"
                )
            else:
                st.write("No data retrieved for the query.")

if __name__ == '__main__':
    main()
