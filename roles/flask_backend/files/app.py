import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def connect_to_db():
    """Функция проверки подключения к PostgreSQL"""
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"), # В будущем контейнеры будут в одной сети
            database=os.getenv("DB_NAME", "flask_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres")
        )
        connection.close()
        return True
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        return False

@app.route('/')
def home():
    db_status = "Успешно" if connect_to_db() else "Нет подключения (временно отключена)"
    return jsonify({
        "status": "success",
        "message": "Привет, Эдуард! Flask-бэкенд внутри Docker работает на Шаге №18!",
        "database_connection": db_status
    })

if __name__ == '__main__':
    # Обязательно слушаем на 0.0.0.0, чтобы порт пробрасывался наружу из контейнера
    app.run(host='0.0.0.0', port=5000)

