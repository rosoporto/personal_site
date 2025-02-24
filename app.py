import os
import base64
import content
from flask import Flask, render_template, url_for, Response
from dotenv import load_dotenv
from datetime import datetime


load_dotenv(override=True)
app = Flask(__name__)


SITE_URL = os.getenv('SITE_URL')


# Добавляем пользовательский фильтр для base64
@app.template_filter('b64encode')
def b64encode_filter(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


@app.route('/')
def home():
    return render_template('index.html', contacts=content.contacts)


@app.route('/robots.txt')
def robots_txt():
    # Рендерим шаблон и возвращаем как text/plain
    content = render_template('robots.txt', site_url=SITE_URL)
    return Response(content, mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap():
    # Рендерим шаблон и возвращаем как application/xml
    current_date = datetime.now().strftime('%Y-%m-%d')
    content = render_template('sitemap.xml', site_url=SITE_URL, lastmod=current_date)
    return Response(content, mimetype='application/xml')


@app.errorhandler(404)
def page_not_found(e):
    # Здесь вы можете вернуть HTML-страницу или JSON-ответ
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
