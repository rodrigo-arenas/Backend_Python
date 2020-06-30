import aioredis
from store.utils.constants import TEST, REDIS_URL, TEST_REDIS_URL

redis = None


async def redis_connection():
    if TEST:
        redis_db = await aioredis.create_redis_pool(REDIS_URL)
    else:
        redis_db = await aioredis.create_redis_pool(TEST_REDIS_URL)
    return redis_db
