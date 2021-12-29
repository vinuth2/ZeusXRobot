
from pyrogram import filters #carbon by vegeta
from telegram import (
    ParseMode,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from ZeusXRobot import pgram as pbot, BOT_USERNAME, UPDATES_CHANNEL
from ZeusXRobot.utils.errors import capture_err
from ZeusXRobot.utils.make_carbon import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**🙄Reply to a text message to make carbon.**")
    if not message.reply_to_message.text:
        return await message.reply_text("**🙄Reply to a text message to make carbon.**")
    m = await message.reply_text("**⬇Downloading...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**⬆Uploading...**")
    await m.delete()
    await pbot.send_photo(message.chat.id,
                          photo=carbon,
                          caption="**Made by @ZeusXRobot**", reply_markup=InlineKeyboardMarkup(
                              [[ InlineKeyboardButton(text="⚡UPDATES", url=f"t.me/{UPDATES_CHANNEL}")]]
                              
carbon.close()
