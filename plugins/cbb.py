import pyrogram

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name
from pyrogram import Client as pyrogram, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from script import script

helpbutton = [[
        InlineKeyboardButton(f'📢CHANNEL📢', url="https://t.me/telsabots"),
        InlineKeyboardButton(f'🧑🏼‍💻DEV🧑🏼‍💻', url="https://t.me/alluaddict")
        ],[
        InlineKeyboardButton(f'🤗ABOUT🤗', callback_data="about")
        InlineKeyboardButton(f'🎬GROUP🎬', url='https://telegram.me/FILIMSMOVIE')
    ]]

aboutbutton = [[
        InlineKeyboardButton(f'📢CHANNEL📢', url="https://t.me/telsabots"),
        InlineKeyboardButton(f'🎬GROUP🎬', url='https://telegram.me/FILIMSMOVIE')
        ],[
        InlineKeyboardButton(f'🆘HELP🆘', callback_data="help"),
        InlineKeyboardButton(f'🔐CLOSE 🔐', callback_data="close")
    ]]


@pyrogram.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)

    elif update.data == "help":
        await update.answer()
        keyboard = InlineKeyboardMarkup(helpbutton)
        await update.message.edit_text(
            text=script.HELP_USER,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif update.data == "about":
        await update.answer()
        keyboard = InlineKeyboardMarkup(aboutbutton)
        await update.message.edit_text(
            text=script.ABOUT_ME,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif update.data == "close":
        await update.message.delete()

        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
