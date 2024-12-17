from sqlalchemy import Integer, String, Column, create_engine, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
import pymysql
pymysql.install_as_MySQLdb()


#create a database engine
db_url = "mysql://root:password@localhost/todo"
engine = create_engine(db_url)
# create a base class for the database columns
Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False)


# create the database tables
Base.metadata.create_all(engine)






