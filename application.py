#!/usr/bin/env python



from flask import Flask,url_for

from wordCutAnalyse import WordCutAnalyse



app = Flask(__name__)
app.register_blueprint(WordCutAnalyse)
#app.register_blueprint(BayesProb)

if __name__ == "__main__":
	app.run(host="127.0.0.1",port=5000,threaded=True,debug=True)
