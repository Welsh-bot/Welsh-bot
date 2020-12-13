import discord
from discord.ext import commands
from gt import mimic
import random
import asyncio
def to_piglatin(sentence):
        t = lambda str: str[0]+str[1]
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
        sentence = sentence.split()
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i+'ay'
                elif t(i) in lst:
                        sentence[k] = i[2:]+i[:2]+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:]+i[0]+'ay'
        return ' '.join(sentence)


class Fun(commands.Cog):
    """Commands used to have some fun!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
    @commands.command()
    async def say(ctx, *, arg):
      await ctx.send(arg)
    @say.error
    async def sayerror(ctx, error):
      await ctx.send("You did not pass anything")
    @commands.command(aliases=['backwords'])
    async def reverse(self,ctx, *, string=None):
      """Reverses the input!"""
      if string==None:
        return await ctx.send("Please provide the s parameter (What to reverse)")
      rs = string[::-1]
      return await mimic(ctx.message, rs)
    @commands.command()
    async def heyho(self,ctx):
      """Hey, Ho! Hey, Ho!"""
      msg = await ctx.send("Hey")
      await asyncio.sleep(1)
      await msg.edit(content="Ho!")
      x = 1
      y = 10
      while not x==y:
        await asyncio.sleep(1)
        await msg.edit(content="Hey")
        await asyncio.sleep(1)
        await msg.edit(content="Ho!")
        x+=1
      return msg
    @commands.command(aliases=['platin', "pigl", "piglat"])
    async def piglatin(self, ctx,*, sentence="Input `piglatin *sentence*` and that sentence will be converted!"):
        """Converts sentence to pig latin"""
        embed=discord.Embed(title="Translation", color=discord.Color.blurple())
        embed.add_field(name="English(?)",value=sentence)
        embed.add_field(name="Pig latin",value=to_piglatin(sentence))
        return await ctx.send(embed=embed)
    @commands.command(aliases=['burn'])
    async def roast(self, ctx, user:discord.Member):
        """There is only one roast rn lol"""
        roast=random.choice((f"Hey I would like to report {user.name}, they need their existence licence removed.",))
        return await ctx.send(roast)
    @commands.command(aliases=['fquote'])
    async def fakequote(self, ctx):
        """Get a very real quote!11!!11!1!1!!"""
        quote=random.choice(("Help", "Everything on the Internet is real", "My ass is burning", "Epstein didn't kill himself", "My friend thinks he is smart. He said onions are the only food that makes you cry. So I threw a coconut on his face.", "If we’re ever in a situation where I am the “Voice of reason” then we are in a very very bad situation.", "I never dreamed I’d grow up to be an asshole but here I am killin’it", "The fact that there’s a highway to hell and only a stairway to heaven says a lot about anticipated traffic numbers.", "Some people think that the truth can be hidden with a little cover-up and decoration. But as time goes by, what is true is revealed, and what is fake fades away.", "You got nothing to lose. You don't lose when you lose fake friends.", "People like to tear you down. People are always going to take shots. You've just got to go for it.", "I wonder if this is fake?"))
        author=random.choice(ctx.message.guild.members).name
        return await ctx.send(quote+" -"+author)
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        """The 8ball, providing ass advice™. Just input a question and get an answer!"""
        a = random.choice(("Yes", "It is certain","Without a doubt","You may rely on it","Yes definitely","It is decidedly so","As I see it, yes","Most likely","Outlook good","Signs point to yes","Reply hazy try again","Better not tell you now","Ask again later","Cannot predict now","Concentrate and ask again", "Maybe", "No", "Maybe yes", "Maybe no","Don’t count on it","Outlook not so good","My sources say no","Very doubtful","My reply is no",f"It's obvious that the answer is {random.choice(('Yes', 'No'))}","Let me think on that...", "You tell me"))
        if "is 9ball better" in question.lower():
          a="Nada, lol"
        elif "9ball is better" in question.lower():
          a="Nope."
        return await ctx.send(f"🎱 Question: {question} 🎱 Answer: {a} 🎱")
def setup(bot):
    bot.add_cog(Fun(bot))