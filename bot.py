import time
import os
from time import sleep

import discord
from discord import VoiceClient, channel, guild, state

client = discord.Client()
TOKEN = os.environ.get('DISCORD_TOKEN')

@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    if member.bot:
        return
    
    if before.channel != after.channel:
        if after.channel is not None:
            channel = member.voice.channel
            vc = await channel.connect()
            print("入店")
            vc.play(discord.FFmpegPCMAudio("familymart.wav"))
            time.sleep(6.5)
            await vc.disconnect()

        if before.channel is not None:
            print("退店")

client.run(TOKEN)
