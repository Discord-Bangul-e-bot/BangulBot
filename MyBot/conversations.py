from MyBot.base import app
from discord.ext.commands.context import Context
from server.users.models import User
from server.channels.models import Channel

@app.command()
async def 야옹(ctx:CTX):
    interaction = Interaction(ctx)
    await ctx.send(interaction.meow.enthusiastic())
    
@app.command()
async def 여긴어디야(ctx:CTX):
    interaction = Interaction(ctx)
    await ctx.send(interaction.meow.enthusiastic())
    await ctx.send(app.formatter(f"{interaction.cat.my_name}은(는) 여기가 {interaction.channel.my_name}이라고 말하는 것 같다").single_block())

@app.command()
async def 넌여기오면안돼(ctx:CTX):
    interaction = Interaction(ctx)
    await ctx.send(interaction.meow.sad())
    await ctx.send(app.formatter(f"{interaction.cat.my_name}은(는) 슬픈 표정을 지으며 떠나갔다...").single_block())
    interaction.channel.set_permission(False)
    
@app.command()
async def 이제와도돼(ctx:CTX):
    channel:Channel = Channel.get_by_id(ctx.channel.id)
    if channel.has_permission:
        interaction = Interaction(ctx)
        await ctx.send(interaction.meow.curious())
        await ctx.send(app.formatter(f"{interaction.cat.my_name}은(는) 이미 이곳을 자유롭게 드나들고 있었다."))
        await ctx.send(app.formatter(f"{interaction.cat.my_name}은(는) 당신을 이상하게 쳐다봤다"))
    else:
        channel.set_permission(True)
        interaction = Interaction(ctx)
        await ctx.send(interaction.meow.enthusiastic())
        await ctx.send(app.formatter(f"{interaction.cat.my_name}은(는) 반갑게 당신에게 달려들었다."))

@app.command()
async def 물어(ctx:CTX):
    interaction = Interaction(ctx)
    await ctx.send(interaction.meow.aggressive())
    
@app.command()
async def 사용자(ctx:Context):
    await ctx.send(f"{ctx.author.name}")
    
@app.command()
async def 호출횟수(ctx:Context):
    user:User = User.get(id=ctx.author.id)
    await ctx.send(f"{user.call}")

@app.command()
async def 종료(ctx:Context):
    await ctx.send("종료중")
    guild = ctx.guild
    if guild:
        await guild.leave()