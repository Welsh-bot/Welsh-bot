import discord
from discord.ext import commands
import random
class Info(commands.Cog):
    """Commands used to give the user info!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
    @commands.command()
    async def ping(self, ctx):
      """Pong!"""
      msg = await ctx.send("If you see this eyy lmao")
      await msg.edit(content=f'Pong! {round(self.bot.latency, 2)} ms')
    @commands.command()
    async def info(self, ctx):
      """Info about the bot"""
      embed = discord.Embed(title="Bot info", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", color=discord.Color.blurple())
      embed.add_field(name="Bot maker", value="Just a mirror#6810")
      embed.add_field(name="Invite", value="[Welsh bot](https://tiny.cc/welshbot)")
      return await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Info(bot))