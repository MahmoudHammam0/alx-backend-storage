#!/usr/bin/env python3
""" List all documents in Python """
import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """
    res = mongo_collection.find()
    if res:
        return list(res)
    else:
        return []
