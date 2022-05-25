import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DbHelper:
    def __init__(self):
        self._engine = db.create_engine("sqlite:///products.db?check_same_thread=False")
        self._session = sessionmaker(bind=self._engine)()

    def get_products(self):
        return self._session.query(Product).all()

    def add_product(self, name, type, price, rating, number):
        product = Product(name=name, type=type, price=price, rating=rating, number=number)
        self._session.add(product)
        self._session.commit()

    def update_product_number(self, id, subtraction_number):
        product = self._session.get(Product, id)
        product.number -= subtraction_number
        product.number = product.number if product.number > 0 else 0
        self._session.commit()

    def delete_product(self, id):
        product = self._session.get(Product, id)
        self._session.delete(product)
        self._session.commit()

    def get_products_as_json(self, type=None):
        products = [p.as_dict() for p in
                    (filter(lambda p: p.type == type, self.get_products()) if type else self.get_products())]
        return {"products": products}

    def get_product_by_id(self, id):
        for p in self.get_products():
            if p.id == id:
                return p.as_dict()
        return None


class Product(declarative_base()):
    __tablename__ = 'products'
    id = db.Column(db.SmallInteger,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    rating = db.Column(db.SmallInteger)
    price = db.Column(db.Float)
    number = db.Column(db.SmallInteger)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
