import random
import string

from pymongo import MongoClient
from mongoframes.frames import Frame

Frame._client = MongoClient('mongodb://localhost:27017/mydb')
class URLs(Frame):

    _fields = {
        "slug",
        "ios",
        "android",
        "web"
    }


def randomStringDigits(stringLength=8):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def show_data():
	shortlinks = []
	rows = URLs.many()
	if not rows:
		return "not found"
	if len(rows) == 0:
		return shortlinks
	for row in rows:
		new_row = {"slug": row.slug,
                  "ios": {"primary": row.ios["primary"],
                          "fallback": row.ios["fallback"]},
                 "android": {"primary": row.android["primary"],
                              "fallback": row.android["fallback"]},
                  "web": row.web}
		shortlinks.append(new_row)
	return shortlinks   


def insert_data(data):
	if "slug" in data:
		new_row = URLs(data)
		new_row.insert()
		return "inserted directly"
	slug = randomStringDigits()
	data["slug"] = slug
	new_row = URLs(data)
	new_row.insert()
	return slug

def update_data(new_data, slug):
	row = URLs.one({'slug': slug})
	if not row:
		return "not found"
	if "web" in new_data:
		row.web = new_data["web"]
		row.update('web')
	for platform, url in new_data.items():
		for key in url:
			if platform == "android":
				if key == "primary":
					row.android["primary"] = new_data[platform][key]
					row.update("android")
				elif key =="fallback":
					row.android["fallback"] = new_data[platform][key]
					row.update("android")
			elif platform == "ios":
				if key == "primary":
					row.ios["primary"] = new_data[platform][key]
					row.update("ios")
				elif key == "fallback":
					row.ios["fallback"] = new_data[platform][key]
					row.update("ios")
