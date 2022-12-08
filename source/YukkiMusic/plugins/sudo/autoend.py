#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from strings.filters import command
import config
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import autoend_off, autoend_on
from YukkiMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**الطريقة:**\n\n/تلقائي [تفعيل|تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل التلقائي.\n\nسيترك البوت المكالمة تلقائي بعد 3 دقائق إذا ما كان فيه احد بالمكالمة .."
        )
    elif state == "تعطيل":
        await autoend_off()
        await message.reply_text("تم تعطيل التلقائي.")
    else:
        await message.reply_text(usage)
