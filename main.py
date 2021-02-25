import discord
import os

from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rank'):
        await message.channel.send('unfortunately still Iron')

    if message.content.startswith('$coop'):
        await message.channel.send('https://twitter.com/philliptayeri1/status/732715903280807936?s=21')
    
    if message.content.startswith('$phi'):
        await message.channel.send('Still as great and magical as ever. One of the most aesthetically pleasing movies I have ever seen with one of the best on screen chemistries to go with it. When someone asks what is cinema or what is a great film, this is a movie that immediately comes to mind.')

    if message.content.startswith('$tyler'):
        await message.channel.send('https://www.twitch.tv/dirtydanmilkman/clip/SourHilariousMeatloafDAESuppy?filter=clips&range=all&sort=time')

    if message.content.startswith('$dylan'):
        await message.channel.send('dylans CHILLIN') 
    
    if message.content.startswith('$trent'):
        await message.channel.send('fuuuuuuuuuuuuuuuhk maaaaaaaaaaahn') 
    
    if message.content.startswith('$shams'):
        await message.channel.send('uhhhh whats it called')
    
    if message.content.startswith('$andy'):
        await message.channel.send('cooper naked')

    if message.content.startswith('$2020'):
        await message.channel.send('https://open.spotify.com/playlist/3IpiLPbFWB7cSpguuNzsMF?si=hLo7qgO2RwuOip2WIgFfnA')
    
    if message.content.startswith('$pasta'):
        await message.channel.send('What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.')



keep_alive()
client.run(os.getenv('TOKEN'))