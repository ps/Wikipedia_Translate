import wikipedia as w
import simplejson as sj
import requests as r
from config import API_KEY

def get_yandex_tran(word, lang):
	query = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&lang=en-%s&text=%s" % (API_KEY,lang,word)
	res = r.get(query)
	res = sj.loads(res.content)
	return res["text"][0]

def _get_title(query):
	res = w.search(query)
	if len(res)==0:
		return None
	# TODO: add support for choosing which result to use
	return res[0]

def _get_trans(title):
	query = "http://en.wikipedia.org/w/api.php?action=query&format=json&titles=%s&prop=langlinks&lllimit=500&llprop=langname|url&continue=" % title
	res = r.get(query)
	res = sj.loads(res.content)
	page = res["query"]["pages"]
	if "-1" in page.keys() or "langlinks" not in page[page.keys()[0]].keys():
		return None
	trans = []
	for l in page[page.keys()[0]]["langlinks"]:
		translation = l["*"]
		language = l["langname"]
		l_code = l["lang"]
		url = l["url"]
		trans.append({"lang":language,"text":translation, "lang_code":l_code, "url":url})
	trans.sort()
	return trans

def fetch_langs(query):
	title = _get_title(query)
	t=None
	if title:
		t = _get_trans(title)
	return t
