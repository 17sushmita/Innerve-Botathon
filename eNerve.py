import discord
import discord.ext.commands as commands
import dotenv
import os
import random
dotenv.load_dotenv()


bot = commands.Bot(command_prefix='.')


# @bot.event
# async def on_ready():
#     print("I'm online")
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')


@bot.event
async def on_message(message):
    if message.content == "Hello":
        await message.channel.send("Hello!")
    await bot.process_commands(message)

@bot.command(aliases=['hello'])
async def ping(ctx):
    await ctx.send('Pong!')



bot.run(os.getenv('TOKEN'))