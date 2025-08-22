from sqlalchemy import Column, Integer, String, Text

from fast_car_api.database import Base


class Car(Base):
    """Model representing a car in the database."""
    
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=True)
    model = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    model_year = Column(Integer, nullable=True)
    factory_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)

    def __repr__(self):
      return f"<Car(id={self.id}, make='{self.make}', model='{self.model}', year={self.year})>"