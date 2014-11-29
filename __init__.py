from flask import Flask,render_template,request
from wiki_fetch import fetch_langs, get_yandex_tran
from datetime import date

app=Flask(__name__)

@app.route('/')
def main_page():
	'''supp_langs = ["Afrikaans", "Albanian", "Arabic", 
	"Armenian", "Azerbaijani", "Basque", "Belarusian", 
	"Bengali", "Bosnian", "Bulgarian", "Catalan", 
	"Cebuano", "Chinese", "Croatian", "Czech", "Danish", 
	"Dutch", "Esperanto", "Estonian", "Filipino", 
	"Finnish", "French", "Galician", "Georgian", 
	"German", "Greek", "Gujarati", "Haitian Creole", 
	"Hausa", "Hebrew", "Hindi", "Hmong", "Hungarian",
	"Icelandic", "Igbo", "Indonesian", "Irish", 
	"Italian", "Japanese", "Javanese", "Kannada", 
	"Khmer", "Korean", "Lao", "Latin", "Latvian", 
	"Lithuanian", "Macedonian", "Malay", "Maltese", 
	"Maori", "Marathi", "Mongolian", "Nepali", 
	"Norwegian", "Persian", "Polish", "Portuguese", 
	"Punjabi", "Romanian", "Russian", "Serbian", 
	"Slovak", "Slovenian", "Somali", "Spanish", 
	"Swahili", "Swedish", "Tamil", "Telugu", "Thai",
	"Turkish", "Ukrainian", "Urdu", "Vietnamese", 
	"Welsh", "Yiddish", "Yoruba", "Zulu"]'''

	supp_langs_code = {"Arabic":"ar","Czech":"cs", "French":"fr", "German":"de",
	"Polish":"pl"}
	supp_langs = ["Arabic","Czech","French","German","Polish"]
	query=request.args.get("query")
	lang=request.args.get("lang")
	results=None
	if query:
		results = fetch_langs(query)
	lang_specific_res = None
	yandex_trans="Unable to translate."
	if lang and results:
		for l in results:
			if l["lang"]==lang:
				lang_specific_res= l
				break
	if lang:
		yandex_trans = get_yandex_tran(query, supp_langs_code[lang])

	year=date.today().year
	return render_template('index.html', results=results, 
		query=query, lang=lang, lsr=lang_specific_res, 
		supp_langs=supp_langs, yandex=yandex_trans, year=year)

if __name__ == "__main__":
	app.debug= True
	app.run()
