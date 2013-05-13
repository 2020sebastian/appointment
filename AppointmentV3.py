class Appointment():
    appointments = {}
    def __init__(self, date, start_time, end_time, description):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        
    def __repr__(self):
        return ("Appointment({},{},{},{})".format(self.date, self.start_time, self.end_time, self.description))

    def __str__(self):
        return ("Date: {}, Start: {}, End: {}, Description: {}".format(self.date, self.start_time, self.end_time, self.description))        
        
    def addappt(self):
            Appointment.appointments[self.date, self.start_time] = "Date: {}, Start: {}, End: {}, Description: {}".format(self.date, self.start_time, self.end_time, self.description)
            print("Appointment created")


    def removeappt(date, start_time):
        if (date, start_time) in Appointment.appointments:
            del(Appointment.appointments[date, start_time])
            print("Appointment deleted")
        else:
            return("No such appointment")

    def displayappts(date):
        temp = [Appointment.appointments[item] for item in Appointment.appointments if date in item]
        if len(temp) == 0:
            print("No appointments")
        else:
            print("Appointments for",date+":")
            for item in temp:
                print(item)


def main():
    while True:
        choice = eval(input('Enter 1 to add an appointment, 2 to remove an appointment, \nor 3 to display your appointments:\n'))
        if choice == 1:
            date = input('Enter a date of the appointment in the form mm/dd:\n')
            start_time =  input('Enter the starting time of the appointment,\nin the form hh:mm plus AM or PM:\n')
            end_time =  input('Enter the ending time in the form hh:mm plus AM or PM:\n')
            description = input('Enter a description of the meeting:\n')
            appt = Appointment(date, start_time, end_time, description)
            Appointment.addappt(appt)
        elif choice == 2:
            date = input('Enter a date of the appointment in the form mm/dd:\n')
            start_time =  input('Enter the starting time of the appointment,\nin the form hh:mm plus AM or PM:\n')
            Appointment.removeappt(date, start_time)
        else:
            date = input('Enter a date of the appointment in the form mm/dd:\n')
            Appointment.displayappts(date)
        print()
    
main()
