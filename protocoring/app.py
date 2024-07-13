import datetime
import uuid

import jwt

JWT_SECRET = None

USER_ID = None
ACCOUNT_ID = None
ACCOUNT_NAME = None
EXAM_ID = None
SESSION_ID = str(uuid.uuid4())

def get_user_data() -> dict:
    return {
        "userId": USER_ID,
        "lastName": "lastname",
        "firstName": "firstname",
        "thirdName": "thirdname",
        "language": "en",
    }


def get_organization_data() -> dict:
    return {
        "accountId": ACCOUNT_ID,
        "accountName": ACCOUNT_NAME,
    }


def get_exam_data() -> dict:
    start = datetime.datetime.now(tz=datetime.timezone.utc)
    end = start + datetime.timedelta(days=1)
    return {
        "duration": 30,
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "examId": EXAM_ID,
        "examName": "test simple integration",
        "proctoring": "offline",
        "schedule": False,
        "allowMultipleDisplays": True,
        "identification": "face_and_passport"
    }


def get_session_data() -> dict:
    return {
        "sessionId": SESSION_ID,
        "sessionUrl": "https://example.org/",
    }


def get_start_payload_data() -> dict:
    return {
        **get_user_data(),
        **get_organization_data(),
        **get_exam_data(),
        **get_session_data()
    }


def build_token(payload: dict, jwt_secret: str) -> str:
    return jwt.encode(payload=payload, key=jwt_secret, algorithm="HS256")


def main():
    assert JWT_SECRET is None
    assert USER_ID is None
    assert ACCOUNT_ID is None
    assert ACCOUNT_NAME is None
    assert EXAM_ID is None
    assert SESSION_ID is None


    token = build_token(payload=get_start_payload_data(), jwt_secret=JWT_SECRET)
    print(token)


if __name__ == '__main__':
    main()
