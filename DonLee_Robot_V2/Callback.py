# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import math
import json
import time
import shutil
import heroku3
import requests
import os
import ast
from pyrogram import filters, Client as DonLee_Robot_V2
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from DonLee_Robot_V2.Config_Vars.Vars import Config
from DonLee_Robot_V2 import Text, Import, Database, all_connections, active_connection, if_active, delete_connection, make_active, make_inactive, del_all, find_filter, Database, add_user, all_users, humanbytes, filter_stats
 
db = Database()


@DonLee_Robot_V2.on_callback_query()
async def cb_handler(client, query):

    if query.data == "close":
        await query.message.delete()

    elif query.data == "home":
        button = [[  
          Import.Button("β π π½π½ π¬πΎ π³π πΈπππ π’ππΊππ β", url=f"http://t.me/{Config.BOT_USERNAME}?startgroup=true")
          ],[
          Import.Button("β οΈ π§πΎππ", callback_data="help"),
          Import.Button("π π»πππ π€ ", callback_data="about")
          ]]
        await query.message.edit_text(Text.START_TEXT.format(query.from_user.mention, Config.DEV_ID), reply_markup=Import.Markup(button))

    elif query.data == "help":
        button = [[
          Import.Button("π ππππ₯ππππΎπ", callback_data="autofilter"),
          Import.Button("π¬πΊπππΊππ₯ππππΎπ", callback_data="filter"),
          Import.Button("π’ππππΎπΌπππππ", callback_data="connection")
          ],[
          Import.Button("π‘πΊπ", callback_data="ban"),
          Import.Button("π¬πππΎ", callback_data="mute"),
          Import.Button("π―ππππΎ", callback_data="purge")
          ],[
          Import.Button("π³πΎππΎπππΊπ―π", callback_data="telegraph"),
          Import.Button("π³π³π²", callback_data="tts"),
          Import.Button("π²πππΌππΎπ π¨π½", callback_data="sticker")
          ],[
          Import.Button("π’ππππππ", callback_data="country"),
          Import.Button("π¬πΎππΎ", callback_data="meme")
          ],[
          Import.Button("π’ππππ½", callback_data="covid"),
          Import.Button("π±πΎππππ", callback_data="report"),
          Import.Button("πΆπΎππΌπππΎ", callback_data="welcome")
          ],[
          Import.Button("π π§πππΎ", callback_data="home"),
          Import.Button("π²ππΊπππ", callback_data="status"),
          Import.Button("π π»ππππ€ ", callback_data="about")
          ]]
        await query.message.edit_text(Text.HELP_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "about":
        button = [[
          Import.Button("β€οΈupdateβ€οΈ", url='https://t.me/bhiman1234')
          ],[
          Import.Button("β οΈπ§πΎππ", callback_data="help"),
          Import.Button("π π§πππΎ", callback_data="home"),
          Import.Button("π’ππππΎποΈ", callback_data="close")
          ]]
        await query.message.edit_text(Text.ABOUT_TEXT.format(Config.BOT_USERNAME, Config.DEV_ID, Config.DEV_NAME, Config.BOT_USERNAME), reply_markup=Import.Markup(button))

    elif query.data == "autofilter":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help"),
          Import.Button("π­πΎππ β‘οΈ", callback_data="autofilter1")
          ]] 
        await query.message.edit_text(Text.AUTO_FILTER_1_TEXH, reply_markup=Import.Markup(button))

    elif query.data == "autofilter1":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="autofilter")
          ]]
        await query.message.edit_text(Text.AUTO_FILTER_2_TEXH, reply_markup=Import.Markup(button))

    elif query.data == "filter":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help"),
          Import.Button("π΅ππ½πΎπ π½οΈ", url="https://youtu.be/neJ4jHC9Hng")
          ]]
        await query.message.edit_text(Text.FILTER_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "connection":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.CONNECTION_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "ban":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.BAN_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "mute":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.MUTE_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "pin":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.PIN_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "purge":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.PURGE_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "status":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help"),
          Import.Button("π", callback_data="status")
          ]]
        total_users = await db.total_users_count()
        chats, filters = await filter_stats()
        uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - Config.Up_Time))
        await query.message.edit_text(Text.STATUS_TEXT.format(total_users, chats, filters, uptime), reply_markup=Import.Markup(button))

    elif query.data == "welcome":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.WELCOME_TEXT.format(Config.CUSTOM_WELCOME, Config.CUSTOM_WELCOME_TEXT), reply_markup=Import.Markup(button))

    elif query.data == "telegraph":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.TELEGRAPH_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "covid":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.COVID_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "tts":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.TTS_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "sticker":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.STICKER_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "source":
        button = [[
          Import.Button("β€οΈupdateβ€οΈ", url='https://t.me/bhiman1234')
          ],[
          Import.Button("π π‘πΊπΌπ", callback_data="about"),
          ]]
        await query.message.edit_text(Text.SOURCE_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "meme":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.MEME_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "country":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.COUNTY_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "credits":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="source")
          ]]
        await query.message.edit_text(Text.CREDITS_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "report":
        button = [[
          Import.Button("π π‘πΊπΌπ", callback_data="help")
          ]]
        await query.message.edit_text(Text.REPORT_TEXT, reply_markup=Import.Markup(button))

    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("π¬πΊππΎ π²πππΎ π¨πΊπ π―ππΎππΎππ ππ ππππ π¦ππππ!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "π¨'π πππ πΌππππΎπΌππΎπ½ ππ πΊππ ππππππ!\nπ’ππΎπΌπ /connections ππ πΌππππΎπΌπ ππ πΊππ ππππππ",
                    quote=True
                )
                return

        elif (chat_type == "group") or (chat_type == "supergroup"):
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in Config.AUTH_USERS):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("πΈππ ππΎπΎπ½ ππ π»πΎ π¦ππππ π?πππΎπ ππ πΊπ π πππ π΄ππΎπ ππ π½π πππΊπ!",show_alert=True)
    
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type
        
        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif (chat_type == "group") or (chat_type == "supergroup"):
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in Config.AUTH_USERS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("π³ππΊππ πππ πΏππ πππ!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnectbot"

        keyboard = Import.Markup([
            [Import.Button(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                Import.Button("DπΎππΎππΎ", callback_data=f"deletecb:{group_id}")],
            [Import.Button("π‘πΊπΌπ", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"π¦ππππ π­πΊππΎ : **{title}**\nπ¦ππππ π¨π£ : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"π’ππππΎπΌππΎπ½ ππ **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return

    elif "disconnectbot" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"π£πππΌππππΎπΌππΎπ½ πΏπππ **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"π²πππΎ πΎππππ ππΌπΌπππΎπ½!!",
                parse_mode="md"
            )
            return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "π²ππΌπΌπΎπππΏππππ π½πΎππΎππΎπ½ πΌππππΎπΌππππ"
            )
            return
        else:
            await query.message.edit_text(
                f"π²πππΎ πΎππππ ππΌπΌπππΎπ½!!",
                parse_mode="md"
            )
            return
    
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "π³ππΎππΎ πΊππΎ ππ πΊπΌππππΎ πΌππππΎπΌπππππ!! π’ππππΎπΌπ ππ ππππΎ ππππππ πΏππππ",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                if active:
                    act = " - ACTIVE"
                else:
                    act = ""
                buttons.append(
                    [
                        Import.Button(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "πΈπππ πΌππππΎπΌππΎπ½ πππππ π½πΎππΊπππ;\n\n",
                reply_markup=Import.Markup(buttons)
            )
   
    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)
