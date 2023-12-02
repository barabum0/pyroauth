import asyncio
import click
from pyrogram import Client


async def auth(api_id: int, api_hash: str, output: str):
    client = Client(output, api_id=api_id, api_hash=api_hash, in_memory=False)
    async with client:
        await client.authorize()
        me = await client.get_me()
        click.echo(f"""
        Successfully authorized as {me.first_name} {me.last_name if me.last_name else ""}
        """)


@click.command()
@click.option("--api_id", "--id", "-ai", type=click.INT, required=True,
              help="Telegram app API ID. Can be obtained from https://my.telegram.org/apps")
@click.option("--api_hash", "--hash", "-ah", type=click.STRING, required=True,
              help="Telegram app API hash. Can be obtained from https://my.telegram.org/apps")
@click.option("--output", "-o", type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True),
              help=".session file output path", default="user.session")
def main(api_id: int, api_hash: str, output: str):
    output = output.removesuffix(".session")
    asyncio.run(auth(api_id, api_hash, output))


if __name__ == '__main__':
    main()