import pytest
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:sky123@localhost:5432/qa"
db = create_engine(DB_URL)


@pytest.fixture(scope="function")
def db_connection():
    connection = db.connect()
    transaction = connection.begin()
    # Очистка таблицы перед каждым тестом
    connection.execute(text("DELETE FROM student"))
    yield connection
    transaction.rollback()
    connection.close()


def test_create_student(db_connection):
    insert_sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        RETURNING *
    """)
    params = {
        "user_id": 123456,
        "level": "Intermediate",
        "education_form": "group",
        "subject_id": 2
    }

    result = db_connection.execute(insert_sql, params)
    inserted_row = result.mappings().first()

    assert inserted_row is not None
    assert inserted_row["user_id"] == 123456
    assert inserted_row["level"] == "Intermediate"

    select_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db_connection.execute(select_sql, {"user_id": 123456})
    rows = result.mappings().all()
    assert len(rows) == 1


def test_update_student(db_connection):
    insert_sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    db_connection.execute(insert_sql, {
        "user_id": 666999,
        "level": "Advanced",
        "education_form": "personal",
        "subject_id": 1
    })

    update_sql = text("""
        UPDATE student
        SET level = :new_level, education_form = :new_form
        WHERE user_id = :user_id
    """)
    db_connection.execute(update_sql, {
        "user_id": 666999,
        "new_level": "Beginner",
        "new_form": "group"
    })

    select_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db_connection.execute(select_sql, {"user_id": 666999})
    row = result.mappings().first()
    assert row["level"] == "Beginner"
    assert row["education_form"] == "group"


def test_delete_student(db_connection):
    insert_sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    db_connection.execute(insert_sql, {
        "user_id": 999666,
        "level": "Intermediate",
        "education_form": "personal",
        "subject_id": 1
    })
