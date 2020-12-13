import discord
import time
import os
import math
import asyncio
import random
print(os.getcwd())
def errepr(e, defmsg="There was an error"):
      re = repr(e)
      re = re.split("(", 1)
      err = re[0]
      msg = re[1] = re[1][:-2][1:]
      if msg=="":
        msg=defmsg
      return f"{err}: {msg}"
print(errepr(Exception("This is NOT an Exception!")))
def millify(n: int):"""Human readable numbers""";n=float(n);millnames=['','K','M','B','T'];millidx=max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))));return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
def getav(numlist):
  return sum(numlist)/len(numlist)
from keep_alive import keep_alive
from discord.ext import commands
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot = commands.Bot(command_prefix='w!', help_command = MyHelpCommand(no_category = 'General',sort_commands=False))

async def auto_status():
    while True:
        activitys = ["...                 Did you expect to find anything useful?", f"{random.choice(['Hi', 'Hello', 'Ello'])},  there{random.choice(['!', '.', '...', '!!!'])}", "I likey"]
        statuses = ["online", "idle", "dnd", "streaming"]
        raw_status = random.choice(statuses)
        def streaming(s):
          return s == "streaming"
        if not streaming(raw_status):
          status = discord.Status(raw_status)
        else:
          status = discord.Status(random.choice(["online", "idle", "dnd"]))
          url=random.choice(["https://www.twitch.tv/npesta", "https://www.twitch.tv/juniper", "https://www.twitch.tv/chriso2", "https://www.twitch.tv/ "])
        thing = random.choice(activitys)
        ranactivity = f"w!help | {thing}"
        if not streaming(raw_status):
         activity = discord.Activity(
            name=ranactivity, type=discord.ActivityType.watching)
        else:
         activity = discord.Activity(
            name=ranactivity, url=url, type=discord.ActivityType.streaming)
        await bot.change_presence(status=status, activity=activity)
        await asyncio.sleep(86400)
@bot.event
async def on_message(message):
  if not message.content.startswith("w!"):
    if "hi" in message.content.lower() or "hey" in message.content.lower() or "hello" in message.content.lower():
      if "welshbot" in message.content.lower() or "<@785167899052081193>" in message.content or "<@!785167899052081193>" in message.content or "<@&786052333343342614>" in message.content:
          async with message.channel.typing():
               await asyncio.sleep(random.uniform(1, 1.25))
               return await message.channel.send(f"{random.choice(['Hi', 'Hello', 'Lol hi'])}{random.choice([',', ''])} {message.author.name}{random.choice(['!', '.', ' :' + random.choice([')', 'P', '3', '/', '|', 'O', 'V'])])}")
    if "dead chat"==message.content.lower():
      return await message.channel.send(f"""```
+-------------------------------+
| DEAD CHAT                   X |
+-------------------------------+
|                               | 
|       The chat is dead~       |
|                               |
+-------------------------------+
```""")
  else:
   command = message.content.split(" ")
   command = command[0].replace("w!", "", 1)
   await bot.process_commands(message)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(f"Command not found, {ctx.message.author.name}!")
@bot.event
async def on_ready():
  print("Im ready!")
  await bot.change_presence(status=discord.Status("online"), activity=discord.Activity(name="Setting up cogs...", type=discord.ActivityType.watching))
  bot.load_extension("info")
  bot.load_extension("moderation")
  bot.load_extension("fun")
  bot.load_extension("greetings")
  bot.loop.create_task(auto_status())
  print("All is done! ")
@bot.command(aliases=["undeadchat", "chatlivener"])
async def livechat(ctx, wait: float=20.0):
  """Make the chat lively! ("wait" is in minutes) """
  wait=wait*60
  topics=[f"Do you like {random.choice(['cheese cake','chocolate','**me**', 'the gd youtuber morgflame'])}?"]
  await ctx.send("Alright, the loop is starting!")
  while True:
        try:
            msg = await bot.wait_for('message', check=lambda msg: msg.channel == ctx.channel,timeout=wait)
        except asyncio.TimeoutError:
            await ctx.send(random.choice(topics))
keep_alive()
bot.run(os.environ.get("BOTTOKEN"))