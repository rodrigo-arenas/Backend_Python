import psycopg2


class DatabaseConnection:
    """
    Creates postgreSQL connection using psycopg2
    """
    def __init__(self, host, port, database, user, password):
        self.connection = None
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(host=self.host,
                                           port=self.port,
                                           database =self.database,
                                           user=self.user,
                                           password=self.password)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # its executed when conection close
        # if there is an error, close connection without commit
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
