from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

# Импортировали необходимые опции
Base = declarative_base()


# Присвоили Ваse базовый класс


# Далее создаем и описываем классы, в которых создадим таблицы
class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


# id не входит, т.к. он создается автоматом через автоинремент


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(40))
    role = Column(String(20))
    manager_id = Column(Integer, ForeignKey("employee.id"))
    department_id = Column(Integer, ForeignKey("department.id"))
    manager = relationship("Employee")
    department = relationship("Department", back_populates="employees")

    # Взаимосвязь с классом Департамент и вывод всех сотрудников департамента

    def __init__(self, name, role, manager_id, department_id):
        self.name = name
        self.role = role
        self.manager_id = manager_id
        self.department_id = department_id

    # manager и department не входит, т.к. он создается автоматом через релейшеншип
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


Department.employees = relationship("Employee", back_populates="department")
# Взаимосвязь с классом Имплоии

connection_string = "sqlite:///C:/pythonProject/identifier.sqlite"
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# session = Session()


# it = Department('IT')
# hrs = Department('HRs')
# session.add_all([it, hrs])
#
# vasya = Employee('Vasya', 'tester', None, 1)
# katya = Employee('Katya', 'HR', 1, 2)
# volodya = Employee('Volodya', 'tester', 1, 1)
# session.add_all([vasya, katya, volodya])
# session.commit()
#
# stmt = select(Employee).where(Employee.name == "Vasya")
# my_Employee = session.scalar(stmt)
# print(my_Employee.manager)
#
#
# session.close()


def get_user(name):
    session = Session()
    stmt = select(Employee).where(Employee.name == name)
    my_Employee = session.scalar(stmt)
    session.close()
    return my_Employee


from sqlalchemy.orm import joinedload

def get_users():
    session = Session()
    stmt = session.query(Employee).options(joinedload(Employee.department))
    my_Employees = stmt.all()
    session.close()
    return my_Employees



def create_user(name, role, manager_id, department_id):
    session = Session()
    empl = Employee(
        name=name, role=role, manager_id=manager_id, department_id=department_id
    )
    session.add(empl)
    session.commit()
    session.close()
    return empl


def get_department(name):
    session = Session()
    stmp = select(Department).where(Department.name == name)
    my_Department = session.scalar(stmp)
    session.close()
    return my_Department


def get_departments():
    session = Session()
    stmt = session.query(Department).options(joinedload(Department.employees))
    my_Departments = stmt.all()
    session.close()
    return my_Departments


def create_department(name):
    session = Session()
    depart = Department(name)
    session.add(depart)
    session.commit()
    session.close()
    return depart
