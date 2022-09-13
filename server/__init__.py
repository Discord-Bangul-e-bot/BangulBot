from playhouse.migrate import migrate,MySQLMigrator
from peewee import ForeignKeyField,ColumnMetadata

from .cats.models import Cat

from .users.models import Intimacy, User
from .messages.models import Message
from .history.models import History
from .attachments.models import Attachment
from .channels.models import Channel
from .base.settings import mysql_db

def column_exists(table_name:str,column_name:str):
    result = list(map(lambda x:x.name==column_name,mysql_db.get_columns(table_name)))
    print(result)
    return any(result)

def create_tables():
    mysql_db.create_tables([User,Message,History,Attachment,Cat,Intimacy,Channel])
    
        
create_tables()