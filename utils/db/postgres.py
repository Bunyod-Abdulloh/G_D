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
        CREATE TABLE IF NOT EXISTS medias_user (
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
        sql = "SELECT * FROM medias_user"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM medias_user WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM medias_user"
        return await self.execute(sql, fetchval=True)

    async def delete_users(self):
        await self.execute("DELETE FROM medias_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE medias_user", execute=True)

# ======================= TABLE | TABLES =======================
    async def create_table_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS medias_tables (
        table_number INTEGER PRIMARY KEY NOT NULL,
        channel_id VARCHAR(50) NULL,
        comment TEXT NULL,
        files BOOLEAN DEFAULT FALSE
        );
        """
        await self.execute(sql, execute=True)

    async def select_all_tables(self):
        sql = f"SELECT * FROM medias_tables ORDER BY table_number ASC"
        return await self.execute(sql, fetch=True)

    async def select_media_by_id(self, table_number):
        sql = f"SELECT * FROM medias_tables WHERE table_number='{table_number}'"
        return await self.execute(sql, fetchrow=True)

    async def alter_type(self):
        sql = f"ALTER TABLE medias_tables ALTER COLUMN table_number TYPE INTEGER"
        return await self.execute(sql, execute=True)

    async def delete_table_tables(self, table_number):
        await self.execute(f"DELETE FROM medias_tables WHERE table_number='{table_number}'", execute=True)

    async def drop_table_tables(self):
        await self.execute(f"DROP TABLE medias_tables", execute=True)

# ======================= TABLE | MEDIA =======================
    async def select_all_media(self, table_name):
        sql = f"SELECT * FROM {table_name} ORDER BY lesson_number"
        return await self.execute(sql, fetch=True)

    async def db_get_media_by_id(self, table_name, lesson_number):
        sql = f"SELECT * FROM {table_name} WHERE lesson_number='{lesson_number}'"
        return await self.execute(sql, fetchrow=True)

    async def drop_table_media(self, table_name):
        await self.execute(f"DROP TABLE {table_name}", execute=True)
