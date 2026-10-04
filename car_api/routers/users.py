from fastapi import APIRouter, status
from car_api.schemas.users import UserListPublicSchema


router = APIRouter()


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=UserListPublicSchema,
)
async def list_users():
    return {
        "users": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "John.Doe@example.com",
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "Jane.Smith@example.com",
            },
            {
                "id": 3,
                "name": "Alice Johnson",
                "email": "Alice.Johnson@example.com",
            },
        ]
    }