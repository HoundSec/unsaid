from pymongo import MongoClient
from datetime import datetime, timezone, timedelta
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class DB:
    def __init__(self):  
        try:
            uri = getenv("DATABASE_URI")
            self.client = MongoClient(uri)
            self.database = self.client["untold"]  
            self.collection = self.database["messages"]  
        except Exception as e:
            raise Exception("Error connecting to database: ", e)
    
    def submit_message(self, name, message):  
        try:
            message_data = {
                "name": name,
                "message": message,
                "timestamp": datetime.now(timezone(timedelta(hours=6)))  
            }
            result = self.collection.insert_one(message_data)
            return f"Message submitted with id {result.inserted_id}"
        except Exception as e:
            raise Exception("Error submitting message: ", e)

    def fetch_messages(self, limit):  
        try:
            messages = self.collection.find().sort("timestamp", -1).limit(limit)
            return list(messages)  
        except Exception as e:
            raise Exception("Error fetching messages: ", e)

    def close(self):  
        self.client.close()

