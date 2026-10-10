from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from car_api.core.settings import Settings 


engine = create_async_engine(Settings().DATABASE_URL, echo=True)


async def get_session() -> AsyncSession:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

    