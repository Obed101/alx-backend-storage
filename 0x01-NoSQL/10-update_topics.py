#!/usr/bin/env python3
""" This module changes all topics of school docs"""


def update_topics(mongo_collection, name, topics):
    """ This functions updates school's topics
    where name == Name
    """

    return mongo_collection.update_many({ "name": name },
                                        { "$set": { "topics", topics } })
