#!/usr/bin/env python3
"""this file will find docs by specific filter"""


def schools_by_topic(mongo_collection, topic):
    '''find docs by filter'''
    res = mongo_collection.find(
        {"topic": topic}
    )
    return res
