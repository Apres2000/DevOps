import os
import time
import psycopg2
from flask import Flask  # Добавили импорт Flask

app = Flask(__name__)

# Берем настройки из переменных окружения
dbname = os.getenv("POSTGRES_DB", "my_db")
user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "pass_key")
host = "db" # Имя сервиса БД из docker-compose.yml

def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port="5432"
            )
            print("Успех! Мы подключились к PostgreSQL из контейнера.")
            conn.close()
            break
        except Exception as e:
            print(f"База еще не готова, ждем... ({e})")
            time.sleep(2)

@app.route('/')
def home():
    return "Сервер работает, Docker-мост настроен!" "и теперь, у меня работает автоматический CI/CD деплой через GitHub Actions!"

if __name__ == "__main__":
    # Сначала проверяем базу, потом запускаем Flask
    connect_to_db()
    app.run(host="0.0.0.0", port=5000)

