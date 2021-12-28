import time
import os
from time import sleep

import discord
from discord import VoiceClient, channel, guild, state

client = discord.Client()
TOKEN = os.environ.get('DISCORD_TOKEN')

@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return

    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")

    elif message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")

    if message.content == "!play":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return
        message.guild.voice_client.play(discord.FFmpegPCMAudio("7eleven.wav"))

@client.event
async def on_voice_state_update(member: discord.Member, before, after):
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
