from utils.context_manager.db_connection import DatabaseConnection
from utils.constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
import asyncio


async def check_jwt_user(user):
    async with DatabaseConnection(host=DB_HOST, port=5432,
                                  database=DB_NAME, user=DB_USER,
                                  password=DB_PASSWORD) as connection:
        values = await connection.fetch(f"SELECT * FROM public.fn_get_user('{user}')")
        print(values)


loop = asyncio.get_event_loop()
loop.run_until_complete(check_jwt_user('user1'))
