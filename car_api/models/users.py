from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import func 
from car_api.models import Base


if TYPE_CHECKING:
    from car_api.models.cars import Car

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=False)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    cars: Mapped[List["Car"]] = relationship("Car", backref="owner")
