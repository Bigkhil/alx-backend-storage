#!/usr/bin/env python3
"""this file will find docs by specific filter"""


def schools_by_topic(mongo_collection, topic):
    '''find docs by filter'''
    return mongo_collection.find({"topics": topic})
