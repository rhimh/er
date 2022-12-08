#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ايقاف مؤقت",
            description=f"ايقاف التشغيل مؤقت للمكالمة.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("مؤقت"),
        ),
        InlineQueryResultArticle(
            title="استئناف التشغيل",
            description=f"استئناف التشغيل  للموقوف مؤقت.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("كمل"),
        ),
        InlineQueryResultArticle(
            title="كتم للمكالمة",
            description=f"كتم الصوت في المكالمة.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("اكتم"),
        ),
        InlineQueryResultArticle(
            title="الغاء كتم المكالمة",
            description=f"الغاء كتم الصوت في المكالمة.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("الغاء الكتم"),
        ),
        InlineQueryResultArticle(
            title="تخطي",
            description=f"تخطي الاغنية الي في المكالمة ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("تخطي"),
        ),
        InlineQueryResultArticle(
            title="انهاء",
            description="يقوم بانهاء كل مافي المكالمة من اغاني ومن قوائم تشغيل.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("ايقاف"),
        ),
        InlineQueryResultArticle(
            title="التكرار",
            description="يقوم بتكرار الموسيقى الي في المكالمة 3 مرات",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("تكرار 3"),
        ),
    ]
)
