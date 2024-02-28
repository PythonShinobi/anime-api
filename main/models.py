
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float

from . import db

class Anime(db.Model):
    __tablename__ = 'anime_model'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Rank: Mapped[int] = mapped_column(Integer)
    Name: Mapped[str] = mapped_column(String(250), nullable=True)
    Japanese_name: Mapped[str] = mapped_column(String(250), nullable=True)
    Type: Mapped[str] = mapped_column(String(250), nullable=True)
    Episodes: Mapped[float] = mapped_column(Float, nullable=True)
    Studio: Mapped[str] = mapped_column(String(250), nullable=True)
    Release_season: Mapped[str] = mapped_column(String(250), nullable=True)
    Tags: Mapped[str] = mapped_column(String(250), nullable=True)
    Rating: Mapped[float] = mapped_column(Float, nullable=True)
    Release_year: Mapped[float] = mapped_column(Float, nullable=True)
    End_year: Mapped[float] = mapped_column(Float, nullable=True)
    Description: Mapped[str] = mapped_column(String(250), nullable=True)
    Content_warning: Mapped[str] = mapped_column(String(250), nullable=True)
    Related_mange: Mapped[str] = mapped_column(String(250), nullable=True)
    Related_anime: Mapped[str] = mapped_column(String(250), nullable=True)
    Voice_actors: Mapped[str] = mapped_column(String(250), nullable=True)
    Staff: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Create a dictionary where the keys are the names of the columns in the database table, and the values 
        # are the corresponding values of those columns in the specific row represented by self. 
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}