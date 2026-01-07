import sqlite3
import pandas as pd

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect("job_platform.db")

# Criação das tabelas
create_tables = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    age INTEGER,
    country TEXT,
    education_level TEXT,
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    industry TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    job_type TEXT,
    location TEXT,
    salary_range TEXT
);

CREATE TABLE IF NOT EXISTS applications (
    application_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER,
    application_date DATE,
    status TEXT
);
"""
conn.executescript(create_tables)

# Query: Total de candidaturas por vaga
query = """
SELECT 
    job_id, 
    COUNT(*) AS total_applications
FROM applications
GROUP BY job_id
ORDER BY total_applications DESC;
"""

# Executa a query e transforma em DataFrame
df = pd.read_sql_query(query, conn)

# Exibe resumo no terminal
print("Resumo das análises - Total de candidaturas por vaga:")
print(df.head())

# Exporta resultado para CSV
df.to_csv("output_total_applications.csv", index=False)
print("Arquivo 'output_total_applications.csv' gerado com sucesso.")

# Fecha a conexão
conn.close()
