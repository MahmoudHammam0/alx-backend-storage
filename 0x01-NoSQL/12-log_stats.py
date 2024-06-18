#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
logs_collection = db.nginx

print("{} logs".format(logs_collection.count_documents({})))

print("Methods:")

get = logs_collection.count_documents({"method": "GET"})
print("\tmethod GET: {}".format(get))

post = logs_collection.count_documents({"method": "POST"})
print("\tmethod POST: {}".format(post))

put = logs_collection.count_documents({"method": "PUT"})
print("\tmethod PUT: {}".format(put))

patch = logs_collection.count_documents({"method": "PATCH"})
print("\tmethod PATCH: {}".format(patch))

delete = logs_collection.count_documents({"method": "DELETE"})
print("\tmethod DELETE: {}".format(delete))

status = logs_collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(status))
