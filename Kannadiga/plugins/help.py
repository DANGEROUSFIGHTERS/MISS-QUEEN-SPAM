from Kannadiga import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Kannadiga import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/e19ba5f20ce63ebe35d55.jpg"

ZAID_Help = "β€οΈπ MISS QUEEN SPAM πβ€οΈ\n\n"
 
ZAID_Help += f"_α΄α΄Ι΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ α΄α΄α΄α΄ΚΚ Κα΄α΄__\n\n"

ZAID_Help += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

ZAID_Help += f" `.ping` - to check ping\n `.alive` - To Check Bot Alive/Version (Only Main Userbot Will Reply)\n .`restart` - To Restart All Spam Bot \n `.addecho` - To Add Echo \n `.rmecho` - To Remove Echo \n `.addsudo` - To Add Sudo User Using Spam Bot \n\n"
 
ZAID_Help += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

ZAID_Help += f" `.leave` - To Leave Public/Private Channel/Groups\n\n"
 
ZAID_Help += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

ZAID_Help += f" `.raid` - To Raid\n `.replyraid` - To Active Reply Raid\n `.dreplyraid` - To Deactivate Reply Raid\n `.spam` - This Is Used For Normal Spam\n `.bigspam` - This Is Used For Big Spam\n `.uspam` - This Is Used For Unlimited Spam Unt You Restart The Bots!!\n `.delayspam` - This Is Used For Delay Spam\n\n"

ZAID_Help += f" .zaidspam - Ιͺ α΄‘ΙͺΚΚ κ±α΄Ι’Ι’α΄κ±α΄ α΄α΄Ι΄'α΄ α΄κ±α΄ α΄ΚΙͺκ± α΄α΄α΄α΄α΄Ι΄α΄ππβ§\n\n"

ZAID_Help += f"Β© @MISS_QUEEN_YT_OP\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=ZAID_Help,
                                  buttons=[
        [
        Button.url("β€οΈ α΄Κα΄Ι΄Ι΄α΄Κ β€οΈ", "https://t.me/KANNADIGA_BOTS")
        ] 
        ]
        )                                                         
