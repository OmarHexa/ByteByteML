from sqlalchemy import Column, Integer, String

from src.backend.database.mysql.config import Base


class ShowModel(Base):
    """This class represents the Object oriented mapping of the netflix table."""

    __tablename__ = "netflix"

    # id = Column(Integer, autoincrement=True)
    show_id = Column(String(200), primary_key=True, nullable=False, unique=True)
    type = Column(String(200), nullable=False)
    title = Column(String(200), nullable=False)
    director = Column(String(200), nullable=True)
    cast = Column(String(200), nullable=True)
    country = Column(String(200), nullable=True)
    date_added = Column(String(200), nullable=True)
    release_year = Column(Integer, nullable=True)
    rating = Column(String(200), nullable=True)
    duration = Column(String(200), nullable=True)
    listed_in = Column(String(200), nullable=True)
    description = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<ShowData(show_id={self.show_id}, title={self.title}, type={self.type}, director={self.director}, cast={self.cast}, country={self.country}, date_added={self.date_added}, release_year={self.release_year}, rating={self.rating}, duration={self.duration}, listed_in={self.listed_in}, description={self.description})>"
