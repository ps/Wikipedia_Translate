import wikipedia as w
import simplejson as sj
import requests as r

def _get_title(query):
	res = w.search(query)
	if len(res)==0:
		return None
	return res[0]

def _get_trans(title):
	query = "http://en.wikipedia.org/w/api.php?action=query&format=json&titles=%s&prop=langlinks&lllimit=500&llprop=langname|url&continue=" % title
	res = r.get(query)
	res = sj.loads(res.content)
	page = res["query"]["pages"]

	trans = []
	for l in page[page.keys()[0]]["langlinks"]:
		translation = l["*"]
		language = l["langname"]
		trans.append([language,translation])
	trans.sort()
	return trans

def fetch_langs(query):
	title = _get_title(query)
	t=None
	if title:
		t = _get_trans(title)
	return t
