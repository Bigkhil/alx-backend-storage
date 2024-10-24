#!/usr/bin/env python3
from pymongo import MongoClient
"""python script"""


def main():
    '''main function'''
    client = MongoClient()
    logs = client.logs.nginx
    print(f'{logs.count_documents()} logs')
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f'    method {method}: {logs.count_documents(
            {"method": method})
            }'
            )
    print(
        f'{logs.count_documents(
            {"method": "GET", "path": "/status"})} status check'
        )
    return


if __name__ == "__main__":
    main()
