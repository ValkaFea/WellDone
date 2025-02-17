import pytest
from well_app.crud import add_val, get_all_val, get_val_by_well, delete_well
from well_app.schemas import WellCreate
from sqlalchemy.exc import IntegrityError


def test_get_all_val(db_session):
    # Создаем несколько записей
    well_data1 = WellCreate(id_well=21, id_tag=21, tag_val="test1", date_time="2025-02-17T10:16:32.075000")
    well_data2 = WellCreate(id_well=22, id_tag=22, tag_val="test2", date_time="2025-02-17T10:17:32.075000")

    add_val(db_session, well_data1)
    add_val(db_session, well_data2)

    # Получаем все записи
    result = get_all_val(db_session)

    # Проверяем, что количество записей соответствует ожидаемому
    assert len(result) == 2

    # Проверяем, что данные первой записи совпадают
    assert result[0].id_well == 21
    assert result[0].id_tag == 21
    assert result[0].tag_val == "test1"
    assert str(result[0].date_time) == "2025-02-17 10:16:32.075000"

    # Проверяем, что данные второй записи совпадают
    assert result[1].id_well == 22
    assert result[1].id_tag == 22
    assert result[1].tag_val == "test2"
    assert str(result[1].date_time) == "2025-02-17 10:17:32.075000"

def test_add_val(db_session):

    well_data = WellCreate(id_well=11, id_tag=11, tag_val="test", date_time="2025-02-17T10:16:32.075000")

    result = add_val(db_session, well_data)
    assert result.id_well == 11
    assert result.id_tag == 11

    #создаем дубликат
    with pytest.raises(ValueError, match="Запись с такими id_well и id_tag уже существует"):
        add_val(db_session, well_data)


def test_get_val_by_well(db_session):

    well_data = WellCreate(id_well=3, id_tag=3, tag_val="test", date_time="2025-02-17T10:16:32.075000")
    add_val(db_session, well_data)

    result = get_val_by_well(db_session, 3)
    assert result[0].id_well == 3

def test_delete_well(db_session):

    well_data = WellCreate(id_well=12, id_tag=12, tag_val="test", date_time="2025-02-17T10:16:32.075000")
    added_well = add_val(db_session, well_data)

    result = delete_well(db_session, 12)
    assert result is True

    result = get_val_by_well(db_session, 12)
    assert result is None



