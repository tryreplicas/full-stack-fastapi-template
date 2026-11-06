from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, delete

from app.core.config import settings
from app.core.db import engine, init_db
from app.main import app
from app.models import Item, User
from tests.utils.user import authentication_token_from_email
from tests.utils.utils import get_admin_headers


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session]:
    with Session(engine) as session:
        init_db(session)
        yield session
        statement = delete(Item)
        session.execute(statement)
        statement = delete(User)
        session.execute(statement)
        session.commit()


@pytest.fixture(scope="module")
def api_client() -> Generator[TestClient]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def admin_headers(api_client: TestClient) -> dict[str, str]:
    return get_admin_headers(api_client)


@pytest.fixture(scope="module")
def normal_user_token_headers(api_client: TestClient, db: Session) -> dict[str, str]:
    return authentication_token_from_email(
        api_client=api_client, email=settings.EMAIL_TEST_USER, db=db
    )
