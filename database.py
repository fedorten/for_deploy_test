from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("postgresql://postgres:228666@localhost/post_punk")
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    password = Column(String(10))

    def __repr__(self):
        return f"User(name='{self.name}, age={self.age})"


Base.metadata.create_all(engine)
