import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "387468jhxhdsbssb3636"


def create_token(user_id: str):
    data = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
    }
    card = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return card


def check_token(card: str):
    try:
        data = jwt.decode(card, SECRET_KEY, algorithms=["HS256"])
        return data
    except:
        return "এই card ভুয়া বা মেয়াদ শেষ"


my_card = create_token("mahmud322")
print(my_card)
print(check_token(my_card))
