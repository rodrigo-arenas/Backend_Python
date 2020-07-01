from store.utils.context_manager.db_object import db_connection


async def db_get_datetime():
    async with db_connection as connection:
        query = "SELECT CURRENT_TIME"
        db_time = dict(await connection.fetchrow(query))
        print(db_time)
        return db_time


async def db_get_user(user):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_user('{user.username}')"
        try:
            db_user = dict(await connection.fetchrow(query))
        except Exception as e:
            db_user = {}
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


async def db_get_author_from_id(author_id):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_get_author_from_id('{author_id}')"
        try:
            db_author = dict(await connection.fetchrow(query))
        except Exception as e:
            db_author = {}
        return db_author


async def db_patch_author(author_id, name):
    async with db_connection as connection:
        query = f"SELECT * FROM public.fn_update_author_name(\
                                '{author_id}', \
                                '{name}')"
        await connection.execute(query)


