import pymongo

CON = pymongo.Connection()
db = CON["wiki_translate"]

def fetch_cache_dict_translation(query, lang):
	'''
	Checks if provided query is in the db cache.

	Args:
		query: query that was issued for translation 
		lang: language code for which the translation is being asked for 
	Returns:
		Translated text if one is found or None if not found.
	'''
	trans = db.dict_trans.find_one({"query":query, "lang":lang})
	if trans:
		hits = int(trans["hits"])
		hits += 1
		db.dict_trans.update({"_id":trans["_id"]}, {"$set": {"hits": hits}})
		return trans["text"]
	else:
		return None


def insert_dict_translation(query,lang,text):
	'''
	Inserts into db cache the provided dictionary mapping.

	Args:
		query: query that was issued for translation
		lang: language code for which the translation is being asked for
		text: translated text 
	'''
	db.dict_trans.insert({"query":query, "lang":lang, "text":text, "hits":1})


def insert_wiki_translation(title, langs):
	'''
	Inserts into db cache the provided wiki property.

	Args:
		title: Wikipedia valid article title
		langs: list of dicts in form:
			lang: language
			text: appropriate translation
			lang_code: corresponding langauge code
			url: corresponding wikipedia url page in the language

	'''
	db.wiki_trans.insert({"hits":0, "title":title, "langs": langs})


def fetch_cache_wiki_translation(title):
	trans = db.wiki_trans.find_one({"title":title})
	if trans:
		hits = int(trans["hits"])
		hits += 1
		db.wiki_trans.update({"_id":trans["_id"]}, {"$set": {"hits": hits}})
		return trans["langs"]
	else:
		return None
