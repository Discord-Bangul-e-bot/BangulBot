import abc
from MyBot.formatter.Formatter import Formatter
from typing import List, Optional, TypedDict
from MyBot.interfaces import CTX
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

class BiteResult(TypedDict):
    cat:Cat
    result:bool
    churr:int
    target:Optional[User]
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
    
    def 물어(self,name:str,amount=1):
        users = self.user.find_by_name(name)
        if users:
            target:User = users[0]
            if target.have_churr(amount):
                msg = self.formatter(f"{self.cat.my_name}은(는) {target.my_name}에게서 {amount}만큼의 츄르를 빼았아왔다!").single_block()
                return BiteResult(cat=self.cat,result=True,churr=amount,target=target,message=msg)
            else:
                msg = self.formatter(f"{self.cat.my_name}은(는) {target.my_name}에게서 {amount}만큼의 츄르를 찾아 보았지만 그만큼은 없었다...")
                return BiteResult(cat=self.cat,result=True,churr=amount,target=target,message=msg)
        else:
            msg = self.formatter(f"{self.cat.my_name}은(는) {self.formatter(name).bold().italic()}을(를) 찾지 못했다....")
            return BiteResult(cat=self.cat,result=False,churr=amount,target=None,message=msg)
    
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
        