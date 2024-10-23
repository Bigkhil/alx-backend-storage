#!/usr/bin/env python3
"""
insert document
"""
def insert_school(mongo_collection, **kwargs):
    '''insert document'''
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
