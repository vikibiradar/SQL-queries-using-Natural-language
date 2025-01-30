# Text-to-SQL App

This is a **Streamlit** app that converts natural language questions into SQL queries and retrieves data from a database. Users can upload their own SQLite database or use a sample database.

## Features
- Convert English questions into SQL queries using an LLM.
- Upload your own database or use a sample database.
- Choose from multiple LLM models for query generation.
- View query results and download them as a CSV file.

---

## How to Use

### 1. Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2.Install dependencies:

pip install -r requirements.txt

3. Create a .env file and add your Groq API key:


4. Run the app:

streamlit run main.py
