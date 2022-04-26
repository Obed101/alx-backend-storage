#!/usr/bin/env python3
""" This module uses pymongo library (imported in test function) to
list mogodb docs
"""


def list_all(mongo_collection):
    """ lists all docs in the collection """
    return [ doc for doc in
            mongo_collection.find()] if mongo_collection else []
