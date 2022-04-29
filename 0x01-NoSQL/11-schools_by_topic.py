#!/usr/bin/env python3
""" This module lists topics of school docs"""

def schools_by_topic(mongo_collection, topic):
    """ This function returns all school topics that match topic """
    return [school for school in mongo_collection.find({"topics": topic})]
