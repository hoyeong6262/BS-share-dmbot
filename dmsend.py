
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('따라하기')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 416903534160642049:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="따라가기봇 ")
                        embed.add_field(name="테스트중!", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/3Rsg9Bb")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzQyNzIyMjk5NTM0NTA4MDgz.XzKQCw.L-faKASl03hjZzCDh9nnLPOs5X8')
