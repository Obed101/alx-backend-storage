#!/usr/bin/env python3
""" This module provides some stats about Nginx logs in MongoDB """


from pymongo import MongoClient


def nginx_logs():
    """ provides stats about Nginx logs stored in MongoDB """
    client = MongoClient()
    colections = client.logs.nginx

    documents_count = colections.count_documents({})
    print("{} logs".format(documents_count))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # printing the documents count one-by-one
    for method in methods:
        count = colections.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status = colections.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    nginx_logs()
