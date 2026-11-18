import database


def test_load_returns_empty_list_when_no_file(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "FILE_NAME", str(tmp_path / "bookings.json"))
    assert database.load_bookings() == []


def test_save_then_load_gives_same_list(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "FILE_NAME", str(tmp_path / "bookings.json"))
    database.save_bookings([9, 14, 15])
    assert database.load_bookings() == [9, 14, 15]
