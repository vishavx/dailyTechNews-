from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    outerData = soup.find_all("div",class_="widget-listing-content-section",limit=10)

    news=""
    for data in outerData:
        findnews=data.a['title']
        news += '\u2022 ' + findnews +'\n'
    return render_template("index.html",News=news)