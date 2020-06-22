import asyncpg


class DatabaseConnection(object):
    """
    Creates postgreSQL connection using asyncpg
    """

    def __init__(self, host, port, database, user, password):
        self.connection = None
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    async def __aenter__(self):
        self.connection = await asyncpg.connect(host=self.host,
                                                port=self.port,
                                                database=self.database,
                                                user=self.user,
                                                password=self.password)
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # its executed when connection close
        await self.connection.close()

