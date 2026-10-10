from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import func 
from car_api.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=False)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
