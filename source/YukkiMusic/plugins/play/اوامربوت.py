import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from config.config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from typing import Union

from pyrogram.types import InlineKeyboardButton

from YukkiMusic.utils.inline import settings

from config import GITHUB_REPO
from YukkiMusic import app
import config

from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)
@app.on_message(
    command(["المكالمة","المكالمه"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_animation(
       animation=f"https://telegra.ph/file/c6d455069abd30e415e93.mp4",
        caption=f""" ↤ ** اهلا بك عزيزي ** \n**في اوامر التشغيل بالمكالمه **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تشغيل بالقناة", callback_data=f"ddd"),
                    InlineKeyboardButton(
                        "تشغيل بالقروب", callback_data=f"tt"),
                       ],
                [
                    InlineKeyboardButton(
                        "اوامر DEV", callback_data=f"dss"),
                    InlineKeyboardButton(
                        "اوامر المتحكم", callback_data=f"abf"),
                       ],
                [
                    InlineKeyboardButton(
                        "وضع التشغيل", callback_data="PM"),
                    ],
                [
                    InlineKeyboardButton(
                       "𝘴𝘰𝘶𝘳𝘤𝘦 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 ♪", url=f"{SUPPORT_CHANNEL}"),
                    
                    ],
                [
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                    
                    
                     ],
            ]
        ),
    ) 
