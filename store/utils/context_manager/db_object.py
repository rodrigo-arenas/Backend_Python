import asyncpg
from utils.constants import (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT,
                                   TEST_DB_HOST, TEST_DB_NAME, TEST_DB_USER,
                                   TEST_DB_PASSWORD, TEST_DB_PORT, TEST)

pool = None


async def db_connection():
    if TEST:
        db_pool = await asyncpg.create_pool(host=TEST_DB_HOST, port=TEST_DB_PORT,
                                            database=TEST_DB_NAME, user=TEST_DB_USER,
                                            password=TEST_DB_PASSWORD,
                                            min_size=5,
                                            max_size=40,
                                            max_inactive_connection_lifetime=60)
    else:
        db_pool = await asyncpg.create_pool(host=DB_HOST, port=DB_PORT,
                                            database=DB_NAME, user=DB_USER,
                                            password=DB_PASSWORD,
                                            min_size=5,
                                            max_size=40,
                                            max_inactive_connection_lifetime=60)
    return db_pool
