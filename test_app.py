from booking_system import OnlineAppointmentBookingSystem
from datetime import datetime


def test_book_appointment():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    assert system.book_app("U1", "D1", slot) == True


def test_already_booked_slot():
    system = OnlineAppointmentBookingSystem(
        users={"U1", "U2"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    system.book_app("U1", "D1", slot)

    assert system.book_app("U2", "D1", slot) == False


def test_cancel_appointment():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2026, 12, 5, 10, 30)

    system.book_app("U1", "D1", slot)

    assert system.cancel_app("U1", "D1", slot) == True


def test_past_date_appointment():
    system = OnlineAppointmentBookingSystem(
        users={"U1"},
        doctors={"D1"}
    )

    slot = datetime(2020, 1, 1, 10, 30)

    assert system.book_app("U1", "D1", slot) == False