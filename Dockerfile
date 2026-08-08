# Используем зеркало Timeweb для загрузки образа Python
FROM dockerhub.timeweb.cloud/library/python:3.9-slim

# Устанавливаем системные пакеты для работы с базой
RUN apt-get update && apt-get install -y libpq-dev gcc

# Рабочая директория в контейнере
WORKDIR /app

# Копируем список библиотек и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем твой скрипт Python
COPY app.py .

# Команда запуска
CMD ["python", "app.py"]

