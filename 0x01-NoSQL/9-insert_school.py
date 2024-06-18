#!/usr/bin/env python3
""" Insert a document in Python """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    newobj = {}
    for k, v in kwargs.items():
        newobj[k] = v
    res = mongo_collection.insert_one(newobj)
    return res.inserted_id
