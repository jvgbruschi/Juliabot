import discord
from discord.ext import commands
import random
import asyncio
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
import requests
import youtube_dl

# ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
role_name = "[🎈] Plebeus"

bot = commands.Bot(command_prefix='Julia ', intents=intents)

counter = 0

@bot.event
async def on_ready():
    activity = discord.Game(name='@lunarravens on IG! 👩‍💻🌌')
    await bot.change_presence(activity=activity)
    print(chr(27) + "[2J")
    print(f'# Bot conectado como {bot.user.name} ⸜(｡˃ ᵕ ˂ )⸝♡')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=role_name)
    if role is not None:
        await member.add_roles(role)
        print(f"Gave {member.name} the {role_name} role upon joining.")


## Mandar mensagens da DM para @crowvos ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Tratar mensagens enviadas no privado
    if isinstance(message.channel, discord.DMChannel) and not message.content.startswith(bot.command_prefix):
        remetente = message.author
        destinatario = bot.get_user(327873590865428490)
        if destinatario is None:
            destinatario = await bot.fetch_user(327873590865428490)
            if destinatario is None:
                print('Não foi possível encontrar o usuário.')
                return

        await destinatario.send(f'**Mensagem de @{remetente.name}:** _"{message.content}"_')

    await bot.process_commands(message)


## Mandar mensagens com Julia mensagem [Mensagem] para @crowvos ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def mensagem(ctx, *, mensagem=None):
    if mensagem is None:
        await ctx.send('Por favor, forneça uma mensagem para ser enviada. O comando certo seria: Julia [Mensagem]')
        return

    remetente = ctx.message.author
    destinatario = bot.get_user(327873590865428490)
    if destinatario is None:
        destinatario = await bot.fetch_user(327873590865428490)
        if destinatario is None:
            await ctx.send('Não foi possível encontrar o usuário.')
            return

    await destinatario.send(f'**Mensagem de @{remetente.name}:** _"{mensagem}"_')
    await ctx.send('Mensagem enviada para @crowvos! Obrigada pelo contato! ⸜(｡˃ ᵕ ˂ )⸝♡')


## Ping ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def ping(ctx):
        await ctx.send('Pong! ~ ⸜(｡˃ ᵕ ˂ )⸝♡ **(Latência de {0} ms!)**'.format(round(bot.latency, 1)))


## Julia quieta ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def quieta(ctx):
        await ctx.send('NÃO, ME DA UM AUMENTO QUE EU FICO!')


## Mostrar comandos ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def comandos(ctx):
        embed = discord.Embed(title=f'Comandos da Julinha! * ੈ✩‧₊˚', color=0xe6b8c2)
        embed.set_thumbnail(url="https://i.imgur.com/4tHgOK6.jpg")
        embed.description = (f'Aqui estão os comandos que eu posso executar! Sempre envie "Julia " antes do comando! ⋆˚✿˖° ')
        embed.add_field(name='🌷 quieta', value=f"Me manda ficar quieta;", inline=False)
        embed.add_field(name='🎀 mensagem [Conteúdo da mensagem]', value=f"Envia uma mensagem para o @crowvos;", inline=False)
        embed.add_field(name='🌷 ping', value=f"Pong!;", inline=False)
        embed.add_field(name='🎀 sexo', value=f"Investe um valor aleatório na empresa do sexo!;", inline=False)
        embed.add_field(name='🌷 salário', value=f"Mostra o meu salário!;", inline=False)
        embed.add_field(name='🎀 frases', value=f"Uma frase dentre uma seleção será enviada!;", inline=False)
        embed.add_field(name='🌷 lembrete [Tempo (Em minutos)] [Nome do lembrete]', value=f"Cria um temporizador para eu te lembrar depois de um tempo!!;", inline=False)
        embed.add_field(name='🌷 role [Dado]', value=f"Rola um dado em formato XdY+Z!; (X = Quantidade de dados, Y = Quantidade de faces do dado, Z = Modificador)", inline=False)
        await ctx.send(embed=embed)


## Investimentos em sexo ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def sexo(ctx):
    global counter
    counter += random.randint(1, 1000)
    await ctx.send(f'Acabamos de receber investimentos para a **empresa do sexo**! O total é de: R$ {counter},00! ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა 💰')

# Julia fala sobre o salário dela: ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def salário(ctx):
        number = random.randint(1, 30)
        await ctx.send(f'Meu salário atualmente é de: {number} coxinhas por mês! (ㅠ﹏ㅠ) 🥺')

## Frases aleatórias ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def frases(ctx):
    frases = ['Pix na mão, calcinha no chão (@zenguitoy)', 'Oq é monsterfucker? (@raffa10ell)', ''] 
    frases = random.choice(frases)  
    await ctx.send(frases)


