from importlib.metadata import metadata
from select import select

from db import Base, db
from db.utils import CreatedModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String


# class Category(CreatedModel):
#     __tablename__ = 'categories'
#     name:Mapped[str] = mapped_column(String(255), nullable=False)
#
#     @classmethod
#     async def get_by_name(cls, name):
#         query = (select(cls)
#                  .where(cls.name.ilike(f'%{name}%'))
#                  )
#         objects = await db.execute(query)
#         objects = objects.scalars()
#         if objects:
#             return objects.first()
#         else:
#             return []

metadata = Base.metadata