from flask import Flask, render_template, request
from scraper import scrape_jobs

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    jobs = scrape_jobs(keyword)
    return render_template('index.html', jobs=jobs, keyword=keyword)

# ✅ Correct binding for Render (host + port)
import os

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)