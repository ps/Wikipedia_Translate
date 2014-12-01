import logging
from config import SUPP_LANGS,SUPP_LANGS_CODES
from datetime import date
from flask import Flask,render_template,request
from logging.handlers import RotatingFileHandler
from wiki_fetch import fetch_langs, get_yandex_tran

app=Flask(__name__)

@app.route('/')
def main_page():
	# fetch passed parameters
	query=request.args.get("query")
	lang=request.args.get("lang")
	results=None
	if query:
		results = fetch_langs(query)
	lang_specific_res = None
	yandex_trans="Unable to translate."

	# find specific wikipedia article for the requested
	# language within the returned results
	if lang and results:
		for l in results:
			if l["lang"]==lang:
				lang_specific_res= l
				break
	# get translation only if langauge was specified
	if lang:
		yandex_trans = get_yandex_tran(query, SUPP_LANGS_CODES[lang])
	year=date.today().year

	return render_template('index.html', results=results, 
		query=query, lang=lang, lsr=lang_specific_res, 
		supp_langs=SUPP_LANGS, yandex=yandex_trans, year=year)

if __name__ == "__main__":
	file_handler = RotatingFileHandler('../wiki_error.log', 
                maxBytes=1024 * 1024 * 100, backupCount=20)
	file_handler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	file_handler.setFormatter(formatter)
	app.logger.addHandler(file_handler)
	app.run()
