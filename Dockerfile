# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем переменную окружения для отключения буферизации вывода Python
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменную окружения PYTHONPATH для корректного импорта модулей
ENV PYTHONPATH=/app

# Запускаем тесты с использованием pytest
RUN pytest

# Определяем команду по умолчанию для запуска приложения
CMD ["uvicorn", "well_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
