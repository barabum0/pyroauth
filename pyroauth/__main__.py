import asyncio
import click
from pyrogram import Client


async def auth(api_id: str, api_hash: str):
    client = Client("client", api_id=api_id, api_hash=api_hash)
    async with client:
        await client.authorize()


@click.command()
@click.option("--api_key", "--key", "-ak", type=click.STRING, required=True,
              help="Telegram app API key. Can be obtained from https://my.telegram.org/apps")
@click.option("--api_id", "--id", "-ai", type=click.STRING, required=True,
              help="Telegram app API ID. Can be obtained from https://my.telegram.org/apps")
def main(api_id: str, api_hash: str):
    asyncio.run(auth(api_id, api_hash))


if __name__ == '__main__':
    main()