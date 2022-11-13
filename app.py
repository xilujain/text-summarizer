from __future__ import unicode_literals
from flask import Flask,render_template,url_for,request

from spacy_summarization import text_summarizer

import spacy

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen


nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

# Fetch Text From Url
def get_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

@app.route('/')
def input():
	return render_template('input.html')


@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():
	if request.method == 'POST':
		raw_url = request.form['raw_url']
		rawtext = get_text(raw_url)
		final_summary = text_summarizer(rawtext)
	return render_template('output.html',ctext=rawtext,final_summary=final_summary,url=raw_url)

if __name__ == '__main__':
	app.run(debug=True)
