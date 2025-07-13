from flask import Flask, render_template, request
from scraper import scrape_jobs
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    jobs = scrape_jobs(keyword)
    return render_template('index.html', jobs=jobs, keyword=keyword)

# ✅ Important: Use host='0.0.0.0' and dynamic PORT for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)