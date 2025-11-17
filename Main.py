# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from person import Person

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    
    discharged_patients = []
    
    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    patients = Patient.read_patient_list('patients_file.txt')


    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- view / Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- View patient of  same family')
        print(' 5- Add/view symptoms')
        print(' 6- Admit New Patient')
        print(' 7- Assign doctor to a patient')
        print(' 8- Update admin detais')
        print(' 9- Appointments')
        print(' 10- Relocate Doctors')
        print(' 11- View Management Report')
        print(' 12- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
      
          admin.doctor_management(doctors)
           
          pass

        elif op == '2':
        
            admin.discharge(patients,discharged_patients)
           
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':

                    admin.discharge(patients,discharged_patients)

                elif op == 'no' or op == 'n':
                    break
                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            admin.view_discharge(discharged_patients)
            pass

        elif op == '4':
            admin.same_surname(patients)

        elif op == '5':
            admin.print_symptoms(patients)

        elif op == '6':
            admin.admit_patients(patients)
          
        elif op == '7':
             admin.assign_doctor_to_patient(patients, doctors)

        elif op =='8':
             admin.update_details()

        elif op == '9':
            admin.appointment(patients,doctors)

        elif op == '10':
            admin.relocate_patient(patients,doctors)

        elif op == '11':
            admin.view_management_report(doctors,patients)
           
        elif op == '12':
            print("you quitted")
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
 

