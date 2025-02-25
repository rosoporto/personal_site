# Используем официальный образ Python 3.9
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

ENV PYTHONUNBUFFERED=1

# Указываем порт, который будет использовать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]