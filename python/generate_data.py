import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("job_platform.db")
cursor = conn.cursor()

countries = ["Brazil", "Portugal", "Germany", "Italy", "Spain"]
industries = ["Tech", "Finance", "Healthcare", "Education"]

# Inserir usuários
for i in range(1, 101):
    cursor.execute(
        "INSERT INTO users VALUES (?, ?, ?, ?, ?)",
        (
            i,
            random.randint(18, 45),
            random.choice(countries),
            "Bachelor",
            datetime.now() - timedelta(days=random.randint(1, 365))
        )
    )

# Inserir empresas
for i in range(1, 21):
    cursor.execute(
        "INSERT INTO companies VALUES (?, ?, ?)",
        (
            i,
            random.choice(industries),
            random.choice(countries)
        )
    )

# Inserir vagas
for i in range(1, 51):
    cursor.execute(
        "INSERT INTO jobs VALUES (?, ?, ?, ?, ?)",
        (
            i,
            random.randint(1, 20),
            "Full-time",
            random.choice(countries),
            "3000-6000"
        )
    )

# Inserir candidaturas
for i in range(1, 301):
    cursor.execute(
        "INSERT INTO applications VALUES (?, ?, ?, ?, ?)",
        (
            i,
            random.randint(1, 100),
            random.randint(1, 50),
            datetime.now() - timedelta(days=random.randint(1, 90)),
            random.choice(["approved", "rejected", "pending"])
        )
    )

conn.commit()
conn.close()
print("Base de dados populada com sucesso!")
