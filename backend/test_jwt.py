from app.core.jwt_handler import create_access_token

token = create_access_token(
    {"sub":"subbu@gmail.com"}
)

print(token)