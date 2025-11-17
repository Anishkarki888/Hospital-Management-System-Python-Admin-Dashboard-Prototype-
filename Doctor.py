from person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations."""

    def __init__(self, first_name: str, surname: str, speciality: str):
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.appointments = []

    def get_first_name(self) -> str:
        """Get the doctor's first name."""
        return super().get_first_name()
    
    def get_surname(self) -> str:
        """Get the doctor's surname."""
        return super().get_surname()
    
    def full_name(self) -> str:
        """Get the doctor's full name."""
        return super().full_name()

    def get_appointment(self) -> list:
        """Get the doctor's appointments."""
        return self.appointments
    
    def set_appointment(self, time: str):
        """Add a new appointment time."""
        self.appointments.append(time)

    def get_speciality(self) -> str:
        """Get the doctor's speciality."""
        return self.__speciality

    def set_speciality(self, new_speciality: str):
        """Set a new speciality for the doctor."""
        self.__speciality = new_speciality

    def add_patient(self, patient: str):
        """Add a new patient to the doctor's list."""
        self.__patients.append(patient)

    def write_patient_records(self):
        """Write the patient's records to a file."""
        with open("patients_file.txt", "a") as f:
            for patient in self.__patients:
                f.write(str(patient) + "\n")
        print("Patient records written to file.")
    
    def get_num_patients(self) -> int:
        """Get the number of patients assigned to the doctor."""
        return len(self.__patients)
