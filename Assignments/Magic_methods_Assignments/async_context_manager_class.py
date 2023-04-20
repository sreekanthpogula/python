import aiosqlite
import asyncio

class AsyncDBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    
    async def __aenter__(self):
        self.conn = await aiosqlite.connect(self.db_name)
        return self.conn
    
    async def __aexit__(self, exc_type, exc, tb):
        if exc_type:
            await self.conn.rollback()
        else:
            await self.conn.commit()
        await self.conn.close()
    
    async def execute(self, query, args=None):
        cursor = await self.conn.execute(query, args or ())
        rows = await cursor.fetchall()
        await cursor.close()
        return rows



async def main():
    async with AsyncDBManager('test.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
        await db.execute('INSERT INTO users (name) VALUES (?)', ('Satya',))
        rows = await db.execute('SELECT * FROM users')
        print(rows)

asyncio.run(main())
