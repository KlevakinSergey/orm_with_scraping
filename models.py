from peewee import *
from datetime import datetime
# создание базы данных
user  = 'Mell'
password = 'sergey1993'

db_name = 'kenesh'

db = MySQLDatabase(
    user = user, password = password,
    database = db_name
)

# скилет базы
class BaseModel(Model):
    class Meta:
        database = db

class Deputy(BaseModel):
    id = PrimaryKeyField(primary_key= True)   
    name = CharField(max_length=100)
    number = CharField(max_length=100)
    bio = TextField()
    created_ad = DateTimeField(default=datetime.now())



    class Meta:
        db_table = 'deputy_data'
        order_by = ('created_at',)

try:
    db.connect()
    Deputy.create_table()


except InternalError as px:
    print(str(px))



