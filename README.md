# Text-to-SQL App

This is App which converts natural language questions into SQL queries and retrieves data from a database. Users can upload their own SQLite database or use a sample database.

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
![Screenshot 2025-01-30 094625](https://github.com/user-attachments/assets/ad968ecc-8859-46b4-8302-dbf265054f4d)

#Data after downloading, will be in csv format
![image](https://github.com/user-attachments/assets/6b63d654-b2d9-4ce3-ab02-ba49e88b5eb0)

## Class UML Diagram:
UML diagram is generated using PLANTUML WEB PLATFORM
![Screenshot 2025-01-30 095458](https://github.com/user-attachments/assets/30acb6e0-8da2-419a-93e5-3096c7f92529)

##Sequence UML Diagram:
![Screenshot 2025-01-30 100219](https://github.com/user-attachments/assets/d8e9091c-ff27-4783-9775-b27b9ce7bd14)




