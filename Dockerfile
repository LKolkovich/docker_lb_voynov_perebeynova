# Используем легковесный базовый образ
FROM python:3.10-alpine

# Устанавливаем зависимости
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY app /app

# Устанавливаем переменную окружения для Flask
ENV FLASK_APP=app.py

# Убираем кеш после установки
RUN rm -rf /root/.cache

# Создаем непривилегированного пользователя
RUN adduser -D flaskuser
USER flaskuser

# Открываем порт для приложения
EXPOSE 4000

# Команда запуска приложения
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]

