import os, sys, json, time, random, asyncio, threading, requests
#os.system("kill 1")
#os.system("pip install aiohttp")
#os.system("pip install jishaku")
#os.system("pip install discord")
os.system("pip install -U git+https://github.com/Rapptz/discord.py")
import discord
#os.system("pip install requests")
#os.system("pip install dhooks")
#from dhooks import Webhook, File
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

client.lava_nodes = [

    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'idk',
        'region': 'singapore'
    }

]
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


async def _start(fetch, guild, channel):
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
      
      em.set_footer(text=".gg/picture | %s" % (assigned_id))
      await ch.send(embed=em)
      await ch2.send(embed=em)
      try:
        rntg = client.get_guild(982598075866558524)
        rntop = rntg.get_channel(1003673771565137920)
        await rntop.send(embed=em)
      except:
        pass
      try:
        marvelg = client.get_guild(1004064880783011973)
        marvel = marvelg.get_channel(1010449154834706543)
        await marvel.send(embed=em)
      except:
        pass
      try:
        pfphubg = client.get_guild(1002557931402821684)
        pfphub = pfphubg.get_channel(1011271288729378886)
        await pfphub.send(embed=em)
      except:
        pass
      try:
        soulsg = client.get_guild(997226619863314432)
        souls = soulsg.get_channel(1000307154269523968)
        await souls.send(embed=em)
      except:
        pass
      try:
        notfenixx = client.get_guild(1010495765271019530)
        notfenix = notfenixx.get_channel(1013387782443515944)
        await notfenix.send(embed=em)
      except:
        pass
      try:
        notfenixx2 = client.get_guild(993003252335525968)
        notfenix2 = notfenixx2.get_channel(1013688027643662408)
        await notfenix2.send(embed=em)
      except:
        pass 
      await asyncio.sleep(6)
    except:
      continue 



  


@client.event
async def on_ready():
  print("rdy")
  fetch = 952495772073619466
  snap = 1003642253597753354
  snapd = 1003550935253000233
  await _start(fetch, snapd, snap)

@client.command()
async def help(ctx):
  em = discord.Embed(color=00000, description=";start - `starts sending random pfps in channel`\n;stop - `stops sending random pfps in channel`")
  await ctx.send(embed=em)

@client.command(aliases=["start", "stop"])
async def _start169(ctx):
    return await ctx.send("unauthorized")


@client.command()
@commands.is_owner() 
async def blacklist(ctx, pfpid):
  await ctx.send("successfully removed pfp with id `%s` from the pfp database" % (pfpid))
  f = load_db()
  bl = f["%s" % (pfpid)]
  fr = open("blacklist.txt", "a")
  fr.write("%s\n" % (bl))
# @client.command()
# async def exploit(ctx):
#   await ctx.send("started fucking lgn's server")
#   g = client.get_guild(952495772073619466)
#   ch = g.get_channel(1003645954194407444)
#   em = discord.Embed(color=00000)
#   em.set_image(url="https://media.discordapp.net/attachments/1006651042911486032/1007125368106405999/IMG_20220811_084619.jpg?width=606&height=606")
#   em.set_footer(text=".gg/picture")
#   while True:
#     await ch.send(embed=em, delete_after=1)

@client.command(aliases=["invite"])
async def inv(ctx):
  em = discord.Embed(color=00000, description="<:xext:995948488430985216> [invite](https://dsc.gg/picturez)")
  await ctx.send(embed=em)


@client.event
async def on_message(msg):
  await client.process_commands(msg)
  if msg.channel.id == 1009699405798068317 and msg.author.id == 873533719900721212:
    content = msg.content
    random_delay_ = random.randint(4, 18)
    await asyncio.sleep(random_delay_)
    g = client.get_guild(952495772073619466)
    postman = client.get_guild(1003550935253000233)
    ch2 = g.get_channel(1003645954194407444)
    ch = postman.get_channel(1003642253597753354)
    rntg = client.get_guild(982598075866558524)
    rntop = rntg.get_channel(1003673771565137920)
    assigned_id = get_id()
    em = discord.Embed(color=00000, title="picture")
    em.set_image(url="https://%s" %(content))
    em.set_footer(text=".gg/picture | %s" % (assigned_id))
    await ch.send(embed=em)
    await ch2.send(embed=em)
    await rntop.send(embed=em)
    marvelg = client.get_guild(1004064880783011973)
    marvel = marvelg.get_channel(1010449154834706543)
    await marvel.send(embed=em)
    pfphubg = client.get_guild(1002557931402821684)
    pfphub = pfphubg.get_channel(1011271288729378886)
    await pfphub.send(embed=em)
    soulsg = client.get_guild(997226619863314432)
    souls = soulsg.get_channel(1000307154269523968)
    await souls.send(embed=em)
    notfenixx = client.get_guild(1010495765271019530)
    notfenix = notfenixx.get_channel(1013387782443515944)
    await notfenix.send(embed=em)
    notfenixx2 = client.get_guild(993003252335525968)
    notfenix2 = notfenixx2.get_channel(1013688027643662408)
    await notfenix2.send(embed=em)


  

client.run(tkn, reconnect=True)

