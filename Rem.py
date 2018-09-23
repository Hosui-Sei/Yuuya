import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import random
import time
import asyncio
import aiohttp
import json

client = discord.Client()
client: Bot = commands.Bot(command_prefix="%")
client.remove_command('help')
bot = client

#@client.event
#async def on_message(message):
#    if message.content.startswith("USAHSUHAUSHAUSAHDAUSDHASKUDSAHDUA"):
#        await client.send_message(message.channel, "O pora, tá dando risada pq? <@410843558590021643>")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help me, nigga!')
    embed.add_field(name='%8ball', value='Joguinho de sim ou não.', inline=False)
    embed.add_field(name='%gaymeter', value='Medidor de Homossexualidade.', inline=False)
    embed.add_field(name='%lesbianmeter', value='Medidor de Homossexualidade feminina.', inline=False)
    embed.add_field(name='%square', value='Faz um número ser elevado ao quadrado.', inline=False)
    embed.add_field(name='%help', value='Mostra esta mensagem.', inline=False)
    embed.add_field(name='%clear', value='Limpa as mensagens de um chat, por favor especifique o número para não acabar apagando 100 mensagens de uma vez. 2 a 100 mensagens.', inline=False)
    embed.add_field(name='%bitcoin', value='Mostra o preço do Bitcoin em dólar', inline=False)
    embed.add_field(name='%displayembed', value='Mostra um embed, nada demais...', inline=False)
    embed.add_field(name='%dirty', value='Oh! You have dirty panties!~', inline=False)
    embed.add_field(name='%echo', value='Repete sua mensagem "<@410843558590021643>" disse: Olá!', inline=False)
    embed.add_field(name='%ship', value='Mostra as chances de serem um casal', inline=False)
    embed.add_field(name='%flipcoin', value='Joguinho de sorte', inline=False)

    await client.send_message(author, embed=embed)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Joguinho de sim ou não.",
                aliases=['eight_ball', 'eightball', '8-ball', 'lucky-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Não',
        'Claro',
        'Difícil de responder',
        'Possível',
        'Definitivamente sim',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command()
async def suy():
    myid = '<@252431723051221002>'
    await client.say(' %s ' % myid)

@client.command()
async def mami():
    myid = '<@412453837614481439>'
    await client.say(' %s ' % myid)


@client.command()
async def yuu():
    myid = '<@410843558590021643>'
    await client.say(' %s ' % myid)


@client.command()
async def gay():
    id = 'everyone in this server'
    await client.say('%s' % id)


@client.command(pass_context=True)
async def hug(ctx, arg):
    author = ctx.message.author
    client.say("{} abraçou {}".format(author, arg))


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
       messages.append(message)
    await client.delete_messages(messages)
    await client.say('Mensagens deletadas.')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="meus comandos fora ;~;"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("O preço do BitCoin é: $" + response['bpi']['USD']['rate'])


@client.command()
async def yoah():
    myid = '<@477955694331691028>'
    await client.say(' %s ' % myid)


@client.command()
async def nevas():
    myid = '<@313306952816001034>'
    await client.say(' %s ' % myid)


@client.command()
async def drake():
    myid = '<@478592182912155651>'
    await client.say(' %s ' % myid)


@client.command(name='O quão lésbica eu sou',
                description="Fala o quanto você é lésbica",
                brief="Medidor de lésbica",
                aliases=["lesbianmeter", "lesbian-meter", "o_quao_lesbica_sou"],
                pass_context=True)
async def lesbianmeter(context):
    possible_responses = [
        '100% lésbica, meu amor',
        'Me mostra tua tesoura',
        'Vou te chupar, sua tesoura é só minha',
        'Me dá sua ppk, sua lésbica',
        'Hey, me come, sei que você é lésbica',
        'Ain~~ Minha querida, tu é com certeza uma lésbica com esses peitão e olhar',
        'SUA HÉTERA',
        '**SAI DAQUI SUA HÉTERA**',
        'Definitivamente, você é **hétera**, **ugo**',
        'Te amo meu amor, tu é claramente lésbica',
    ]
    await client.say(random.choice(possible_responses) + ', ' + context.message.author.mention)


@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'Le Criador',
        description = 'Foi ele quem criou essa bagaça.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='©2018')
    embed.set_image(url='https://cdn.discordapp.com/avatars/419300859927724032/912e64baf7d3e2954a64e7d69b6d7312.png?size=2048')
    embed.set_thumbnail(url='https://orig00.deviantart.net/e4b1/f/2016/343/2/9/_render__rem_by_eazl1999-dar42f5.png')
    embed.set_author(name='Yuu', icon_url='https://cdn.discordapp.com/avatars/410843558590021643/9649d0b5f5c4e2d0101e848e9935ad72.png?size=2048')
    embed.add_field(name='Nascimento/Birth:', value='21/09/2018', inline=False)
    embed.add_field(name='Linguagem/Language:', value='Python', inline=False)
    embed.add_field(name='Discord:', value='<@410843558590021643>', inline=False)


    await client.say(embed=embed)


@client.command(name='O_quao_gay_sou',
                description="Fala o quanto você é gay.",
                brief="Medidor de homossexualidade.",
                aliases=['gay_meter', 'gay-meter', 'o_quao_gay_sou', 'gaymeter'],
                pass_context=True)
async def gaymeter(context):
    possible_responses = [
        '100%',
        'Muito gay',
        'Difícil de responder o quão gay é você',
        'Possívelmente gay',
        'Definitivamente sim, você é gay',
        'Gay pra krl em, pqp',
        'Oloko, gostei de você :3',
        'Ain, bora pra cama \*pego em sua mão, te levo até meu quarto, tranco a porta e te jogo na cama*',
        'Ain~, totalmente hétero, **ugo**',
        'Vou te comer, meu amor',
        '\*Tira as calças e vira a bunda na direção do homem que realizou este comando* pode entrar se quiser, hehe~~',
        '**EEK, SAI FORA SEU HÉTERO',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def dirty():
    await client.say('You have dirty panties~')


@client.command(pass_context=True)
async def echo(ctx, *, arg):
    author = ctx.message.author
    await client.say("{} disse: {}".format(author.mention, arg))


@client.command(name='hot_yaoi',
                aliases=['hot-imagine', 'hot', 'NSFW-Yaoi'],
                pass_context=True)
async def hot_yaoi(context):
    possible_responses = [
        '\*Sinto que seu membro começa a pulsar, querendo liberar todo o seu esperma, então começo a ir mais rápido* Hehe~, parece que está quase em seu limite <3',
        '\*Começo a sentar em cima de seu pênis*',
        '\*Começo a chupar todo o seu membro*',
        '\*Enquanto seu membro adentra meu corpo, eu entrelaço minhas pernas em você, fazendo com que seu pênis entre mais profundamente enquanto o beijo*',
        '\*Você começa a me masturbar, enquanto te beijo neste calor imenso que nossos corpos provocam*',
        '*Hey~ A última noite foi boa não é?~ Eu fiquei louco, queria novamente e novamente, você também havia ficado louco...~* \*Sinto sua mão, pegando em meu membro, duro feito pedra* *Oh...~ Vejo que você quer novamente~* \*Deito em cima de você* *Se você deseja...~ Ganhará mais presentes deliciosos hoje...~*'
    ]
    await client.say(random.choice(possible_responses) + ' ' + context.message.author.mention)


@client.command(name='hot_yuri',
                aliases=['hot_imagine_yuri', 'hot-yuri', 'NSFW-Yuri'],
                pass_context=True)
async def hot_yuri(context):
    possible_responses = [
        ''
    ]

@client.command()
async def flipcoin():
    rndom = random.randint(0, 1)
    if rndom == 0:
        await client.say ("Cara")
    if rndom == 1:
        await client.say("Coroa")


@client.command()
async def ship(arg1, arg2):
    rndom = random.randint(0, 100)
    if rndom == 100:
        await client.say("100% de chances de serem um casal, lol eles já estão casados e você pergunta pra mim as chances, lololol")
    if 80 <= rndom <= 99:
        await client.say("80 a 99% de chances de serem um casal, :thinking: será que eles já estão namorando?")
    if 60 <= rndom <= 79:
        await client.say("60 a 79% de chances de serem um casal, :thinking: será que eles são bem amigos?")
    if 40 <= rndom <= 59:
        await client.say("40 a 59% de chances de serem um casal, devem ser apenas conhecidos :<")
    if 20 <= rndom <= 49:
        await client.say("20 a 49% de chances de serem um casal, amigos?")
    if 0 <= rndom <= 19:
        await client.say("0 a 19% de chances de serem um casal, nah, eles não combinam. Nem a pau.")

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())

client.run("NDE5MzAwODU5OTI3NzI0MDMy.DobE5A.NOqxhHAHKVmOm4_9AO6EGsPyfwM")
