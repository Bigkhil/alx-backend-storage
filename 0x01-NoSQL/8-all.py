#!/usr/bin/env python3
"""
this file lists all the documents in a certain collection
"""
def list_all(mongo_collection):
    '''list all the documents in a certain collection'''
    return mongo_collection.find()
