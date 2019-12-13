from datetime import datetime 
from peewee import *

user = 'Mell'
password = 'sergey1993'
db_name = 'peewee_demo'


dbhandle = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)
class BaseModel(Model):
    class Meta:
        database = dbhandle
class Category(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    created_at = DateTimeField(
        default=datetime.now()
    )
    updated_at = DateTimeField(
        default=datetime.now()
    )
    class Meta:
        db_table = "categories"
        order_by = ('created_at',)
class Product(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    price = FloatField(default=None)
    category = ForeignKeyField(
        Category, related_name='fk_cat_prod',
        to_field='id', on_delete='cascade',
        on_update='cascade'
    )
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
    class Meta:
        db_table = "products"
        order_by = ('created_at',)
if __name__ == '__main__':
    try:
        dbhandle.connect()
        Category.create_table()
    except InternalError as px:
        print(str(px))
    try:
        Product.create_table()
    except InternalError as px:
        print(str(px))
def add_category(name):
    row = Category(
        name=name.lower().strip(),
    )
    row.save()
def add_product(name, price, category_name):
    cat_exist = True
    try:
        category = Category.select().where(
            Category.name == category_name.strip()).get()
    except DoesNotExist as de:
        cat_exist = False
    if cat_exist:
        row = Product(
            name=name.lower().strip(),
            price=price,
            category=category
        )
        row.save()

add_category('Books')
add_product('C++ Premier', 24.5, 'books')
add_product('Juicer', 224.25, 'Electronic Appliances')


def find_all_categories():
    return Category.select()


def find_all_products():
    return Product.select()


# print(f'Cat {find_all_categories}')
# print(f'prod {find_all_products}')    



products = find_all_products()
product_data = []
for product in products:
    product_data.append({'title': product.name, 'price':product.price,'category': product.category.name})
# print(product_data)






def find_product(name):
    return Product.get(Product.get(Product.name == name.lower().strip()))

p = find_product('c++ premier')
print(p.name)
print(p.category.name)





def update_category(id,new_name):
    category = Category.get(Category.get(Category.id == id))
    category.name = new_name
    category.save()

update_category(2,'Kindle book')    