from utils.context_manager.db_connection import DatabaseConnection
from utils.constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


async def db_get_user(user):
    async with DatabaseConnection(host=DB_HOST, port=5432,
                                  database=DB_NAME, user=DB_USER,
                                  password=DB_PASSWORD) as connection:
        query = f"SELECT * FROM public.fn_get_user('{user.username}')"
        db_user = dict(await connection.fetchrow(query))
        return db_user
