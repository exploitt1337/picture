import os, sys, json, time, random, asyncio, threading, requests
#os.system("pip install aiohttp")
os.system("pip install -U git+https://github.com/Rapptz/discord.py")
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound

auth = ["1003550935253000233"]

tkn = os.environ['tkn']
prefix = ";"
shards = 1



intents = discord.Intents.all()
intents.members = True
intents.messages = True
headers = {'Authorization': "Bot {}".format(tkn)}
client = commands.AutoShardedBot(shard_count=shards, command_prefix=prefix, case_insensitive=True, intents=intents)

client.remove_command('help')

def get_id():
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  char1 = random.choice(chars)
  char2 = random.choice(chars)
  char3 = random.choice(chars)
  char4 = random.choice(chars)
  char5 = random.choice(chars)
  return "%s%s%s%s%s" % (char1, char2, char3, char4, char5)
#endpoint = "https://discord.com/api/v9/channels/%s/messages", json={'content': msg}, headers=headers)"
def load_db():
  with open('id.json') as f:
    return json.load(f)


async def __start(fetch, guild, channel):
  session = requests.Session()
 # r = requests.post(endpoint % (chan), json=)
  g = client.get_guild(fetch)
  postman = client.get_guild(guild)
  ch2 = g.get_channel(1003645954194407444)
  ch = postman.get_channel(channel)
  while True:
    try:
      f = open("blacklist.txt", "r")
      blacklist = f.read()
      randomizer = random.choice(g.members)
      if randomizer.bot:
        continue
      elif str(randomizer.id) in str(blacklist):
        continue 
      assigned_id = get_id()
      #fr = load_db()
     # fr[str("%s" % (assigned_id))] = "%s" % (randomizer.id)
    #  with open('id.json', 'w') as f:
       # json.dump(fr, f, indent=2)
      pfp = randomizer.avatar.url
      r = session.get(pfp)
      f = open("socials.png", "wb")
      f.write(r.content)
      #file = discord.File("socials.png", filename="socials.png")

      em = discord.Embed(color=00000, title="picture")
      em.set_image(url=pfp)
      
      em.set_footer(text=".gg/socials | %s" % (assigned_id))
      await ch.send(embed=em)
      await ch2.send(embed=em)

  


@client.event
async def on_ready():
  print("rdy")
  os.system("clear")
  fetch = 952495772073619466
  snap = 1003642253597753354
  snapd = 1003550935253000233
  # await _start(fetch, snapd, snap)

@client.command()
async def help(ctx):
  em = discord.Embed(color=00000, description=";start - `starts sending random pfps in channel`\n;stop - `stops sending random pfps in channel`")
  await ctx.send(embed=em)

@client.command(aliases=["start", "stop"])
async def _start(ctx):
  while True: 
    av = random.choice(open("database.txt", "r").readlines())
    g = client.get_guild(872019984019247124)
    ch = g.get_channel(1052527319203450880)
    assigned_id = get_id()
    em = discord.Embed(color=00000)
    em.set_image(url="https://%s" %(content))
    em.set_footer(text="socials | %s" % (assigned_id))
    await ch.send(embed=em)
    print("[INFO]: successfully posted:", content)
    
    
    


@client.command()
@commands.is_owner() 
async def blacklist(ctx, pfpid):
  await ctx.send("successfully removed pfp with id `%s` from the pfp database" % (pfpid))
  f = load_db()
  bl = f["%s" % (pfpid)]
  fr = open("blacklist.txt", "a")
  fr.write("%s\n" % (bl))


@client.command(aliases=["invite"])
async def inv(ctx):
  em = discord.Embed(color=00000, description="<:xext:995948488430985216> [invite](https://dsc.gg/picturez)")
  await ctx.send(embed=em)

  
try:
  client.run(tkn, reconnect=True)
except:
  os.system("kill 1")

