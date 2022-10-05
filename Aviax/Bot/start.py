
import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from time import time
from datetime import datetime
from Aviax import SUDO_USER, OWNER
from AviaxData.bs import *
from AviaxData.bs import HELP_TEXT, SPAM_TEXT, RAID_TEXT, HANG_TEXT, CARBON_TEXT, TOOLS_TEXT, START_TEXT
from pyrogram.errors import MessageNotModified
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message


# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)






# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

keyboard = InlineKeyboardMarkup(
        [    
            [
               InlineKeyboardButton("Help & Commands", callback_data="help"),
            ],
            [
               InlineKeyboardButton(text="⚖ Owner", user_id=OWNER), 
            ], 
            [
               InlineKeyboardButton(text="👥 Support", url="t.me/AviaxSupport"),
               InlineKeyboardButton(text="UpDate 📢", url="t.me/AviaxOfficial"),
            ],
            [
               InlineKeyboardButton(text="❌ Close", callback_data="cls"),
            ],
        ]
    )

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Tᴏᴏʟꜱ", callback_data="tools"),
                InlineKeyboardButton ("Sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("RᴇᴘʟʏRᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton ("Hᴀɴɢ", callback_data="hang"),
            ],
            [
               InlineKeyboardButton("CᴀʀBᴏɴ", callback_data="carbon"),
            ],
            [
               InlineKeyboardButton("╰✰ Cʜᴀɴɴᴇʟ", url=f"https://t.me/AviaxOfficial"),
               InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
               InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ ✰╮", url=f"https://t.me/AviaxSupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)        
        try:
            await query.edit_message_text(
                HELP_TEXT,               
                reply_markup=reply_markup, 
            )
        except MessageNotModified:
            pass

    elif query.data=="carbon":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/AviaxOfficial"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                CARBON_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="tools":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/AAviaxOfficial"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                TOOLS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="hang":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/AviaxOfficial"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HANG_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/AviaxOfficial"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/AviaxOfficial"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton("⚖ Owner", user_id=OWNER),
            ],
            [
                InlineKeyboardButton("👥 Support", url=f"https://t.me/AviaxSupport"),
                InlineKeyboardButton("UpDate 📢", url=f"https://t.me/AviaxOfficial"),
            ],
            [
               InlineKeyboardButton("❌ Close", callback_data="cls"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

@Client.on_message(filters.command(["start", "active"], [".", "/", "!"]))
async def start_private(client: Client, message: Message):
   await message.delete() 
   await message.reply_text(f"**Hey 👋** {message.from_user.mention()}`\n\nWelcome To AviaxSpamBot`\n`This SpamBot Is Powerfull SpamBot Made On Python With PyroGram`\n\n`This Is Open Source SpamBot To Raid Chats In TeleGram Within Fight Between Two Clan Or Between To People`\n\n`Please Not That Anything Wrong Happeneds With This SpamBot To Anyone Then We Are Not Responsible Cause We Just Created The Source Not The Handler Of The Bot!`",
                    reply_markup=keyboard,                     
) 
