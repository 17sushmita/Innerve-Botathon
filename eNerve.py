import discord
from discord import member
from discord import message
from discord import embeds
import discord.ext.commands as commands
import dotenv
import os
import random
dotenv.load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)


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

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)    
    await ctx.send(f"You've got {result}!!")

    
@bot.command()
async def role(ctx, user:discord.Member, role:discord.Role):
    print(ctx.author, role.name)
    await user.add_roles(role)
    await ctx.send(f"{user.mention} You've been assigned the role {role.name} ")

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    print(guild.name)
    message_id = os.getenv('MESSAGE_ID')
    if payload.message_id == message_id:
        if payload.emoji.name == '👑':
            King = discord.utils.get(guild.roles, name="King")
            print(f'Reacted with emoji {payload.emoji.name}')
            await payload.member.add_roles(King)
        if payload.emoji.name == '🎤':
            Singer = discord.utils.get(guild.roles, id=899193197950021643)
            print(Singer.name)
            print(f'{payload.member.mention} Reacted with emoji {payload.emoji.name}')
            await payload.member.add_roles(Singer)
        

@bot.command()
async def raffle(ctx):
    members = await ctx.guild.fetch_members().flatten()
    winner = random.choice(members)
    chocolates = '🍫'*random.randint(1, 30)
    await ctx.send(f"Congratulations!! {winner.mention} You've won the raffle!! You've got {chocolates} as gift for you!")


@bot.command()
async def help(ctx):
    embeding = discord.Embed(description='.raffle\tChooses a lucky winner\n.role\tadd roles to users')
    await ctx.send(embed=embeding)

bot.run(os.getenv('TOKEN'))