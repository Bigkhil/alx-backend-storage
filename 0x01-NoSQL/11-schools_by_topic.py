#!/usr/bin/env python3
"""this file will find docs by specific filter"""


def schools_by_topic(mongo_collection, topic):
    '''find docs by filter'''
    mongo_collection.find_many(
        {"topic": topic}
    )
