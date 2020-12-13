import discord
from discord.ext import commands
from gt import allmembers
import random
class Greetings(commands.Cog):
    """Just used to greet"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
    @commands.Cog.listener()
    async def on_member_join(self, member):
        bot=self.bot
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel is not None:
          if bot.get_user(member.id) in allmembers(bot, member.guild):
            await channel.send(f'Nice to see you again, {member.mention}!')
          else:
            await channel.send(f'Heya, {member.mention}.')
def setup(bot):
    bot.add_cog(Greetings(bot))