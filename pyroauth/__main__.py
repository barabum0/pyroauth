import asyncio

from pyrogram import Client


async def auth():
    client = Client("client")
    async with client:
        await client.authorize()


def main():
    asyncio.run(auth())


if __name__ == '__main__':
    main()