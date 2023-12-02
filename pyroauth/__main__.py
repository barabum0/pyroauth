import asyncio
import click
from pyrogram import Client


async def auth(api_key: str, api_hash: str):
    client = Client("client")
    async with client:
        await client.authorize()


@click.command()
@click.option("--api_key", "--key", "-ak", type=click.STRING, required=True,
              help="Telegram app API key. Can be obtained from https://my.telegram.org/apps")
@click.option("--api_hash", "--hash", "-ah", type=click.STRING, required=True,
              help="Telegram app API hash. Can be obtained from https://my.telegram.org/apps")
def main(api_key: str, api_hash: str):
    asyncio.run(auth(api_key, api_hash))


if __name__ == '__main__':
    main()