

import asyncio
from pyrogram import idle
from Aviax import bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, LOGGER

async def main():
    await bot1.start() 
    await bot1.send_message(
            LOGGER, 
            "<b> Congrats!! AviaSpamBot Started Successfully!</b>", 
        ) 
    if bot2:
       await bot2.start() 
       await bot2.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           )
    if bot3: 
       await bot3.start() 
       await bot3.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           ) 
    if bot4:
       await bot4.start() 
       await bot4.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           )
    if bot5:
       await bot5.start() 
       await bot5.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           ) 
    if bot6:
       await bot6.start() 
       await bot6.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           )
    if bot7: 
       await bot7.start() 
       await bot7.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           )
    if bot8:
       await bot8.start() 
       await bot8.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxpamBot Started Successfully!</b>", 
           )
    if bot9:
       await bot9.start() 
       await bot9.send_message(
               LOGGER, 
               "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           )
    if bot10: 
       await bot10.start() 
       await bot10.send_message(
                LOGGER, 
                "<b> Congrats!! AviaxSpamBot Started Successfully!</b>", 
           ) 
    await idle()




'''SPAM BOT LOGS'''

botlogs = "Yeah Your Spam Bot Deploying Successfully, "
team = "© TeamAviax"
c = botlogs + team
print(c)


    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
