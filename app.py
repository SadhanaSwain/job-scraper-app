from flask import Flask, render_template, request
from scraper import scrape_jobs  # importing your scraper function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    keyword = ""
    if request.method == "POST":
        keyword = request.form["keyword"]
        jobs = scrape_jobs(keyword)
    return render_template("index.html", jobs=jobs, keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)