## Temporizador! ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def lembrete(ctx, tempo: int, *, mensagem: str):
    await ctx.send(f"Certo, vou lembrá-lo em {tempo} minutos: {mensagem}")
    await asyncio.sleep(tempo * 60)
    await ctx.send(f"### Lembrete para {ctx.author.mention}: {mensagem}")



## Comando secreto Clarinha! ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def clarinha(ctx):
    clarinha = [f'Oi Marcela! 💖', 'Oi Thales 😍', 'Odeio casal feliz 😡', 'ELA ME ENGANA DIZENDO QUEEEEE AMA VAI... MENTE PRA MIM! 😎','Coisa de nerdola 🙄', 'Ai que sono 😴', 'Isso foi fofo cara 👍', 'Vai se ferrar 😠', 'Vou te matar 🔪', 'Saudades dele 😢', 'Bota Veigh 🎶', 'Invejosa 🆒', 'Que ódio!! 😡']
    clarinha = random.choice(clarinha)
    await ctx.send(clarinha)


## JULIA DADOS ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def role(ctx, dice: str):
    dice_lines = dice.splitlines()
    embed = discord.Embed(title='Resultado', color=0xe6b8c2)
    embed.set_thumbnail(url="https://i.imgur.com/7DPT9E7.jpeg")
    
    for line in dice_lines:
        line = line.lower()
        if '+' in line:
            line, modifier = line.split('+')
            modifier = int(modifier)
        elif '-' in line:
            line, modifier = line.split('-')
            modifier = -int(modifier)
        else:
            modifier = 0

        if 'd' not in line:
            embed.add_field(name='Formato inválido', value=f"Use o formato xdy+z ou xdy-z na linha '{line}'")
            continue

        rolls, limit = map(int, line.split('d'))
        if rolls > 20 or limit > 1000:
            embed.add_field(name='Valor inválido', value=f"Por favor, escolha um valor menor para a quantidade de dados ou faces na linha '{line}'")
            continue

        result = [random.randint(1, limit) for _ in range(rolls)]
        total = sum(result) + modifier

        result_text = f'{result} + {modifier} = {total}'
        if total == 1:
            result_text = f'**_{result_text}_**'
        elif total == rolls * limit:
            result_text = f'**{result_text}**'
        
        embed.add_field(name=f'## Resultado do dado {line}', value=result_text, inline=False)

    await ctx.send(embed=embed)


# Julia cupiaitiqui ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def KUPIAITIQUI(ctx):
        await ctx.send('@gab3293 diz: https://www.youtube.com/watch?v=kn6LXpEcRp8!')

## JULIA ONE TIME USE ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def otu(ctx):
        embed = discord.Embed(title=f'Bem-vindes ao servidor 🌙 * ੈ✩‧₊˚', color=0xe6b8c2)
        embed.set_thumbnail(url="https://i.imgur.com/IVrhNH6.png")
        embed.description = (f'Eu sou um BOT programado pela Luna para atender a vocês! ⋆˚✿˖° ')
        embed.add_field(name='🌸 Regras', value=f"Não se esqueça de ler as #regras", inline=False)
        embed.add_field(name='🧁 Cargos', value=f"E pegue seus cargos em #cargos!", inline=False)
        await ctx.send(embed=embed)

# Infos do usuário ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣
@bot.command()
async def minfos(ctx, member: discord.Member):
    user_name = member.name
    user_id = member.id
    user_joined = member.joined_at.strftime("%d/%m/%Y %H:%M:%S")
    await ctx.send(f"Nome do usuário: {user_name}\nID do usuário: {user_id}\nEntrou em: {user_joined}")

# tempo ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def temperatura(ctx, cidade):
    api_key = "e453d3693bfab31136f857d7fc9511e9" 
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"
    
    response = requests.get(base_url)
    data = response.json()
    
    if data["cod"] == 200:
        temperatura = data["main"]["temp"]
        clima = data["weather"][0]["description"]
        temperatura2 = temperatura - 273
        await ctx.send(f"### Em {cidade}, a temperatura é de {round(temperatura2)}°C com {clima}. ☀")
    else:
        await ctx.send("Cidade não encontrada.")

# MUSICA? ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

@bot.command()
async def play(ctx, url):
    ydl_opts = {'format': 'bestaudio/best'}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
        
        
        channel = ctx.message.author.voice.channel
        voice_channel = await channel.connect()
        voice_channel.play(discord.FFmpegPCMAudio(url2))
    except Exception as e:
        await ctx.send(f"Ocorreu um erro ao tocar a música: {e}")




bot.run('[Token]')
