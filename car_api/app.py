from fastapi import FastAPI, status
from car_api.routers import users 


app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/health_check", status_code=status.HTTP_200_OK)   
async def health_check():
    return {"status": "OK"}


