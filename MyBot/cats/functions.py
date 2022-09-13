from discord.ext.commands.context import Context
from MyBot.formatter.Formatter import Formatter
from MyBot.interfaces import CTX
from typing import Optional, TypedDict
from server.users.models import Intimacy, User
from server.cats.models import Cat
from server.channels.models import Channel

class GiveChurrResult(TypedDict):
    cat:Cat
    result: bool
    hungry: int
    churr:int
    intimacy:int
    amount:int
    message:str

class Interaction:
    formatter=Formatter()
    def __init__(self,ctx:CTX):
        self.ctx = ctx
        self.user = User.get_user_from_ctx(ctx)
        self.cat = Cat.get_cat_from_ctx(ctx)
        self.intimacy = Intimacy.get_intimacy_from_ctx(ctx)
        self.channel = Channel.get_channel_from_ctx(ctx)
        self.meow = SpeakMeow(user=self.user,cat=self.cat,intimacy=self.intimacy)
        
    def 너의이름은(self,name:str):
        self.cat.rename(name)
        self.cat.refresh()
        return True
    
    def give_churr(self,amount=1):
        if self.cat.is_hungry and self.user.have_churr(amount=amount):
            self.cat.decrease_hungry(amount=amount)
            self.intimacy.increase_intimacy(amount=amount)
            self.user.decrease_churr(amount=amount)
            self.cat.refresh()
            self.intimacy.refresh()
            self.user.refresh()
            return GiveChurrResult(amount=amount,cat=self.cat,hungry=self.cat.hungry,intimacy=self.intimacy.intimacy,churr=self.user.call,result=True) # type: ignore
        else:
            return GiveChurrResult(amount=amount,cat=self.cat,hungry=self.cat.hungry,intimacy=self.intimacy.intimacy,churr=self.user.call,result=False) # type: ignore
        
        
class SpeakMeow:
    def __init__(self,user:User,cat:Cat,intimacy:Intimacy):
        self.user = user
        self.cat = cat
        self.intimacy = intimacy
        
    @Formatter.cat_speak
    def curious(self):
        """의문스러운"""
        if self.intimacy.intimacy>=50:
            return Formatter("웨ㅔ옹?")
        else:
            return Formatter("야옹?")
    
    @Formatter.cat_speak
    def enthusiastic(self):
        """열광적인"""
        if self.intimacy.intimacy>=50:
            return Formatter("에에에옹!")
        else:
            return Formatter("야옹!")
        
    @Formatter.cat_speak
    def sad(self):
        """슬픈"""
        if self.intimacy.intimacy>=50:
            return Formatter("야아옹...?")
        else:
            return Formatter("에옹...")
        
    @Formatter.cat_speak
    def aggressive(self):
        """공격적인"""
        if self.intimacy.intimacy>=50:
            return Formatter("크르릉....")
        else:
            return Formatter("하아악!")