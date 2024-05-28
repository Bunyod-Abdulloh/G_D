from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

# ======================= TABLE | USERS =======================
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM Users WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

# ======================= TABLE | TABLES =======================
    async def create_table_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Tables (
        id SERIAL PRIMARY KEY,
        table_name VARCHAR(255) NULL,
        channel_id TEXT NULL,
        comment_one TEXT NULL,
        comment_two TEXT NULL,
        files BOOLEAN DEFAULT FALSE
        );
        """
        await self.execute(sql, execute=True)

    async def add_table(self, table_name, channel_id):
        sql = f"INSERT INTO Tables (table_name, channel_id) VALUES($1, $2) returning id"
        return await self.execute(sql, table_name, channel_id, fetchrow=True)

    async def select_all_tables(self):
        sql = f"SELECT * FROM Tables ORDER BY id"
        return await self.execute(sql, fetch=True)

    async def select_media_by_id(self, id_):
        sql = f"SELECT * FROM Tables WHERE id=$1"
        return await self.execute(sql, id_, fetchrow=True)

    async def db_update_comments(self, comment_one, comment_two, id_):
        sql = f"UPDATE Tables SET comment_one=$1, comment_two=$2 WHERE id='{id_}'"
        return await self.execute(sql, comment_one, comment_two, execute=True)

    async def update_media_name(self, new_name, id_):
        sql = f"UPDATE Tables SET table_name='{new_name}' WHERE id='{id_}'"
        return await self.execute(sql, execute=True)

    async def update_media_status(self, id_):
        sql = f"UPDATE Tables SET files=TRUE WHERE id='{id_}'"
        return await self.execute(sql, execute=True)

    async def delete_table_tables(self, id_):
        await self.execute(f"DELETE FROM Tables WHERE id='{id_}'", execute=True)

    async def drop_table_tables(self):
        await self.execute(f"DROP TABLE Tables", execute=True)

# ======================= TABLE | MEDIA =======================
    async def create_media_table(self, media_table):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {media_table} (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(150) NULL,
        file_name VARCHAR(255) NULL,
        file_type TEXT NULL,
        caption VARCHAR(4000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_media(self, table_name, file_id, file_name, file_type, caption):
        sql = f"INSERT INTO {table_name} (file_id, file_name, file_type, caption) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, file_id, file_name, file_type, caption, fetchrow=True)

    async def select_all_media(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        return await self.execute(sql, fetch=True)

    async def db_get_media_by_id(self, table_name, id_):
        sql = f"SELECT * FROM {table_name} WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def drop_table_media(self, table_name):
        await self.execute(f"DROP TABLE {table_name}", execute=True)
