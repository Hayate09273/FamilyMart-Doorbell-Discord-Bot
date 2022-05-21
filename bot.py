import time
import os
from time import sleep

import discord
from discord import VoiceClient, channel, guild, state

client = discord.Client()
TOKEN = os.environ.get('DISCORD_TOKEN')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    if message.content == ";join"
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        
        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")
        
    elif message.content == ";leave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return
            
        await message.guild.voice_client.disconnect()
        await message.channel.send("切断しました。")
         
@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    if member.bot:
        return
    
    if before.channel != after.channel:
        if after.channel is not None:
            channel = client.get_channel(after.channel.id)
            if channel.guild.voice_client is None:
                return
            else:
                vc = channel.guild.voice_client
            print("入店")
            if vc.guild.voice_client.is_playing():
                return
            time.sleep(0.5)
            vc.play(discord.FFmpegPCMAudio("familymart.wav"))

        if before.channel is not None:
            print("退店")

client.run(TOKEN)