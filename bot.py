import discord
import search_runpee 


runpee_web = search_runpee.RunPeeWeb()

no_result_message = '''Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, 
but you can subscribe to our news letter for updates of our newest content 
--> https://runpee.com/about-runpee/runpee-movie-newsletter/'''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content.lower()

    if message.content.startswith(f'$hello'):

        await message.channel.send("Hello There! I1m the bad robot you fart face.")

    if f'$search' in message_content:

        key_words, search_words = runpee_web.key_words_search_words(message_content) 
        result_links = runpee_web.search(key_words)
        links = runpee_web.send_link(result_links, search_words)

        if len(links) > 0:
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)            






client.run('ODgwMDkzMTU3NzQyNzUxODE2.YSZQoA.fz29M1pMFeuSIZofGtGlCNg_1VI')    