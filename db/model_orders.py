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


def get_orders():
    session = Session()
    stmt = session.execute(select(Orders))
    my_orders = stmt.scalars().all()
    session.close()
    return my_orders
