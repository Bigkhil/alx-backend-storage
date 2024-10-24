#!/usr/bin/env python3
"""
this file updates docs
"""
def update_topics(mongo_collection, name, topics):
    '''updating docs'''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return
