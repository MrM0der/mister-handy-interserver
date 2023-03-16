import os
import discord
from discord.ext import commands
import asyncio
import datetime

class interserv(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot


    @commands.Cog.listener()
    async def on_message(self, message):
        everyone_content = message.content.replace('@everyone', '@еveryone')
        here_content = everyone_content.replace('@here', '@hеre')
        channels = []
        #
        try:
            for w in await self.Bot.get_channel(754288078637760513).history(limit=None).flatten():
                if(w.author.bot):
                    channels.append(int(w.content))
        except:
            pass
        #
        logs_channel = 689861452575670400
        if message.author.id != self.Bot.user.id:
            if message.channel.id in channels:
                if message.author.bot == False:
                    emb1 = discord.Embed(description=f'{here_content}')
                    emb1.set_author(name=f'{message.author}', icon_url=f'{message.author.avatar_url}')
                    emb1.add_field(name='channel', value=f'**name:** {message.channel}\n**id:** {message.channel.id}', inline=False)
                    emb1.add_field(name='guild', value=f'**name:** {message.guild}\n**id:** {message.guild.id}', inline=False)
                    emb1.set_footer(text=f'author id: {message.author.id}')
                    try:
                        emb1.add_field(name='file', value=f'**url:** [{message.attachments[0].filename}]({message.attachments[0].url})', inline=False)
                    except:
                        pass
                    await self.Bot.get_channel(logs_channel).send(embed = emb1)
                    Hentai = len(channels)
                    while Hentai > 0:
                        Hentai -= 1
                        await asyncio.sleep(0.1)
                        if message.channel.id != int(channels[Hentai]):
                            try:
                                await self.Bot.get_channel(int(channels[Hentai])).send(f"**{message.author.name}** - {here_content}")
                            except:
                                pass
                            try:
                                emb = discord.Embed(description=f'{message.author.name} отправил файл [{message.attachments[0].filename}]({message.attachments[0].url})', timestamp=datetime.datetime.utcnow(), color=0x36393F)
                                emb.set_image(url=f'{message.attachments[0].url}')
                                emb.set_footer(text=f'Перенаправил из: {message.channel} • Автор: {message.author.name}')
                                await self.Bot.get_channel(int(channels[Hentai])).send(embed = emb)
                            except:
                                pass




def setup(Bot):
    Bot.add_cog(interserv(Bot))