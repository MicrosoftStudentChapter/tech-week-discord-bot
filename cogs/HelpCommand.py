import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand is online.")

    @commands.command(name='help')
    async def custom_help(self, ctx):
        help_embed = discord.Embed(
            title="Help Desk for Tech-Week-Discord-Bot",
            description="All commands for the bot.",
            color=discord.Color.random()
        )
        
        # Get the bot's avatar URL safely
        avatar_url = self.client.user.avatar.url if self.client.user.avatar else self.client.user.default_avatar.url

        help_embed.set_author(
            name="Tech-Week-Discord-Bot",
          icon_url=avatar_url  # Use self.client instead of self.bot
        )
      
        help_embed.add_field(name="Register", value="Register for the tech week.There will be 3 departments Technical,Design and Presentation.You can choose any 2 departments as per priority.(Joining two departments are necessary)", inline=False)
       
        await ctx.send(embed=help_embed)

async def setup(client):
    await client.add_cog(HelpCommand(client))  # Use client instead of bot in add_cog
