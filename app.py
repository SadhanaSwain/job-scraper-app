from flask import Flask, render_template, request
from scraper import scrape_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    job_title = request.form['job_title']
    location = request.form['location']
    jobs = scrape_jobs(job_title, location)
    return render_template('index.html', jobs=jobs, job_title=job_title, location=location)

# ✅ Correct binding for Render (host + port)
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)