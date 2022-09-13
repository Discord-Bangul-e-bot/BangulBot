from datetime import datetime
from typing import Optional
from peewee import Model,IntegerField,DateTimeField,CharField,BigIntegerField,BigAutoField,BooleanField
from MyBot.formatter.Formatter import Formatter
from server.base.settings import mysql_db

class BaseModel(Model):
    formatter=Formatter()
    id=BigAutoField(primary_key=True)
    created_at=DateTimeField(default=datetime.now)
    name:Optional[CharField]
    """Base Model for MySQL"""
    class Meta:
        database=mysql_db
      
    def refresh(self):
        newer_self = self.get_by_id(self.id)
        for field_name in self._meta.fields.keys(): # type: ignore
            val = getattr(newer_self, field_name)
            setattr(self, field_name, val)
        self._dirty.clear()
        
    @property
    def my_name(self):
        return self.formatter(f"{self.name}").bold().italic()

class PermissionModel(BaseModel):
    permission=BooleanField(default=True)
    
    def check_permission(self):
        if self.has_permission:
            return True
        else:
            raise
    
    @property
    def has_permission(self):
        return True if  self.permission else False
    
    def set_permission(self,permission:bool):
        query = type(self).update(permission=permission).where(type(self).id==self.id)
        query.execute() # type: ignore