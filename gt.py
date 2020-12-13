import aiohttp
import discord
def allmembers(bot, exclude):
        result = []
        for guild in bot.guilds:
            for member in guild.members:
             if not member.guild in exclude:
              result += bot.get_user(member.id)
        return result
async def mimic(msg=None, content=None, username=None, avatar_url=None, channel=None):
       url=None
       if not msg==None:
           if content==None:
            content=msg.content
           if username==None:
            username=msg.author.display_name
           if avatar_url==None:
            avatar_url=msg.author.avatar_url
           if channel==None:
            channel=msg.channel
       for webhook in await channel.webhooks():
         if webhook.name == "Welshhook":
           url = str(webhook.url)
       if url==None:
         webhook = await channel.create_webhook(name="Welshhook")
         url = str(webhook.url)
       async with aiohttp.ClientSession() as s:
          webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(s))
          await webhook.send(content, username=username, avatar_url=avatar_url)
          if not msg==None:
            await msg.delete()