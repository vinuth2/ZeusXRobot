

from pyrogram import filters

from ZeusXRobot import pgram #pgram
from ZeusXRobot.utils.errors import capture_err
from ZeusXRobot.modules.carbon import make_carbon
import codecs
import pickle
from asyncio import gather, get_running_loop
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from random import randint
from re import findall
from time import time
from datetime import timedelta, datetime
from ZeusXRobot import aiohttpsession as aiosession
import aiofiles
import aiohttp
import speedtest
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pyrogram.types import Message
from wget import download



@pgram.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "`Reply to a text message to make carbon.`"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "`Reply to a text message to make carbon.`"
        )
    m = await message.reply_text("`Makeing Carbon...`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading...`")
    await pgram.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()
    
    async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

#ZeusXRobot
