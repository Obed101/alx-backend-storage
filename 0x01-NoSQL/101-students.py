#!/usr/bin/env python3
""" This module utilises aggregate to get average score in MongoDB """

def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    students = [{
        "$project": {"name": "$name",
        "averageScore": {"$avg": "topics.score"}}
    },
    {
        "$sort": {"averageScore": -1}
    }]
    return mongo_collection.aggregate(students)
