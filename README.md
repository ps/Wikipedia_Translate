Wikipedia Translate
===================
A simple Flask/MongoDB that utilizes [Wikipedia API](http://www.mediawiki.org/wiki/API:Main_page) (along with Wikipedia python library)
to fetch Wikipedia translations for words/phrases. A dictionary translation is given on the
side for comparison by [Yandex.Translate](http://translate.yandex.com/). For instance, have you ever wondered how the movie 
"[Limitless](http://en.wikipedia.org/wiki/Limitless)" is called in Polish?
If you have the only way to find out would be to search Wikipedia for the English version and look
on the side for other language translations. Wikipedia Translate does exactly this!

See it live in action at [wikitranslateitfor.me](http://wikitranslateitfor.me/)

Requirements
============
The app requires:
- [MongoDB](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)
- [Flask](http://flask.pocoo.org/)
- [simplejson](https://pypi.python.org/pypi/simplejson/)
- [wikipedia](https://pypi.python.org/pypi/wikipedia/) 
- [pymongo](https://pypi.python.org/pypi/pymongo/)

Remarks
=======
- Yandex translation does not always translate as desired. For instance when attempting
to translate 'white chicks' to Polish the translation will look as if it wasn't translated. This behavior
is due to Yandex, not due to this app.
- The translation search picks up the first article title returned by the [wikipedia](https://pypi.python.org/pypi/wikipedia/)
search procedure. 

Upcoming
========
- Allow user to see all possile results for a query and let them pick which one they meant (if more than one appeard).
- Organize unit tests.
- Investigate translation from any language to any langauge.
