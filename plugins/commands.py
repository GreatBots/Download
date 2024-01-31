from pyrogram import filters, Client as Mbot
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup
import bs4, requests
from bot import DUMP_GROUP
from apscheduler.schedulers.background import BackgroundScheduler
from sys import executable
from os import sys , execl , environ 
# if you are using service like heroku after restart it changes ip which avoid Ip Blocking Also Restart When Unknown Error occurred and bot is idle 
RESTART_ON = environ.get('RESTART_ON')
def restart():
     execl(executable, executable, "bot.py")
if RESTART_ON:
   scheduler = BackgroundScheduler()
   scheduler.add_job(restart, "interval", hours=6)
   scheduler.start()
@Mbot.on_message(filters.incoming & filters.private,group=-1)
async def monitor(Mbot, message):
           if DUMP_GROUP:
              await message.forward(DUMP_GROUP)
          
@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(Mbot, message):
    keyboard = [
        [InlineKeyboardButton("📣 Updates Channel", url="https://t.me/better_botz")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await message.reply(
        f"**👋🏻 Hello {message.from_user.mention()}**,\n\nI am a Telegram Bot which can download from multiple social media. Send me any **Instagram, TikTok, Twitter, Facebook, YouTube (Music and shorts)** links.",
        reply_markup=reply_markup
    )
     
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("**⁉️ Need Help**\n\nThis is user friendly bot so you can simple send your Social Media links here:) \n\n **eg:** `https://www.instagram.com/reel/CuCTtORJbDj/?igshid=MzRlODBiNWFlZA==`")
@Mbot.on_message(filters.command("donate") & filters.command("Donate") & filters.incoming )
async def donate(_, message):
       await message.reply_text(f"**Thanks For Choosing Donate 💰**\n\n**Payment Options:**\n**BuyMeCoffee :** https://www.buymeacoffee.com/ \n**UPI**`not ready yet` \n**Paypal:** https://www.paypal.me/ \n\nSent a screenshot of payment to @anocy for getting rewards")
