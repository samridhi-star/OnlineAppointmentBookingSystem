from datetime import datetime
class OnlineAppointmentBookingSystem:

    def __init__(self,users,doctors):
        self.users=users
        self.doctors=doctors
        self.booked=set()

    def book_app(self,user_id,doctor_id,slot):
        booking=(user_id,doctor_id,slot)

        if user_id not in self.users:
            return False
    
        if doctor_id not in self.doctors:
            return False

        if not user_id or not doctor_id or slot is None:
            return False
        if slot <= datetime.now():
            return False
        for existing in self.booked:
            if existing[1] == doctor_id and existing[2] == slot:
                return False

        self.booked.add(booking)
        return True

    def cancel_app(self,user_id,doctor_id,slot):
        booking=(user_id,doctor_id,slot)
        if booking not in self.booked:
            return False
        self.booked.remove(booking)
        return True

    def view_app(self,user_id):
        appointments=[]
        for booking in self.booked:
            if booking[0]==user_id:
                appointments.append(booking)

        return appointments
