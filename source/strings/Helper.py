#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**اوامر المشرفين :**



`مؤقت`  \n ✶ **للإيقاف المؤقت.**
`كمل ` \n ✶ **استئناف المؤقت.**
`كتم` \n ✶ **كتم لصوت المكالمة.**
`الغاء الكتم` \n ✶ **إلغاء كتم صوت المكالمة.**
`تخطي` \n ✶ **تخطي الاغنية.**
`وقف ` \n ✶ **لايقاف التشغيل.**
`/restart `\n ✶ ** إعادة تشغيل للبوت.**

🎷** تكرار الاغنية:**
`تكرار 10 `\n ✶**عند التفعيل ، يقوم البوت بتكرار الموسيقى التي يتم تشغيلها حاليا إلى 1-10 مرات في المكالمة . اعلى عدد للتكرار إلى 10 مرات**"""


HELP_2 = """✅**اوامر التشغيل:** 

` `تشغيل `شغل` او  \n ✶للتشغيل اكتب اسم الاغنية بعد مثال: \n `تشغيل `الفاتنه ماجد المهندس\n شغل` الفاتنه ماجد المهندس`

ربط  [يوزر القناة او ايدي القناة] \n✶ لربط القناة بالقروب ويمديك تشغل من القروب بس لازم ترفع البوت مشرف في القناة وفي القروب وتربطها مثال : \n `ربط` @IDSSDI

لتحميل مقطع فيديو او صوت الأمر:
 حمل [اسم الاغنية] `\n حمل الفاتنه ماجد المهندس`


✅قائمة التشغيل**:**
/قائمتي \n ✶ لعرض اغانيك المحفوظة في القائمة.
/حذف_قائمتي \n ✶ لحذف اغانيك المحفوظة بالقائمة.
/play  \n\n للتشغيل اكتب الأمر الذي في الأعلى ^ \n ثم اضغط على تشغيل القائمة."""


HELP_3 = """✅** اوامر القناة:**

لربط القروب بالقناة اول شي ارفع البوت مشرف في القناة وفي القروب ثم ارسل 
ربط [معرف القناة]
مثال: ` ربط @IDSSDI `


/cplay \n للتشغيل بالقناة رد على الملف الي تبي تشغله او اكتب اسم الاغنية بعد الأمر

/cplayforce \n للتشغيل بالقوة في القناة 

/cloop \n لتكرار الاغنية بالقناة واكتب الأمر مع رقم التكرار الحد 10

/cseek \n يقدم في الاغنية الي مشغلها بالقناة 10 ثواني

/cshuffle \n يشغل عشوائي قائمة التشغيل

/cskip \n للتخطي بالقناة

/cstop \n لايقاف التشغيل بالقناة

/cpause \n للايقاف المؤقت بالقناة

/cresume \n لاستئناف التشغيل بالقناة

/cmute  \n لكتم الصوت بالمكالمة في القناة.

/cunmute \n إلغاء كتم الصوت بالمكالمة في القناة

/cplayer \n لعرض قائمة التحكم بالأغاني للقناة

/cqueue \n لعرض قائمة التشغيل بالقناة."""

HELP_4 = """✅** اوامر اضافية:**

/الاوامر \n لعرض اوامر البوت .

/البنق \n لعرض البنق وسرعة البوت.

/حصة \n لعرض الاحصائيات 

/المطورين \n لعرض مطورين البوت المطورين """

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/اضف_مطور [اسم المستخدم]
/delsudo [اسم المستخدم]

🛃**<u>هيروكو:</u>**
/الاستخدام - المعدل.

🌐**الفارات**
/get_var - للحصول على الفأرة
/del_var - لحذف الفأرة
/set_var [اسم الفأرة] [الرقم] - قم بتعيين Var أو تحديث Var على heroku أو .env. منفصلة Var وقيمتها بمسافة.

🤖**<u>اوامر البوت:</u>**
/reboot - لاعادة تشغيل بوتك 
/تحديث - لتحديث البوت.
/السرعة - لقياس سرعة السيرفر
/الصيانة [تفعيل / تعطيل] 
/التسجيل [تفعيل / تعطيل] - Bot logs the searched queries in logger group.
/get_log [رقمه] - Get log of your bot from heroku or vps. Works for both.
/تلقائي [تفعيل|تعطيل] - البوت يطلع بعد 3 دقايق اذامافي احد بالمكالمة.

📈**احصائيات**
/النشطة - يطلع لك المكالمات النشطة
/stats - Check Bots Stats

⚠️**<u>القائمة السوداء:</u>**
/السوداء [ايدي القروب] - اي قروب في السوداء ما يمديه يستخدم البوت
/بيضاء [ايدي القروب] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
