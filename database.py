# database.py (FULL CODE)

import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self):
        self._client = None
        if Config.DATABASE_URL:
            self._client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URL)
            self.db = self._client["StreamLinksDB"]
            self.collection = self.db["links"]
        else:
            self.db = None
            self.collection = None
            print("WARNING: DATABASE_URL not set. Links will not be permanent.")

    async def save_link(self, unique_id, message_id):
        if self.collection is not None:
            await self.collection.insert_one({'_id': unique_id, 'message_id': message_id})

    async def get_link(self, unique_id):
        if self.collection is not None:
            doc = await self.collection.find_one({'_id': unique_id})
            return doc.get('message_id') if doc else None
        return None

db = Database()
