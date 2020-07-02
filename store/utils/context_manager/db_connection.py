import asyncpg
import warnings

warnings.warn("This module is not longer used to database connection", DeprecationWarning)


class DatabaseConnection(object):
    """
    Creates postgreSQL connection using asyncpg
    """

    def __init__(self, host, port, database, user, password):
        self.pool = None
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    async def __aenter__(self):
        self.pool = await asyncpg.create_pool(host=self.host,
                                              port=self.port,
                                              database=self.database,
                                              user=self.user,
                                              password=self.password,
                                              min_size=2,
                                              max_size=10,
                                              max_inactive_connection_lifetime=60)

        return self.pool

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # its executed when connection close
        await self.pool.close()
