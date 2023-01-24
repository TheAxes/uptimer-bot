import os
############################
os.system("pip install httpx")
os.system("pip install requests")
os.system("pip install discord")
import httpx
import time
import requests
import discord
import asyncio
import json
from discord.ext import commands, tasks
from webserver import keep_alive


with open('config.json') as f:
    config = json.load(f)

prefix = config.get('prefix')
statusname = config.get('activity')
interval = config.get('ping_time')
intents = discord.Intents.all()
client = commands.Bot(description='Uptimer.Exe', command_prefix=prefix, intents=intents, case_insensitive=True, help_command=None)
token = os.getenv("token")
webhook = os.getenv("webhookurl")


######################
# Made By The Axes Very Ez #
#### Daddy Code ########


@client.event
async def on_ready():
	game = discord.Game(
	name=statusname
	)
	await client.change_presence(activity=game)
	print(client.user.id)
	print(f"Logged In : {client.user}")
	print("Made By : TheAxes")
	print("Social : https://youtube.com/@theaxes")
	own.start()
	
#######################

@client.command()
async def help(ctx):
	embed = discord.Embed(title=client.name, description=f"{prefix}help, {prefix}uptime <url>, {prefix}remove <url>, {prefix}total")
	embed.set_footer("Made By TheAxes ♥️")
	await ctx.reply(embed=embed)

@client.command()
async def uptime(ctx, *, url):
	await ctx.message.delete()
	urls = open("database.txt").read().splitlines()
	with open("database.txt", "a+") as ok:
		if url.startswith('http'):
			if url not in urls:
				ok.write(f"{url}\n")
				await ctx.send("Project Has Been Registered")
				ok.close()
			else:
				await ctx.send("Already In DataBase")
		else:
			await ctx.send("Please Give a https:// or http:// url")

@client.command()
async def remove(ctx, *, url):
	urls = open("database.txt").read().splitlines()
	if url in urls:
		with open("database.txt", "r") as f:
			lines = f.readlines()
			with open("database.txt", "w") as f:
				for line in lines:
					if line.strip("\n") != url:
						f.write(line)
						await ctx.send("Project Has Been Removed.")
	else:
		await ctx.send("Project Not Found In DataBase.")
		
@client.command()
async def total(ctx):
	urls = open("database.txt").read().splitlines()
	embed = discord.Embed(title="Uptime | Total", description=f"`Total` : {len(urls)}\n{urls}")
	await ctx.send(embed=embed)
		
		
@tasks.loop(seconds = interval)
async def own():
	urls = open("database.txt").read().splitlines()
	for web in urls:
		try:
			req = httpx.get(web)
			req2 = httpx.get(web)
			send(req.status_code, req2.status_code, web)
		except Exception as e:
			print(e)
			
def send(req, req2, web):
	data = {
	"username" : "Uptimer"
	}
	data["embeds"] = [
	{
	"description" : f"Website : `{web}`\n`Get` : {req}\n`Post` : {req2}",
	"title" : "Uptime Status"
	}
	]
	requests.post(webhook, json = data)
	

keep_alive()
client.run(token)
#########################
