#!/usr/bin/env python3
""" This module changes all topics of school docs"""


def update_topics(mongo_collection, name, topics):
    """ This functions updates school's topics """
    name_match = { "name": name }
    new_topic = { "$set": { "topics", topics } }

    return mongo_collection.update(name_match, new_topic)
