#!/usr/bin/env python3
""" Top students """
import pymongo


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    agg = [
        {
            '$project': {
                'name': 1,
                'averageScore': { '$avg': '$topics.score' }
            }
        },
        { '$sort': { 'averageScore': -1 } }
    ]
    return list(mongo_collection.aggregate(agg))
