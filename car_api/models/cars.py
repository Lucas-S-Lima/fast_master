from datetime import datetime
from typing import Optional, TYPE_CHECKING
from enum import Enum
from sqlalchemy import ForeignKey, String, Text, Numeric, Integer, Boolean, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from car_api.models import Base


if TYPE_CHECKING:
    from car_api.models.users import User


class TransmissionType(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    SEMI_AUTOMATIC = "semi-automatic"


class FuelType(str, Enum):
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"
    ETHANOL = "ethanol"


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(45), unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    revenue: Mapped[float] = mapped_column(Numeric(precision=12, scale=2), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), nullable=False)
    model: Mapped[str] = mapped_column(String(60), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String(30), nullable=False)
    plate: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=12, scale=2), nullable=False)
    transmission_type: Mapped[TransmissionType] = mapped_column(String(20), nullable=False)
    fuel_type: Mapped[FuelType] = mapped_column(String(20), nullable=False)
    mileage: Mapped[float] = mapped_column(Numeric(precision=12, scale=2), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True, default=None)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    brand: Mapped["Brand"] = relationship("Brand", backref="cars")
    user: Mapped["User"] = relationship("User", backref="cars")