from flask import Flask, request
import scraping.main as scraping

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape")
def scrape():
    return scraping.scrape(request.args.get("pages", 1, type=int))

def start():
    app.run()