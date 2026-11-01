from booking_system import OnlineAppointmentBookingSystem
from datetime import datetime


def test_two_users_same_slot():
    system = OnlineAppointmentBookingSystem(
        users={"U1", "U2"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    assert system.book_app("U1", "D1", slot) == True
    assert system.book_app("U2", "D1", slot) == False


def test_cancel_nonexistent_appointment():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    assert system.cancel_app("U1", "D1", slot) == False


def test_past_time_slot():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2020, 1, 1, 10, 30)

    assert system.book_app("U1", "D1", slot) == False


def test_incomplete_details():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    assert system.book_app(None, "D1", slot) == False
    assert system.book_app("U1", None, slot) == False
    assert system.book_app("U1", "D1", None) == False


def test_slot_available_after_cancellation():
    system = OnlineAppointmentBookingSystem(
        users={"U1", "U2"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    system.book_app("U1", "D1", slot)
    system.cancel_app("U1", "D1", slot)

    assert system.book_app("U2", "D1", slot) == True