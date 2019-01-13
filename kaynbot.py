import discord
from discord.ext import commands
import async

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def kill():
    await bot.say('Just one kill?:c')
@bot.command()    
async def love():
	await bot.say('I only love myself.')
@bot.command()	
async def ping():
	await bot.say('How dare you?')
@bot.command()
async def idk():
    	await bot.say('SPEAK ENGLISH YOU MOTHERFUCKER!')
@bot.command()
async def Taric():
	await bot.say('I DONT WANT TO BE TOUCHED BY A GAY')
@bot.command()
async def marry():
	await bot.say('I.ll only get married with MY Owner ❤')
@bot.command()
async def helpmepls():
	await bot.say('Here are the commands.. Even tho u don.t need them bcs u.ll be my next victim.Taric, marry, kill, idk, love, ping.')
bot.run('NTMyNjM4MjIxMjM5MTg5NTE0.DxkbPw.lPib6xMkb9JQH8euqlLJKaI1gJc')
