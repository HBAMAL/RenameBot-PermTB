import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import time
import os
import sqlite3
import asyncio

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import script

import pyrogram

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from plugins.rename_file import rename_doc

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🎬GROUP🎬', url='https://telegram.me/FILIMSMOVIE')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

@Client.on_message(pyrogram.filters.command(["start"]))
async def text(bot, update):
    await update.reply_text(script.START_TEXT.format(update.from_user.first_name),
        reply_markup= START_BUTTONS,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["help"]))
def help_user(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=script.HELP_USER,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="CONTACT MY 🧑🏼‍💻DEV🧑🏼‍💻", url="https://t.me/alluaddict")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["about"]))
def about(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=script.ABOUT_ME,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📢CHANNEL📢", url="https://t.me/telsabots")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["bots"]))
def upgrade(bot, update):
    # logger.info(update)

    bot.send_message(
        chat_id=update.chat.id,
        text=script.CHANNEL_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🤖OTHER BOTS🤖", url="https://t.me/telsabots/13")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
@Client.on_message(filters.command(["Group"]))
def upgrade(bot, update):
    # logger.info(update)

    bot.send_message(
        chat_id=update.chat.id,
        text=script.GROUP_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🎬MOVIE GROUP🎬", url="https://t.me/filimsmovie")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
@Client.on_message(filters.command(["feedback"]))
def upgrade(bot, update):
    # logger.info(update)

    bot.send_message(
        chat_id=update.chat.id,
        text=script.FEEDBACK_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🖋FEEDBACK🖋", url="https://t.me/alluaddict")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
@Client.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.voice | filters.video_note))
async def rename_cb(bot, update):
 
    file = update.document or update.video or update.audio or update.voice or update.video_note
    try:
        filename = file.file_name
    except:
        filename = "Not Available"
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="<b>File Name</b> : <code>{}</code> \n\nSelect YOUR DESIERED OPTION".format(filename),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 RENAME 📝", callback_data="rename_button")],
                                                [InlineKeyboardButton(text="🗑 CANCEL 🗑", callback_data="cancel_e")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    )   


async def cancel_extract(bot, update):
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="✅DONE CANCELLED",
    )
