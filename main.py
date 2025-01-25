import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
import sqlite3
from sqlalchemy import create_engine


def get_sql_from_text(user_query):
    sql_prompt=ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    Suppose,the SQL database has the name STUDENT and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please  """)
    model="llama3-8b-8192"
    llm=ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name=model
    )
    chain=sql_prompt | llm | StrOutputParser()
    sql_query=chain.invoke({user_query})
    return sql_query

def get_data_from_database(sql_query):
    database = "Student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()
    

def main():
    st.set_page_config(page_title="SQL Bot")
    # st.header("Upload your Data Base")
    # uploaded_file=st.file_uploader("Choose a file databse file",type["csv","xlsx"])
    # if uploaded_file is not None:
    #     df = pd.read_csv(uploaded_file) 
    st.header("How can i help you ?")
    user_query=st.text_input("Enter your question")
    submit=st.button("Enter")
    if submit:
        sql_query=get_sql_from_text(user_query)
        retrived_data=get_data_from_database(sql_query)
        st.header("SQL Query is : ")
        st.write(sql_query)
        for row in retrived_data:
            st.write(row)
if __name__=='__main__':
    main()