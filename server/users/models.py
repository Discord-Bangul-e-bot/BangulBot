from typing import Union, overload
from peewee import CharField,IntegerField,ForeignKeyField
from discord.ext.commands.context import Context
from MyBot.interfaces import CTX
from server.base.models import BaseModel
from server.cats.models import Cat

class User(BaseModel):
    name = CharField()
    call = IntegerField(default=1)
    
    def have_churr(self,amount=1):
        if self.call >= amount:
            return True
        else:
            return False
    
    def increase_churr(self,amount=1):
        if self.call < 100:
            query = User.update(call=self.call+amount).where(User.id==self.id)
            query.execute() # type: ignore
            return True
        else:
            return False
    
    def decrease_churr(self,amount=1):
        if self.call > 0:
            query = User.update(call=self.call-amount).where(User.id==self.id)
            query.execute() # type: ignore
            return True
        else:
            return False
        
    @classmethod
    def get_user_from_ctx(cls,ctx:CTX):
        user:User = User.get_by_id(ctx.author.id)
        return user
    
    @classmethod
    def create(cls,id:int,name:str):
        instance = super().create(id=id,name=name)
        instance.save()
        return instance

    @classmethod
    def update_call(cls,id:int,name:str):
        db_user:Union[User,None] = User.get_or_none(id=id)
        if db_user:
            query = User.update(call=db_user.call+1).where(User.id == id)
            query.execute()  # type: ignore
            return db_user
        else:
            db_user = User.create(id=id,name=name)
            db_user.save()
            return db_user

class Intimacy(BaseModel):
    user = ForeignKeyField(User)
    cat = ForeignKeyField(Cat)
    intimacy = IntegerField(default=0)
    
    def increase_intimacy(self,amount=1):
        query = Intimacy.update(intimacy=self.intimacy+amount).where(Intimacy.id==self.id)
        query.execute() # type: ignore
    
    @classmethod
    def create(cls,cat_id:int,user_id:int):
        instance = super().create(cat=cat_id,user=user_id)
        instance.save()
        return instance
    
    @classmethod
    def get_intimacy_from_ctx(cls,ctx:CTX):
        user = ctx.author
        guild = ctx.guild
        if guild:
            return cls.get_intimacy(cat_id=guild.id,user_id=user.id)
        else:
            cat = Cat.get_cat_from_ctx(ctx)
            return cls.get_intimacy(cat_id=cat.id,user_id=user.id)
        
    
    @classmethod
    def get_intimacy(cls,cat_id:int,user_id:int):
        intimacy:Union[Intimacy,None] = cls.get_or_none(cat=cat_id,user=user_id)
        if intimacy:
            return intimacy
        else:
            instance = cls.create(cat_id=cat_id,user_id=user_id)
            return instance