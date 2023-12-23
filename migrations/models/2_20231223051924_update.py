from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "avatar" TEXT;
        ALTER TABLE "article" DROP COLUMN "test_field";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "test_field" TEXT NOT NULL;"""
