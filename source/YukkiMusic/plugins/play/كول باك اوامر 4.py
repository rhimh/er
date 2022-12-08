import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from YukkiMusic.utils.inline import settings

from config import GITHUB_REPO
from YukkiMusic import app
import config
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
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


@app.on_callback_query(filters.regex("dss"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""↤ **اوامر المطورين :**\n\nالنشطة : يجيب لك القروبات اللي تشغل صوت حاليا\n\nفيد نشطة : يجيب لك القروبات اللي تشغل فيديو حاليا\n\nسوداء + ايدي القروب : يمنع القروب من التشغيل\n\nبيضاء + ايدي القروب : تفك منع القروب من التشغيل\n\nالقائمة السوداء : يجيب لك القروبات المحظوره من التشغيل\n\nبلوك + اليوزر او بالرد : يحظر العضو من استخدام التشغيل\n\nربلوك + اليوزر او بالرد : يفك الحظر عن العضو\n\nالمبلكين : يجيب لك قائمه المبلكين\n\nحظر ع : بالرد او باليوزر يحظره عام\n\nالغاء حظر ع : بالرد او باليوزر يفك الحظر العام\n\nالمحظورين العامه : قائمه المحظورين عام""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                    InlineKeyboardButton(
                        "رجوع", callback_data="back"),
        ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
   await query.edit_message_text(
      f""" ↤ ** اهلا بك عزيزي ** \n**في اوامر التشغيل بالمكالمه **""",
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
