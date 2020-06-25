from utils.context_manager.db_connection import DatabaseConnection
from utils.constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

db_connection = DatabaseConnection(host=DB_HOST, port=DB_PORT,
                                   database=DB_NAME, user=DB_USER,
                                   password=DB_PASSWORD)


async def db_get_user(user):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_user('{user.username}')"
        db_user = dict(await connection.fetchrow(query))
        return db_user


async def db_check_jwt_username(username):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_user('{username}')"
        try:
            db_user = dict(await connection.fetchrow(query))
        except Exception as e:
            db_user = {}

        if bool(db_user):
            return True
        else:
            return False


async def db_insert_personnel(user):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_insert_personnel(\
                                '{user.name}', \
                                '{user.password}', \
                                '{user.mail}', \
                                '{user.role}')"
        await connection.execute(query)


async def db_check_personnel(username, password):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_personnel('{username}','{password}')"
        try:
            db_personnel = dict(await connection.fetchrow(query))
        except Exception as e:
            db_personnel = {}

        if bool(db_personnel):
            return True
        else:
            return False


async def db_get_book_with_isbn(isbn):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_book('{isbn}')"
        try:
            db_book = dict(await connection.fetchrow(query))
        except Exception as e:
            db_book = {}
        return db_book


async def db_get_author(author_name):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_author('{author_name}')"
        try:
            db_author = dict(await connection.fetchrow(query))
        except Exception as e:
            db_author = {}
        return db_author


async def db_get_author_from_id(_id):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_author_from_id('{_id}')"
        try:
            db_author = dict(await connection.fetchrow(query))
        except Exception as e:
            db_author = {}
        return db_author
