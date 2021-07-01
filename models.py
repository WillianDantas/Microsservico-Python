from sqlalchemy import  Column, String, Integer

from common import Base


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    email = Column(String)
    last_name = Column(String)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            elif key == "email":
                self.email = value
            elif key == "last_name":
                self.last_name = value
