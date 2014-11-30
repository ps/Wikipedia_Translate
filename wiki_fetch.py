import wikipedia as w
import simplejson as sj
import requests as r
from config import API_KEY
import cache

def get_yandex_tran(word, lang):
	'''
	Fetches Yandex translation from English to specified language.
	'''

	# check if in the cache
	res_cache = cache.fetch_cache_dict_translation(word,lang)
	if res_cache:
		return res_cache

	query = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&lang=en-%s&text=%s" % (API_KEY,lang,word)
	res = r.get(query)
	res = sj.loads(res.content)
	res = res["text"][0]
	# update the cache
	cache.insert_dict_translation(word,lang,res)
	return res

def _get_title(query):
	'''
	Gets the Wikipedia title of an article that can then be utilized to get language pages
	via the direct API url.
	'''

	res = w.search(query)
	if len(res)==0:
		return None
	# TODO: add support for choosing which result to use
	return res[0]

def _get_trans(title):
	'''
	Fetches Wikipedia translations based on the correct title provided.
	'''

	# check if in cache
	res_cache = cache.fetch_cache_wiki_translation(title)
	if res_cache:
		return res_cache

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
	# update cache
	cache.insert_wiki_translation(title,trans)
	return trans

def fetch_langs(query):
	'''
	Main entry point that returns languages based on the provided query.
	'''

	title = _get_title(query)
	t=None
	if title:
		t = _get_trans(title)
	return t
