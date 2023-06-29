import asyncio
import re
import ast
import math
import random
from Script import script
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid



@Client.on_message(filters.command("slist"))
async def sslist(bot, message):
    await message.reply_text(SLIST)

SLIST = """ """

elif query.data == "s1":
        buttons = [[
                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton('♚ Bᴏᴛ Oᴡɴᴇʀ', callback_data="owner_info"),
                    InlineKeyboardButton('⌬ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=GRP_LNK)
                ],[
                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about'),
                    InlineKeyboardButton('Iɴʟɪɴᴇ Sᴇᴀʀᴄʜ ☌', switch_inline_query_current_chat='')
                ],[
                    InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)
                  ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer(MSG_ALRT)
