import functools
from MyBot.cats.functions import Interaction

from MyBot.interfaces import CTX

def permission_check(cb):
    """this callback must have **kwargs"""
    @functools.wraps(cb)
    async def wrapper(*args,**kwargs):
        context:CTX = args[0]
        interaction = Interaction(context)
        kwargs["interaction"]=interaction
        interaction.channel.check_permission()
        result = await cb(*args,**kwargs)
        return result
    return wrapper