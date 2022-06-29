import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('bot is ready')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 12

    await bot.change_presence(status=discord.Status.idle, activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{members} members'
    ))

@bot.event
async def on_message(message: discord.message):
    if not message.author.bot:
        if message.content == ("سلام", "درود", "hi", "hello"):
            await message.channel.send("hello")
        if message.content == f"{bot.command_prefix}ping":
            ping = bot.latency * 1000
            await message.channel.send(f"bots ping is : {round(ping)}ms")




bot.run("OTg5ODM0MTQ2OTQxNjU3MTE4.GPH1Lm.-b12jkT39FZMEQER7snhvlXOZmAMQeylosSPBk")