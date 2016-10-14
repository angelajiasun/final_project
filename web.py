#imports
import os

from flask import Flask, render_template, request
app = Flask(__name__)
import giphypop

g = giphypop.Giphy()

#functions for pages
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results')
def results():
	search_terms = request.values.get('search_terms')
	if search_terms == "":
		return render_template('results.html')
	else:
		gif_keywords = ' '.join(search_terms.split())
		gif_results = g.search(gif_keywords)
		return render_template('results.html', gif_results=gif_results, gif_keywords=gif_keywords)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/github')
def github():
	return render_template('github.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)