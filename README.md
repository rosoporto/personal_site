# Flask Developer Portfolio

Простой сайт-визитка программиста, построенный на Flask. Включает динамическую генерацию `robots.txt` и `sitemap.xml`, поддержку `favicon`, а также контейнеризацию через Docker.

## Особенности
- Главная страница с контактными данными из `content.py`.
- Генерация `robots.txt` и `sitemap.xml` с использованием переменной `SITE_URL` из `.env`.
- Favicon из `/static/favicon.ico`.
- Развёртывание через Gunicorn в Docker-контейнере.
- Поддержка стилей через `static/style.css`.

## Требования
- Python 3.10+
- Docker (для контейнеризации)
- Git

## Установка и запуск локально

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/rosoporto/personal_site.git
   cd personal_site
   ```

2. **Создайте виртуальное окружение:**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. **Установите зависимости:**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте виртуального окружения:**:
Создайте файл `.env` в корне проекта с переменными:
    ```text
    EMAIL
    TELEGRAM
    GITHUB
    SITE_URL
    ```

5. **Запустите приложение:**:
    ```bash
    python app.py
    ```

## Запуск через Docker

1. **Соберите образ:**:
    ```bash
    docker build -t flask-app .
    ```

2. **Запустите контейнер:**
    ```bash
    docker run -p 8080:8080 --env-file .env flask-app
    ```

3. **Проверьте работу приложения:**
Откройте http://localhost:8080


## Лицензия
MIT License

## Автор
Создано yourusername. Свяжитесь через [Telegram](https://t.me/rosoporo)
