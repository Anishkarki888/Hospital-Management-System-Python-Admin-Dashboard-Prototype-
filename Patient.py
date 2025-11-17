from person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, dr = 'none',status ='pending'):


        super().__init__(first_name,surname)
        self.age = age
        self.mobile = mobile
        self.postcode = postcode
        self.doctor = dr
        self.symptoms = []
        self.appointments = []
        self.status = status
        

    def show_doctor(self, dr, sy):
        self.doctor = dr
        self.symptoms = sy


    def get_doctor(self):
        return self.doctor
    

    def link(self, doctor):
        self.doctor = doctor
        # pass

    def print_symptoms(self):
        return self.symptoms
    
    def set_symptoms(self, symptoms):
        self.symptoms.append(symptoms)

    
    def add_appointment(self, time):
        self.appointments.append(time)
        self.set_status("Approved")


    def show_appointment(self):
        return self.appointments

    
    def get_status(self):
        if len(self.appointments) != 0:
            return ("Approved")
        else:
            return ("Pending")
        
    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status
    
    @staticmethod
    def save_patient_list(patient_list,patients):
        with open(patient_list,'a') as file:
            for patient in patients:
                file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.age},{patient.mobile},{patient.postcode}\n")

    
    
    # @staticmethod

    def read_patient_list(patient_list):
        patients = []
        try:
            with open(patient_list, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:  
                        patient = Patient(data[0], data[1], (data[2]), data[3], data[4])
                        patients.append(patient)
            return patients
        except FileNotFoundError:
            print("File not found.")
            return []
   
  

    def __str__(self):
        return f'{self.full_name():^30}|{self.doctor:^30}|{self.age:^5}|{self.mobile:^15}|{self.postcode:^10}'



