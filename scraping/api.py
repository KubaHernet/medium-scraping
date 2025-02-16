from flask import Flask, request
import scraping.main as scraping

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape")
def scrape():
    return scraping.default(request.args.get("pages", 1, type=int))