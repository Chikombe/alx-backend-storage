#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def print_stats(logs_collection):
    # Total number of logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of logs with method=GET and path=/status
    status_check_count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient()
    
    # Specify the database and collection
    db = client.logs
    logs_collection = db.nginx
    
    # Print stats
    print_stats(logs_collection)
