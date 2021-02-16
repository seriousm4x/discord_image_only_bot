import imghdr
from io import StringIO
from os import getenv
from urllib.parse import urlparse
from urllib.request import urlopen

import discord

TOKEN = getenv("TOKEN")
MAX_IMAGE_SIZE_MB = getenv("MAX_IMAGE_SIZE_MB")
MAX_IMAGE_SIZE_BYTES = MAX_IMAGE_SIZE_MB * 1000 * 1000
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.attachments) <= 0:
        try:
            url_parser = urlparse(message.content)
            if url_parser.scheme and url_parser.netloc:
                image = urlopen(message.content)
                if not image.info().get_content_type().startswith("image"):
                    print("header content-type is not image. deleting.")
                    await message.delete()
                    return
                if int(image.getheader("Content-Length")) > MAX_IMAGE_SIZE_BYTES:
                    print(
                        f"image larger than {MAX_IMAGE_SIZE_MB}MB. deleting.")
                    await message.delete()
                    return
                if not imghdr.what(None, image.read()):
                    print("not a valid image. deleting.")
                    await message.delete()
                    return
            else:
                print("message is not a link. deleting.")
                await message.delete()
                return
        except Exception as e:
            print("probably not a valid image link. deleting.")
            print(e)
            await message.delete()
            return
    else:
        images = [await i.read() for i in message.attachments]
        for image in images:
            if not imghdr.what(None, image):
                print("not a valid image. deleting.")
                await message.delete()
                return

client.run(TOKEN)
