#!/usr/bin/env python3
"""
python script
"""
if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f'{logs.count_documents({})} logs')
    print("Methods:")
    for method in methods:
        print(f'    method {method}: {logs.count_documents(
            {"method": method})
            }'
            )
    print(
        f'{logs.count_documents(
            {"method": "GET", "path": "/status"})} status check'
        )
