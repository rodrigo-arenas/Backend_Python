# Generate key with openssl rand -hex 32
JWT_SECRET_KEY = "46e5c95a2d980476afb2d679b37bb2c8990c25b4ea1075514f67f62f77daf306"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 15

# TODO: Move to environment variables
DB_HOST = 'localhost'
DB_NAME = 'bookstore'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_PORT = 5432

REDIS_URL = 'redis://localhost'
