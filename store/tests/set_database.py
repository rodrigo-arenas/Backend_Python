from store.utils.context_manager.db_object import db_connection


async def insert_user(username, password):
    async with db_connection as connection:
        query = f"""INSERT INTO public.users(username, password) values('{username}', '{password}')"""
        await connection.execute(query)


async def clear_db():
    async with db_connection as connection:
        query = """TRUNCATE users, personnel, books, authors;"""
        await connection.execute(query)


async def check_personnel_mail(name, mail):
    async with db_connection as connection:
        query = f"""SELECT * FROM personnel WHERE name = '{name}' and mail = '{mail}'"""
        try:
            db_user = dict(await connection.fetchrow(query))
        except Exception as e:
            db_user = {}

        if bool(db_user):
            return True
        else:
            return False


