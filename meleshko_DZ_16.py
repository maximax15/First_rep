from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'{self.name}'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    orders = relationship('Orders', back_populates='client')


class Orders(Base):
    __tablename__ = "orders"

    def __init__(self, name, cost, client_id):
        self.name = name
        self.cost = cost
        self.client_id = client_id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'{self.name}'

    id = Column(Integer, autoincrement=True, primary_key=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Clients', back_populates='orders')


connection_string = "sqlite:///C:/pythonProject/identifier.sqlite"
engine = create_engine(connection_string)
connection = engine.connect()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# yura = Clients('Yura')
# pasha = Clients('Pasha')
# anton = Clients('Anton')
# sasha = Clients('Sasha')
# natasha = Clients('Natasha')
# dasha = Clients('Dasha')
# session.add_all([yura, pasha, anton, sasha, natasha, dasha])
# session.commit()
#
# orange = Orders('orange', 7, 1)main
# pencil = Orders('pencil', 1, 2)
# pen = Orders('pen', 2, 3)
# car = Orders('car', 50000, 4)
# sofa = Orders('sofa', 200, 5)
# chair = Orders('chair', 70, 6)
# paper = Orders('paper', 20, 1)
# table = Orders('table', 100, 2)
# laptop = Orders('laptop', 3000, 3)
# apple = Orders('apple', 6, 4)
# session.add_all([orange, pencil, pen, car, sofa, chair, paper, table, laptop, apple])
# session.commit()
##########ORM
# for client in session.query(Clients):
#     print(f'Клиент с именем: {client.name}')
#     for order in client.orders:
#         print(f'заказал: {order.name} {order.cost}')
# connection.close()


####### raw sql
# query = connection.execute(
#     text(
#         "select clients.name as client_name, orders.name as order_name, orders.cost from clients JOIN orders on clients.id = orders.client_id"
#     )
# )
# for row in query.mappings():
#     print(
#         f"клиент {row['client_name']}: {row['order_name']}, стоимость: {row['cost']}$"
#     )
# connection.close()
