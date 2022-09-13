from typing import Union
from typing import List
from discord import DMChannel,PartialMessageable
from pydantic import BaseModel as Schema
from peewee import IntegerField,CharField,BooleanField,ForeignKeyField
from discord.ext.commands.context import Context
from MyBot.interfaces import CTX
from server.base.models import BaseModel,PermissionModel
from server.cats.models import Cat
class Channel(PermissionModel):
    cat = ForeignKeyField(Cat)
    name = CharField()
    
    @classmethod
    def get_channel_from_ctx(cls,ctx:CTX):
        channel = ctx.channel
        id = channel.id
        if isinstance(channel,DMChannel):
            name = f"\n{ctx.author.id}\n과(와)의 개인 놀이방"
        elif isinstance(channel,PartialMessageable):
            name = f"\n{ctx.author.id}\n과(와)의 개인 놀이방"
        elif channel.name:
            name = channel.name
        else:
            name = "뜰"
        return cls.channel_factory(ctx=ctx,id=id,name=name)
        
    @classmethod
    def channel_factory(cls,ctx:CTX,id:int,name:str):
        channel:Union[cls,None] =cls.get_or_none(id=id)
        if channel:
            if not channel.permission:
                raise
            return channel
        else:
            cat =Cat.get_cat_from_ctx(ctx)
            instance = cls.create(cat_id=cat.id,id=id,name=name)
            instance.save()
            return instance