#Dj
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

SLIST = """List of Shows"""


@Client.on_message(filters.command("slist"))
async def sslist(bot, message):
        buttons = [[
                    InlineKeyboardButton('RadhaKrishn', callback_data='rk'),
                    InlineKeyboardButton('Jklk', callback_data='jklk')
                ],[
                    InlineKeyboardButton('MahaBharat 2013', callback_data="mb_new"),
                    InlineKeyboardButton('Buddha', callback_data="buddha")
                ],[
                    InlineKeyboardButton('Ramayan', callback_data='ramayan'),
                    InlineKeyboardButton('Shri Mahapuran', callback_data='mahap')
                ],[
                    InlineKeyboardButton('Meera', callback_data='meera'),
                    InlineKeyboardButton('Jai Deva Shri Ganesha', callback_data='ganesha')
                ],[
                    InlineKeyboardButton('Mahishasur Vadh', callback_data='mvadh'),
                    InlineKeyboardButton('Ramyug', callback_data='ramyug')
                ],[
                    InlineKeyboardButton('YMKN', callback_data='ymkn'),
                    InlineKeyboardButton('Brij Ke Gopal', callback_data=f'bkg')
                ],[
                    InlineKeyboardButton('KBMGKS', callback_data="kbmgks"),
                    InlineKeyboardButton('Maa Vaishnodevi', callback_data="maa_v")
                ],[
                    InlineKeyboardButton('Devi Aadiparashakti', callback_data='devi'),
                    InlineKeyboardButton('Parshuram', callback_data='parshuram'),
                ],[
                    InlineKeyboardButton('Legend of Hanuman', callback_data='loh'),
                    InlineKeyboardButton('little Krishna', callback_data='lk'),
                ],[
                    InlineKeyboardButton('Karn Sangini', callback_data='ks'),
                    InlineKeyboardButton('Kashibai', callback_data='ki')
                ],[
                    InlineKeyboardButton('Next Page >', callback_data='np')
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        p = await message.reply_text(text=SLIST, reply_markup=reply_markup)
        await asyncio.sleep(60)
        await p.delete()
    
if query.data == "np":
        buttons = [[
                    InlineKeyboardButton('Namah Laxmi Narayan', callback_data='namah'),
                    InlineKeyboardButton('Uttar Ramayan', callback_data=f'ur')
                ],[
                    InlineKeyboardButton('Krishna Balram', callback_data="kr_bm"),
                    InlineKeyboardButton('Shiv Mahapuran', callback_data="smp")
                ],[
                    InlineKeyboardButton('Jai Mahalakshmi', callback_data='ml'),
                    InlineKeyboardButton('MahaBharat 1988', callback_data='mb_old')
                ],[
                    InlineKeyboardButton('Maa Shakti', callback_data='maa_shakti'),
                    InlineKeyboardButton('Kahat Hanuman', callback_data='kh')
                ],[
                    InlineKeyboardButton('Dwarkadheesh', callback_data='dd'),
                    InlineKeyboardButton('Shri Krishna', callback_data='shrikrishna')
                ],[
                    InlineKeyboardButton('MahaKaali', callback_data='mahakaali'),
                    InlineKeyboardButton('Dhruv Tara', callback_data='dt')
                ],[
                    InlineKeyboardButton('AliBaba', callback_data="alibaba"),
                    InlineKeyboardButton('Baal Shiv', callback_data="bs")
                ],[
                    InlineKeyboardButton('Devo Ke Dev Mahadev', callback_data='dkdm'),
                    InlineKeyboardButton('Suryaputra Karn', callback_data='karn')
                ],[
                    InlineKeyboardButton('Adventure of Hatim', callback_data='hatim'),
                    InlineKeyboardButton('Dharm Yoddha Garud', callback_data='dyg')
                ],[
                    InlineKeyboardButton('Soon..', callback_data='soon')
                ],[
                    InlineKeyboardButton('Back', callback_data='fp')
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=SLIST, reply_markup=reply_markup)

elif query.data == "fp":
        buttons = [[
                    InlineKeyboardButton('RadhaKrishn', callback_data='rk'),
                    InlineKeyboardButton('Jklk', callback_data='jklk')
                ],[
                    InlineKeyboardButton('MahaBharat 2013', callback_data="mb_new"),
                    InlineKeyboardButton('Buddha', callback_data="buddha")
                ],[
                    InlineKeyboardButton('Ramayan', callback_data='ramayan'),
                    InlineKeyboardButton('Shri Mahapuran', callback_data='mahap')
                ],[
                    InlineKeyboardButton('Meera', callback_data='meera'),
                    InlineKeyboardButton('Jai Deva Shri Ganesha', callback_data='ganesha')
                ],[
                    InlineKeyboardButton('Mahishasur Vadh', callback_data='mvadh'),
                    InlineKeyboardButton('Ramyug', callback_data='ramyug')
                ],[
                    InlineKeyboardButton('YMKN', callback_data='ymkn'),
                    InlineKeyboardButton('Brij Ke Gopal', callback_data=f'bkg')
                ],[
                    InlineKeyboardButton('KBMGKS', callback_data="kbmgks"),
                    InlineKeyboardButton('Maa Vaishnodevi', callback_data="maa_v")
                ],[
                    InlineKeyboardButton('Devi Aadiparashakti', callback_data='devi'),
                    InlineKeyboardButton('Parshuram', callback_data='parshuram'),
                ],[
                    InlineKeyboardButton('Legend of Hanuman', callback_data='loh'),
                    InlineKeyboardButton('little Krishna', callback_data='lk'),
                ],[
                    InlineKeyboardButton('Karn Sangini', callback_data='ks'),
                    InlineKeyboardButton('Kashibai', callback_data='ki')
                ],[
                    InlineKeyboardButton('Next Page >', callback_data='np')
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=SLIST, reply_markup=reply_markup)

elif query.data == "rk":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BNGE1NjNkMGYtODdjOC00ZmZlLWFhM2ItZWEyZTY3MjBjYjY1XkEyXkFqcGdeQXVyNzM4MjU3NzY@._V1_.jpg")
        )
        await query.message.edit_text(
            text=script.RADHAKRISHN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "jklk":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BNTE5MzMzOTMtNTcyMi00MTM3LTk2N2MtMjQ0YWM1NTBjYWNhXkEyXkFqcGdeQXVyMTExNTQyNjk5._V1_.jpg")
        )
        await query.message.edit_text(
            text=script.JKLK,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "mb_new":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BZGZkYTdiMzQtMWE5My00NTg2LTlhNTctOTMxNzdhYTE4NzRlXkEyXkFqcGdeQXVyODAzNzAwOTU@._V1_.jpg")
        )
        await query.message.edit_text(
            text=script.MAHABHARAT_NEW,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "buddha":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.BUDDHA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ramayan":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.RAMAYAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "mahap":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.SHRI_MAHAPURAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "meera":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MEERA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ganesha":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.JDS_GANESHA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "mvadh":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MAHISHASUR_VADH,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ramyug":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.RAMYUG,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ymkn":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.YMKN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "bkg":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.BRIJ_KE_GOPAL,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "kbmgks":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.KBMGKS,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "maa_v":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MAA_VAISHNODEVI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "devi":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.DEVI_AADIPARASHAKTI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "parshuram":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.PARSHURAM,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "loh":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.LEGEND_OF_HANUMAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "lk":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.LITTLE_KRISHNA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ks":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.KARN_SANGINI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ki":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="fp")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.KASHIBAI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")


# Next Page 

elif query.data == "namah":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.NAMAH_LN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ur":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.UTTAR_RAMAYAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "kr_bm":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.KRISHNA_BALRAM,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "smp":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.SHIV_MAHAPURAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "ml":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.JAI_MAHALAKSHMI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "mb_old":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MAHABHARAT_OLD,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "maa_shakti":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MAA_SHAKTI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "kh":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.KAHAT_HANUMAN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "dd":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.DWARKADHEESH,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "shrikrishna":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.SHRI_KRISHNA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "mahakaali":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.MAHAKAALI,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Uploading..")

elif query.data == "dt":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.DHRUV_TARA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Uploading..")

elif query.data == "alibaba":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.ALIBABA,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added")

elif query.data == "bs":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.BAAL_SHIV,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Uploading..")

elif query.data == "dkdm":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.DKDM,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Uploading..")

elif query.data == "karn":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.SURYAPUTRA_KARN,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Uploading..")

elif query.data == "hatim":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.AO_HATIM,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("All Episodes Added.")

elif query.data == "dyg":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.DHARAM_YODDHA_GARUD,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Soon..")

# Soon..
elif query.data == "soon":
        buttons = [[
                    InlineKeyboardButton('Back', callback_data="np")
                  ]]        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("Paste Image link Here")
        )
        await query.message.edit_text(
            text=script.SOON,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Soon..")

