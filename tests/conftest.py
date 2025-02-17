import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from well_app.database import Base
from well_app.models import Well

#Временная БД для тестов

TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="module")
def db_session():

    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)