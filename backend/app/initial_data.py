import logging

from sqlmodel import Session

from app.core.db import engine, init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """Handled by the API router; see the OpenAPI schema for the response shape."""
    with Session(engine) as session:
        init_db(session)


def main() -> None:
    """Handled by the API router; see the OpenAPI schema for the response shape."""
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
