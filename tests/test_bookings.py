from bookings import (
    book_slot,
    cancel_booking,
    find_next_slot,
    is_closed_day,
    shop_status,
)


def test_cancel_booking_removes_hour():
    booked = [9, 10, 11]
    assert cancel_booking(booked, 10) is True
    assert booked == [9, 11]


def test_cancel_booking_with_no_booking_returns_false():
    booked = [9, 10]
    assert cancel_booking(booked, 15) is False
    assert booked == [9, 10]


def test_book_slot_adds_free_hour():
    booked = [9, 10]
    assert book_slot(booked, 14) is True
    assert booked == [9, 10, 14]


def test_book_slot_refuses_taken_hour():
    booked = [9, 10]
    assert book_slot(booked, 10) is False
    assert booked == [9, 10]


def test_first_slot_when_nothing_booked():
    assert find_next_slot([]) == 9


def test_skips_booked_hours():
    assert find_next_slot([9, 10]) == 11


def test_skips_lunch():
    assert find_next_slot([9, 10, 11]) == 13


def test_full_day_returns_none():
    assert find_next_slot([9, 10, 11, 13, 14, 15, 16, 17]) is None


def test_after_hour_starts_search_later():
    assert find_next_slot([], after_hour=14) == 14


def test_sunday_is_closed():
    assert is_closed_day("Sunday")
    assert shop_status("sunday", 10) == "We are closed today"


def test_shop_status_through_the_day():
    assert shop_status("monday", 8) == "We are still closed right now!"
    assert shop_status("monday", 10) == "Shop is open"
    assert shop_status("monday", 12) == "Barber is on lunch, back at 1"
    assert shop_status("monday", 18) == "Shop is closed"
