class script(object):
    START_TXT = """Write Start Message Here"""

    HELP_TXT = """Help"""

    ABOUT_TXT = """About"""

    SOURCE_TXT = """Source"""

    MANUELFILTER_TXT = """.."""

    BUTTON_TXT = """.."""

    AUTOFILTER_TXT = """.."""

    CONNECTION_TXT = """.."""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: Exᴛʀᴀ Mᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""

    ADMIN_TXT = """.."""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """Not Yours."""

    OLD_ALRT_TXT = """Please Send the Request again."""

    CUDNT_FND = """I couldn't find related to this {}"""

    I_CUDNT = """Spelling should be correct 🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ and try again."""

    MVE_NT_FND = """File ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : 
• ᴜꜱᴇʀɴᴀᴍᴇ : 
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    REQINFO = """Note: First Forward File in Saved Message then Start Download."""

    SINFO = """Series Info"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """Custom Caption Here"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """.."""
    
    GFILTER_TXT = """.."""
    
    FILE_STORE_TXT = """.."""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """MythoShowBot Started"""

   
# All Shows Information #
    
    RADHAKRISHN = """rk"""
    JKLK = """jklk"""
    MAHABHARAT_NEW = """ Mahabharat 2013 """
    BUDDHA = """ Buddha """
    RAMAYAN = """ Ramayan """
    SHRI_MAHAPURAN = """ Shri Mahapuran """
    MEERA = """Meera"""
    JDS_GANESHA = """ Jai Deva Shri Ganesha """
    MAHISHASUR_VADH = """ Mahishasur Vadh"""
    RAMYUG = """ Ramyug """
    YMKN = """ ymkn """
    BRIJ_KE_GOPAL = """Brij ke gopal"""
    KBMGKS = """KBMGKS"""
    MAA_VAISHNODEVI = """ maa vaishno devi """
    DEVI_AADIPARASHAKTI = """ Devi Aadi parashakti"""
    PARSHURAM = """parshuram"""
    LEGEND_OF_HANUMAN = """ legend of Hanuman"""
    LITTLE_KRISHNA = """ little Krishna"""
    KARN_SANGINI = """ karn sangini"""
    KASHIBAI = """ kashibai"""
    NAMAH_LN = """ Namah Lakshmi Narayan """
    UTTAR_RAMAYAN = """ Uttar Ramayan"""
    KRISHNA_BALRAM = """ Krishna Balram"""
    SHIV_MAHAPURAN = """ Shiv Mahapuran"""
    JAI_MAHALAKSHMI = """ Jai Mahalakshmi"""
    MAHABHARAT_OLD = """Mahabharat 1988"""
    MAA_SHAKTI = """ Maa Shakti"""
    KAHAT_HANUMAN = """ Kahat Hanuman"""
    DWARKADHEESH = """ dwarkadheesh"""
    SHRI_KRISHNA = """ Shri Krishna"""
    MAHAKAALI = """ mahakaali """
    DHRUV_TARA = """ Dhruv Tara"""
    ALIBABA = """Alibaba"""
    BAAL_SHIV = """ Baal Shiv"""
    DKDM = """ Devi Ke Dev Mahadev"""
    SURYAPUTRA_KARN = """ Suryaputra karn """
    AO_HATIM = """ Adventure of Hatim"""
    DHARAM_YODDHA_GARUD = """ Dharam Yoddha Garud """

    SOON = """ Soon message"""
