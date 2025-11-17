from Doctor import Doctor
from Patient import Patient
import datetime



# doctors=[Doctor("Anish" ,"karki","neurology") ]

# patients =[Patient("john","joshi",20,"984500","44000","fever")]

# discharged_patients=[Patient('anish',"karki","40","99800000","9860")]

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
      

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1}|{item}')
           
        else: 
            if not a_list:
                print("No items to display")


    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if username == 'admin' and password =='123':
             
             print("-----Login-----")
             return True
        else:
            print("please try again")
            return False

    def find_index(self,index,doctors):
          
        index = int(index)        
        if index in range(0,len(doctors)):
            
            return True

        else:
            return False
    def get_register_doctor(first_name,surname,speciality,doctors):
        register = (first_name,surname,speciality)
        doctors.append(register)

    def view_doctor(doctors):
        return doctors
  
    # def get_doctor_details(self):
      
    #     pass
    
    
      

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register doctor')
        print(' 2 - View doctors')
        print(' 3 - Update doctor')
        print(' 4 - Delete doctor')
        op = input("Enter the operation:")
        #ToDo3
        


        # register
        if op == '1':
            print('Enter the doctor\'s details:')
            first_name = input("Enter the first name:")
            surname= input("Enter the surname:")
            speciality = input("Enter the speciality:")
           

            # check if the name is already registered
            name_exists = False
            for existing_doctor in doctors:
                if first_name == existing_doctor.get_first_name() and surname == existing_doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break
            if not name_exists:
                new_doctor = Doctor(first_name,surname,speciality)
                doctors.append(new_doctor)

            print("-----Register-----")
     
        if op == '2':
            print("-----List of Doctors-----")
           
            print("ID     ||   FULL NAME          ||   SPECIALITY")
            self.view(doctors)
           
            pass

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: '))-1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                            print('Choose the field to be updated:')
                            print(' 1 First name')
                            print(' 2 Surname')
                            print(' 3 Speciality')
                            op = int(input('Input: '))
                            if op == 1:
                                first_name =input("enter first name:")
                                Doctor.set_first_name(doctors[doctor_index-1],first_name)
                            elif op == 2:
                                surname = input("enter second name:")
                                Doctor.set_surname(doctors[doctor_index-1],surname)
                            elif op == 3:
                                speciality = input("enter speciality of doctor:")
                                Doctor.set_speciality(doctors[doctor_index-1],speciality)
                            else:
                                print("---invalid option---")

                
                            break
                        
                    else:
                        print("Doctor not found")

                except ValueError: 
                    print('The ID entered is incorrect')

            

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            index = int(input("Enter the ID of the doctor to delete: "))-1
            if self.find_index(index, doctors):
              del doctors[index]
              print("Doctor deleted")
            else:

      
        
                print('The id entered is incorrect')
        
    
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self,patients):
        print("---patients---")
        self.view(patients)-1

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
           
            patient_index = int(patient_index) -1

           
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return 

        except ValueError:
            print('The id entered is incorrect')
            return 
        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() 

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
          
            doctor_index = int(doctor_index) -1

            if self.find_index(doctor_index,doctors)!=False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now assign to the doctor.')
                 
            else:
                print('The id entered was not found.')

        except ValueError: 
            print('The id entered is incorrect')


    def discharge(self,patients, discharged_patient):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        
        print('ID|          Full Name          |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
      
        self.view(patients)
        print("-----Discharge Patient-----")

        op = input('Do you want to discharge a patient(Y/N):').lower()
        if op == 'yes' or op == 'y':
           
            dis_patient = int(input("enter a patients you want to discharge:"))-1
            removed_patient = patients.pop(dis_patient)
          
            discharged_patient.append(removed_patient)
            print("patient has been discharged")
        elif op =='no' or 'n':
            print("you exicted")
            
        else:
                    print("wrong entery")
      
        
                


     
        
    def view_discharge(self,discharged_patient):
   
        print("---discharged patients---")
        print('ID|          Full Name          |      Patients`s Full Name      | Age |    Mobile     | Postcode ')
       
        self.view(discharged_patient)
       
        pass
    def print_symptoms(self,patients):
        print("choose operation:")
        print(" 1. Add symptoms:")
        print(" 2. view symptoms:")
        op = input("Enter option:")
        self.view(patients)
        if op == '1':
            patient_no = (input("Enter a patient you want to add a symptoms:"))
            id = int(patient_no)-1
            if id not in range (len(patients)):
                print('The patient no was not found')
                return
            else:
                symptoms = input("Enter the symptoms that needs to be added for  : ")
                patients[id].set_symptoms(symptoms)
                print("Successfully Added!")
          
        elif op == '2':
            patient_no = (input("Enter the ID of patients:"))
            id = int(patient_no)-1
            if id not in range(len(patients)):
                print('The patient no was not found')
            else:
                patient = patients[id]
                print(f"Symptoms of {patient.full_name()}: {patient.print_symptoms()}")
              

    
    def same_surname(self,patients):
        patients = Patient.read_patient_list('patients_file.txt')
        same_family = {}
        for patient in patients:
            patient_surname = patient.get_surname()
            if patient_surname not in same_family:
                same_family[patient_surname] = [patient]
            else:
                same_family[patient_surname].append(patient)

        for surname, family_members in same_family.items():
            print(f"{surname} family:")
            for member in family_members:
                print(member)
            print()


    def write_patientRecords(self,patients):
        with open("patients_file.txt","w") as f:
            data = f.write(str(patients))
        print(data)
        
    

    def admit_patients(self, patients):
        print("Admit a patient")
        f_name = input("Enter First Name:")
        l_name = input("Enter Second Name:")
        age = input("Enter Age of Patient:")
        ph_no = input("Enter Mobile NUmmber:")
        post_Code = input("Enter postcode:")
        patients.append(Patient(f_name,l_name,age,ph_no,post_Code))
      
        Patient.save_patient_list('patients_file.txt',patients)
        print("New patients has been added.")
        


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input("Enter the new username:")
            self.__username = username
            print("username is updated")
            #ToDo14
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("password is updated")

        elif op == 3:
            address = input("Enter the new address:")
            self.__address = address
            print("Address is updated")
            #ToDo15
            pass

        else:
            print("Invalid choice")



    def relocate_patient(self, patients, doctors):
        print("-----Relocate Doctor-----")
        print("-----List of Patients-----")
        self.view(patients)

        if len(patients) != 0:
            try:
                patient_index = int(input('Enter the ID of the patient to relocate the doctor from: ')) - 1
                if 0 <= patient_index < len(patients):
                    print("-----List of Doctors-----")
                    self.view(doctors)
                    new_doctor = int(input('Enter the ID of the new doctor: ')) - 1

                    if 0 <= new_doctor < len(doctors):
                        previous_doctor = patients[patient_index].get_doctor()
                        full_name = patients[patient_index].full_name()
                        patients[patient_index].link(doctors[new_doctor].full_name())
                        doctors[new_doctor].add_patient(patients[patient_index])
                        print(f"Successfully relocated {full_name} to {doctors[new_doctor].full_name()}.")
                        self.write_patientRecords(patients)
                    else:
                        print('Invalid new doctor ID. Check your input.')
                else:
                    print('Invalid patient ID. Check your input.')
            except ValueError:
                print('Invalid input for patient or new doctor ID. Please enter a valid integer.')
        else:
            print('No patients available for relocation.')


    def appointment(self,patients,doctors):
        print("|--Choose the operation----|")
        print("|--1. Book your date: -----|")
        print("|--2. Check your status:---|")
        print("|--------------------------|")
        op = input("Enter your choice: ")

        try:
            if op == '1':
                #Appointment time
                month = int(input("Enter the month: "))
                day = int(input("Enter the date: "))
                timehour = int(input("Enter hour for appointment: "))
                minute = int(input("Enter minute: "))
                dt = datetime.datetime(2024,month, day, timehour, minute, 0)
           
                self.view(patients)
                p_index = int(input('Enter the ID of the patient: '))-1
                patient_index = self.find_index(p_index, patients)
                if not patient_index:
                    raise ValueError("404! -- Patient not found")
                else:
                    alive_pat = patients[p_index]
                    print("-----List of doctors-----")
                    print('ID |          Full name           |  Speciality')
                    self.view(doctors)
                    d_index = int(input('Enter the ID of the doctor: '))-1
                    doctor_index = self.find_index(d_index, doctors)
                    if not doctor_index:
                        raise ValueError("Doctor not found")
                    else:
                        alive_pat.add_appointment(dt)
                        alive_pat.set_status("Approved(Date found)!")
                        alive_doc = doctors[d_index]
                        alive_doc.set_appointments(dt)
                        print("Appointment Done!")
                        print(alive_pat.show_appointment())

            elif op == '2':
                self.view(patients)
                p_index = int(input('Enter the ID of the patient: '))-1
                patient_index = self.find_index(p_index, patients)
                if patient_index:
                    pat = patients[patient_index]
                    print(pat.get_status())
                else:
                    raise ValueError("404! -- Patient not found")

            else:
                raise ValueError("Invalid choice. Please try again.")

        except ValueError as e:
            print(str(e))
   


    def view_management_report(self,doctors, patients):
        print("---Hospital Overall Report---")

        total_doctors = len(doctors)
        print(f"The total number of doctors in the hospital is {total_doctors}")

        total_patients = len(patients)
        print(f"The total number of patients in the hospital is {total_patients}")

        for doctor in doctors:
            num_patients = sum(1 for patient in patients if patient.get_doctor() == doctor.full_name())
            print(f"The number of patients for {doctor.full_name()} is: {num_patients}")

        total_number_of_patients_based_on_illness = {}
        for patient in patients:
            patient_symptoms = patient.print_symptoms()
            for symptom in patient_symptoms:
                if symptom not in total_number_of_patients_based_on_illness:
                    total_number_of_patients_based_on_illness[symptom] = 1
                else:
                    total_number_of_patients_based_on_illness[symptom] += 1

        print("\nTotal number of patients based on the illness:")
        if not total_number_of_patients_based_on_illness:  
            print("None")
        else:
            for symptom, count in total_number_of_patients_based_on_illness.items():
                print(f"{symptom:<45}: {count:>3} patients")
        
        print("\nTotal number of appointments per month per doctor:")
        for doctor in doctors:
            appointments = doctor.get_appointment()
            print(f"{doctor.full_name()}:")
            if not appointments:
                print("   - None")
            else:
                for month, count in appointments.item():
                    print(f"   - {month}: {count} appointments")
