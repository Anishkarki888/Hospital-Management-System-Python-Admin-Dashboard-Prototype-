from tkinter import ttk,messagebox,simpledialog
from  Main import Admin,Patient
from person import *
from Doctor import Doctor
from Patient import Patient
import tkinter as tk
from tkinter import font
import datetime
import time
import csv


def main():

    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]

def verify_login(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False

def entry():
    open_menu()   

def login():
    username = username_entry.get()
    password = password_entry.get()
    if verify_login(username, password):
        message_label.config(text="Login successful!")
        open_menu()
    else:
        message_label.config(text="Please try again")
global removed_patient


def open_menu(parent_window=None):
    if parent_window and parent_window.winfo_exists():
        parent_window.destroy()
   
    menu_page = tk.Tk()
    menu_page.title("menu_page")
    menu_page.geometry("1000x800")
    menu_page.configure(bg='#729DC8')

    large_font = font.Font(size=25)
    welcome_label = tk.Label(menu_page,text="Welcome to Hospital Management System",bg="#729DC8",fg="#333333",font=large_font)
    welcome_label.grid(row=0, column=0, pady=(20, 10))

    operation_buttons = [
        ("------Choose Operation------",None),
        ("Register/view/update/delete doctor",doctor_management),
        ("View / Discharge patients", open_patient_page),
        ("View Discharged patients", view_discharged_patient),
        ("View patient of same family", open_family_page),
        ("Add/view symptoms", open_symptoms_page),
        ("Admit New Patient", open_admit_page),
        ("Assign doctor to a patient", open_assign_doctor_page),
        ("Appointments", lambda event=None: HospitalManagementApp(menu_page).run()),
        ("Relocate Doctors", open_relocate_Patient_page),
        ("View Management Report", open_management_report_page),
        ("Quit", lambda:menu_page.destroy())
    ]
    for i, (operation_text, operation_func) in enumerate(operation_buttons):
        button = ttk.Button(menu_page, text=operation_text, command=lambda func=operation_func: func(menu_page), width=50)
        button.grid(row=i+2, column=0, pady=10)
 


    menu_page.grid_columnconfigure(0, weight=1)  

 
    menu_page.update_idletasks()
    menu_page_width = menu_page.winfo_width()
    menu_page_height = menu_page.winfo_height()
    screen_width = menu_page.winfo_screenwidth()
    screen_height = menu_page.winfo_screenheight()
    x = (screen_width // 2) - (menu_page_width // 2)
    y = (screen_height // 2) - (menu_page_height // 2)
    menu_page.geometry(f"+{x}+{y}")

    menu_page.mainloop()



def doctor_management(parent_window):
    parent_window.destroy()
    doctor_page = tk.Tk()
    doctor_page.title("doctor_page")
    doctor_page.geometry("1000x800")
    doctor_page.configure(bg='#729DC8')

    large_font = font.Font(size=25)
    welcome_label = tk.Label(doctor_page,text="-----Doctor Management-----",bg="#729DC8",fg="#333333",font=large_font)
    welcome_label.grid(row=0, column=0, pady=(40, 50))

    operation_buttons = [
        ("------Choose Operation------",None),
        ("Register Doctor",register_doctor),
        ("View Doctor",view_doctor),
        ("Update Doctor",update_doctor),
        ("Delete Doctor",delete_doctor),
       
    ]
    for i, (operation_text, operation_func) in enumerate(operation_buttons):
        button = ttk.Button(doctor_page, text=operation_text, command=lambda func=operation_func: func(doctor_page), width=50)
        button.grid(row=i+2, column=0, pady=10)
    
    back_button = tk.Button(doctor_page, text="Back to Menu Page", command=lambda: open_menu(doctor_page))
   
    back_button.place(relx=0.50, rely=0.48, anchor="center")
 

    doctor_page.grid_columnconfigure(0,weight=1)


    doctor_page.update_idletasks()
    doctor_page_width = doctor_page.winfo_width()
    doctor_page_height = doctor_page.winfo_height()
    screen_width = doctor_page.winfo_screenwidth()
    screen_height = doctor_page.winfo_screenheight()
    x = (screen_width // 2) - (  doctor_page_width// 2)
    y = (screen_height // 2) - ( doctor_page_height // 2)
    doctor_page.geometry(f"+{x}+{y}")

    doctor_page.mainloop()

doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
def register_doctor(parent_window):
    parent_window.destroy()

    register_window = tk.Tk()
    register_window.title("Register Doctor")
    register_window.geometry("1000x700")
    register_window.configure(bg='#729DC8')

   
    tk.Label(register_window, text="First Name:", bg="#729DC8").place(relx=0.45, rely=0.25, anchor="center")
    first_name_entry = tk.Entry(register_window)
    first_name_entry.place(relx=0.56, rely=0.25, anchor="center")


   
    tk.Label(register_window, text="Surname:", bg="#729DC8").place(relx=0.45, rely=0.3, anchor="center")
    surname_entry = tk.Entry(register_window)
    surname_entry.place(relx=0.56, rely=0.3, anchor="center")

   
    tk.Label(register_window, text="Speciality:", bg="#729DC8").place(relx=0.45, rely=0.35, anchor="center")
    speciality_entry = tk.Entry(register_window)
    speciality_entry.place(relx=0.56, rely=0.35, anchor="center")
    
    enter_button = tk.Button(register_window,text="submit",command=any)
    enter_button.place(relx=0.56, rely=0.4, anchor="center")

    def register():
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        speciality = speciality_entry.get()

        name_exists = False
        for existing_doctor in doctors:
            if first_name == existing_doctor.get_first_name() and surname == existing_doctor.get_surname():
                name_exists = True
                break
        if not name_exists:

                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
    
                
              
                first_name_entry.delete(0, tk.END)
                surname_entry.delete(0, tk.END)
                speciality_entry.delete(0, tk.END)
    
                
                tk.Label(register_window, text="Doctor registered successfully!", bg="#729DC8").place(relx=0.5, rely=0.45, anchor="center")
                back_button = tk.Button(register_window, text="Back to Doctor Management", command=lambda: doctor_management(register_window))
                back_button.place(relx=0.5, rely=0.5, anchor="center")

        else:
                tk.Label(register_window, text="Doctor already registered.", bg="#729DC8").place(relx=0.5, rely=0.45, anchor="center")
    
          
    
    enter_button = tk.Button(register_window, text="Submit", command=register)
    enter_button.place(relx=0.56, rely=0.4, anchor="center")

    register_window.mainloop()
    
        
def view_doctor(parent_window):
    parent_window.destroy()

    view_window = tk.Tk()
    view_window.title("View Doctors")
    view_window.geometry("1000x700")
    view_window.configure(bg='#729DC8')

    large_font = font.Font(size=15)

    view_window.grid_columnconfigure(0, weight=1)
    view_window.grid_columnconfigure(1, weight=1)
    view_window.grid_columnconfigure(2, weight=1)

    
    tk.Label(view_window, text="ID", bg="#729DC8", font=large_font).grid(row=0, column=0, pady=10, sticky='nsew')
    tk.Label(view_window, text="Full Name", bg="#729DC8", font=large_font).grid(row=0, column=1, pady=10, sticky='nsew')
    tk.Label(view_window, text="Speciality", bg="#729DC8", font=large_font).grid(row=0, column=2, pady=10, sticky='nsew')

    for i, doctor in enumerate(doctors):
        tk.Label(view_window, text=str(i+1), bg="#729DC8").grid(row=i+1, column=0, pady=5, sticky='nsew')
        tk.Label(view_window, text=doctor.first_name + " "+ doctor.surname , bg="#729DC8").grid(row=i+1, column=1, pady=5, sticky='nsew')
        tk.Label(view_window, text=doctor.speciality, bg="#729DC8").grid(row=i+1, column=2, pady=5, sticky='nsew')

    
    back_button = tk.Button(view_window, text="Back to Doctor Management", command=lambda: doctor_management(view_window))
    back_button.grid(row=len(doctors)+1, column=1, pady=20, sticky='nsew')

    view_window.mainloop()





class Doctor:
    def __init__(self, first_name, surname, speciality):
        self.first_name = first_name
        self.surname = surname
        self.speciality = speciality


doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone', 'Carlos', 'Cardiology')]



def open_update_doctor(parent_window, doctor_id_entry, field_var, new_value_entry):
    # parent_window.destroy()

    update_window = tk.Tk()
    update_window.title("Update Doctor")
    update_window.geometry("1000x700")
    update_window.configure(bg='#729DC8')

    large_font = font.Font(size=25)
    welcome_label = tk.Label(update_window, text="Doctor is updated", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, pady=(20, 10))

    back_button = tk.Button(update_window, text="Back to Main Menu", command=lambda: open_menu(update_window))
    back_button.grid(row=1, column=0, pady=(20, 10))

    doctor_id = doctor_id_entry.get().strip()  
    field = field_var.get()
    new_value = new_value_entry.get()

    try:
        selected_id = int(doctor_id)
    except ValueError:
        error_label = tk.Label(update_window, text="Invalid ID. Please enter a numeric ID.", bg="#729DC8")
        error_label.grid(row=1, column=0, pady=(20, 10))
        update_button = tk.Button(update_window, text="Close", command=update_window.destroy)
        update_button.grid(row=2, column=0, pady=(20, 10))
        back_button = tk.Button(update_window, text="Back to Doctor Management", command=lambda: open_menu(update_window))
        back_button.grid(row=3, column=0, pady=(20, 10))
        update_window.mainloop()
        return

    if 1 <= selected_id <= len(doctors):
        doctor = doctors[selected_id - 1] 

        if field == "First Name":
            doctor.first_name = new_value
        elif field == "Surname":
            doctor.surname = new_value
        elif field == "Speciality":
            doctor.speciality = new_value
        else:
            error_label = tk.Label(update_window, text="Invalid field selection", bg="#729DC8")
            error_label.grid(row=1, column=0, pady=(20, 10))
            update_button = tk.Button(update_window, text="Close", command=update_window.destroy)
            update_button.grid(row=2, column=0, pady=(20, 10))
            back_button = tk.Button(update_window, text="Back to Doctor Management", command=lambda: open_menu(update_window))
            back_button.grid(row=3, column=0, pady=(20, 10))
            update_window.mainloop()
            return

        success_label = tk.Label(update_window, text="Doctor details updated successfully!", bg="#729DC8")
        success_label.grid(row=1, column=0, pady=(20, 10))
    else:
        error_label = tk.Label(update_window, text="Doctor not found. Please enter a valid ID.", bg="#729DC8")
        error_label.grid(row=1, column=0, pady=(20, 10))
        update_button = tk.Button(update_window, text="Close", command=update_window.destroy)
        update_button.grid(row=2, column=0, pady=(20, 10))
        back_button = tk.Button(update_window, text="Back to Doctor Management", command=lambda: open_menu(update_window))
        back_button.grid(row=3, column=0, pady=(20, 10))
        update_window.mainloop()
        return

    update_button = tk.Button(update_window, text="Close", command=update_window.destroy)
    update_button.grid(row=2, column=0, pady=(20, 10))

    back_button = tk.Button(update_window, text="Back to Doctor Management", command=lambda: open_menu(update_window))
    back_button.grid(row=3, column=0, pady=(20, 10))

    update_window.mainloop()


def update_doctor(parent_window):
    parent_window.destroy()
    update_doctor_window = tk.Tk()
    update_doctor_window.title("Update Doctor")
    update_doctor_window.geometry("1000x700")
    update_doctor_window.configure(bg='#729DC8')

   
    doctor_id_label = tk.Label(update_doctor_window, text="Doctor ID:")
    doctor_id_label.pack(pady=10)
    doctor_id_entry = tk.Entry(update_doctor_window)
    doctor_id_entry.pack()

    field_label = tk.Label(update_doctor_window, text="Choose field to update:")
    field_label.pack(pady=10)
    field_var = tk.StringVar(update_doctor_window)
    field_var.set("First Name") 
    field_option_menu = tk.OptionMenu(update_doctor_window, field_var, "First Name", "Surname", "Speciality")
    field_option_menu.pack()

    new_value_label = tk.Label(update_doctor_window, text="New value:")
    new_value_label.pack(pady=10)
    new_value_entry = tk.Entry(update_doctor_window)
    new_value_entry.pack()

    update_button = tk.Button(update_doctor_window, text="Update", command=lambda: open_update_doctor(update_doctor_window, doctor_id_entry, field_var, new_value_entry))
    update_button.pack(pady=20)

    back_button = tk.Button(update_doctor_window, text="Back to Doctor Management", command=update_doctor_window.destroy)
    back_button.pack(pady=30)

    update_doctor_window.mainloop()



def delete_doctor(parent_window):
        parent_window.destroy()
        delete_window = tk.Tk()
        delete_window.title("Delete Doctor")
        delete_window.geometry("1000x700")
        delete_window.configure(bg='#729DC8')

        tk.Label(delete_window, text="Enter the ID of the doctor to delete:", bg="#729DC8").pack()

        doctor_id_entry = tk.Entry(delete_window)
        doctor_id_entry.pack()

        delete_button = tk.Button(delete_window, text="Delete", command=lambda:perform_deletion(doctor_id_entry,delete_window))
        delete_button.pack()

        back_button = tk.Button(delete_window, text="Back to Doctor Management", command=lambda: doctor_management(delete_window))
        
        back_button.pack(pady=20)

        delete_window.mainloop()

def perform_deletion(doctor_id_entry,delete_window):
        selected_id = int(doctor_id_entry.get())
        if selected_id > 0 and selected_id <= len(doctors):
            del doctors[selected_id - 1]
            for widget in delete_window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text") == "Doctor deleted":
                    widget.destroy()
            message_label = tk.Label(delete_window, text="Doctor deleted", bg="#729DC8")
            message_label.pack()
            print("Doctor deleted")
        else:
            print("Invalid ID. Please enter a valid ID.")


def open_patient_page(parent_window):
    parent_window.destroy()
    global  entry
    patient_list_window = tk.Toplevel()
    patient_list_window.title("Patient List")
    patient_list_window.geometry("1000x700")
    patient_list_window.configure(bg='#729DC8')

    with open("patients_file.txt", "r") as file:
        patient_list = file.readlines()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(patient_list_window, text="-----Patient List-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    headers = ["ID", "First Name", "Last Name", "Age", "Mobile", "Postcode","Symptoms"]
    for col, header in enumerate(headers):
        tk.Label(patient_list_window, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    for i, patient_info in enumerate(patient_list, start=1):
        patient_info = patient_info.strip().split(",")
        while len(patient_info) < 7:
            patient_info.append("None")

        tk.Label(patient_list_window, text=str(i), bg="#729DC8", fg="#333333").grid(row=i + 1, column=0, pady=5, padx=10, sticky='nsew')
        for col, info in enumerate(patient_info, start=1):
            tk.Label(patient_list_window, text=info, bg="#729DC8", fg="#333333").grid(row=i + 1, column=col, pady=5, padx=10, sticky='nsew')

    for col in range(8):
        patient_list_window.grid_columnconfigure(col, weight=1)

    option_label = tk.Label(patient_list_window, text="-----Do you want to discharge a patient-----", bg="#729DC8", fg="#333333", font=large_font)
    option_label.grid(row=i + 2, column=0, columnspan=7, pady=(20, 10))

    discharge_button = tk.Button(patient_list_window, text="Discharge Patient", command=lambda: discharge_patient(patient_list_window))
    discharge_button.grid(row=i + 3, column=0, columnspan=8, pady=(20, 10))

    return_button = tk.Button(patient_list_window, text="Back to home page", command=lambda: open_menu())
    return_button.grid(row=i + 4, column=0, columnspan=8, pady=(20, 10))

def discharge_patient(parent_window):
        parent_window.destroy()
        dis_patient = tk.Tk()
        dis_patient.title("Discharge Patient")
        dis_patient.geometry("1000x700")
        dis_patient.configure(bg='#729DC8')

        tk.Label(dis_patient, text="Enter the ID of the Patient you want to discharge:", bg="#729DC8").pack()

        patient_id_entry = tk.Entry(dis_patient)
        patient_id_entry.pack()

        discharge_button = tk.Button(dis_patient, text="Discharge", command=lambda:perform_discharge(patient_id_entry,dis_patient))
        discharge_button.pack()

        back_button = tk.Button(dis_patient, text="Back to Patient Page", command=lambda: open_patient_page(dis_patient))   
        back_button.pack(pady=20)

        

        dis_patient.mainloop()

def perform_discharge(patient_id_entry,dis_patient):
    
        selected_id = int(patient_id_entry.get())
        with open("patients_file.txt", "r") as file:
            patient_list = file.readlines()

        if selected_id > 0 and selected_id <= len(patient_list):
            removed_patient = patient_list[selected_id - 1]
            with open("discharged_patients_file.txt", "a") as file:
                file.write(removed_patient + "\n")
            del patient_list[selected_id - 1]
            with open("patients_file.txt", "w") as file:
                file.writelines(patient_list)

            for widget in dis_patient.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text") == "Patient Discharged":
                    widget.destroy()

            message_label = tk.Label(dis_patient, text="Patient Discharged", bg="#729DC8")
            message_label.pack()
            print("Patient Discharged")
        else:
            print("Invalid ID. Please enter a valid ID.")
            error_label = tk.Label(dis_patient, text="Invalid ID. Please enter a valid ID.", bg="#729DC8")
            error_label.pack()
    

def view_discharged_patient(parent_window):
    parent_window.destroy()

    view_patient = tk.Toplevel()
    view_patient.title("View Discharged Patient")
    view_patient.geometry("1000x700")
    view_patient.configure(bg='#729DC8')

    with open("discharged_patients_file.txt", "r") as file:
            discharged_patients = file.readlines()
    

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(view_patient, text="-----Discharged Patient List-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    headers = ["ID", "First Name", "Last Name", "Age", "Mobile", "Postcode","Symptoms"]
   
    for i, patient_info in enumerate(discharged_patients, start=1):
            patient_info = patient_info.strip().split(",")
            while len(patient_info) < 6:
                patient_info.append("None")

            tk.Label(view_patient, text=str(i), bg="#729DC8", fg="#333333").grid(row=i + 1, column=0, pady=5, padx=10, sticky='nsew')  
            for col, info in enumerate(patient_info,start=1):
                tk.Label(view_patient, text=info, bg="#729DC8", fg="#333333").grid(row=i + 1, column=col, pady=5, padx=10, sticky='nsew')

    for col, header in enumerate(headers):
        tk.Label(view_patient, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    for col in range(7):
        view_patient.grid_columnconfigure(col, weight=1)

    return_button = tk.Button(view_patient, text="Back to home page", command=open_menu)
    return_button.place(relx=0.5, rely=0.7, anchor="center")


#
class Patient:
    def __init__(self, first_name, last_name, age, mobile, postcode, dr = 'none',status ='pending'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = mobile
        self.postcode = postcode
        self.doctor = dr
        self.symptoms = []
        self.appointments = []
        self.status = "Pending"

    def add_appointment(self, appointment_time):
        self.appointments.append(appointment_time)

    def set_status(self, status):
        self.status = status 

    def get_status(self):
        return self.status
    
    def get_first_name(self):
        return self.first_name

    def get_surname(self):
        return self.last_name

    def full_name(self) :
        return f"{self.first_name}{self.last_name}"  
          
  
    def print_symptoms(self):
        return ', '.join(self.symptoms)

    @staticmethod
    def save_patient_list(patient_list, patients):
        with open(patient_list, 'w') as file:
            for patient in patients:
                symptoms = ';'.join(patient.symptoms)
                file.write(f"{patient.first_name},{patient.last_name},{patient.age},{patient.mobile},{symptoms},{patient.postcode}\n")


    @staticmethod
    def read_patient_list(patient_list):
        patients = []
        try:
            with open(patient_list, 'r+') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) != 6:
                        print(f"Skipping invalid line: {line.strip()}")
                        continue
                    first_name, surname, age, mobile, symptoms, postcode = [part.strip() for part in parts]
                    symptoms_list = symptoms.split(';') if symptoms else []
                    patient = Patient(first_name, surname, age, mobile, postcode)
                    patient.symptoms = symptoms_list
                    patients.append(patient)
        except FileNotFoundError:
            print(f"The file {patient_list} does not exist. Starting with an empty list.")
        return patients
    

from collections import defaultdict


def same_surname(patients):
    same_family = defaultdict(list)
    for patient in patients:
            patient_surname = patient.get_surname()
            if patient_surname not in same_family:
                same_family[patient_surname] = [patient]
            else:
                same_family[patient_surname].append(patient)
    return same_family
        #     for patient in patients:
#         try:
#             if patient.surname:
#                 same_family[patient.last].append(patient)
#             else:
#                 print(f"Warning: Patient object missing 'surname' attribute: {patient}")
#         except AttributeError:
#             print(f"Warning: Patient object missing 'surname' attribute: {patient}")
#     return same_family


def open_family_page(parent_window):
    parent_window.destroy()
    patient_list_window = tk.Toplevel()
    patient_list_window.title("Patient List")
    patient_list_window.geometry("1000x700")
    patient_list_window.configure(bg='#729DC8')

    patients = Patient.read_patient_list('patients_file.txt')
    same_family = same_surname(patients)

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(patient_list_window, text="-----Patient List-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=6, pady=(40, 20))

    headers = ["First Name", "Surname", "Age", "Mobile","Symptoms","Postcode",]
    for col, header in enumerate(headers):
        tk.Label(patient_list_window, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    row = 2
    for surname, family_members in same_family.items():
        tk.Label(patient_list_window, text=f"{surname} Family:", bg="#729DC8", fg="#333333", font=header_font).grid(row=row, column=0, pady=10, padx=10, sticky='nsew', columnspan=6)
        row += 1
        for member in family_members:
            tk.Label(patient_list_window, text=member._first_name, bg="#729DC8", fg="#333333").grid(row=row, column=0, pady=5, padx=10, sticky='nsew')
            tk.Label(patient_list_window, text=member._surname, bg="#729DC8", fg="#333333").grid(row=row, column=1, pady=5, padx=10, sticky='nsew')
            tk.Label(patient_list_window, text=member.age, bg="#729DC8", fg="#333333").grid(row=row, column=2, pady=5, padx=10, sticky='nsew')
            tk.Label(patient_list_window, text=member.mobile, bg="#729DC8", fg="#333333").grid(row=row, column=3, pady=5, padx=10, sticky='nsew')
            tk.Label(patient_list_window, text=member.print_symptoms(), bg="#729DC8", fg="#333333").grid(row=row, column=4, pady=5, padx=10, sticky='nsew')
            tk.Label(patient_list_window, text=member.postcode, bg="#729DC8", fg="#333333").grid(row=row, column=5, pady=5, padx=10, sticky='nsew')
            row += 1

    return_button = tk.Button(patient_list_window, text="Back to home page", command=lambda: open_menu(patient_list_window))
    return_button.place(relx=0.5, rely=0.9, anchor="center")

def open_symptoms_page(parent_window):
   
    parent_window.destroy()
    symptoms_window = tk.Toplevel()
    symptoms_window.title("Manage Symptoms")
    symptoms_window.geometry("1000x700")
    symptoms_window.configure(bg='#729DC8')

    patients = Patient.read_patient_list("patients_file.txt")

    def add_symptoms():
        patient_id = int(patient_id_entry.get()) - 1
        if patient_id not in range(len(patients)):
            tk.Label(symptoms_window, text="Invalid patient ID.", bg="#729DC8", fg="red").pack()
        else:
            symptoms = symptoms_entry.get()
            patients[patient_id].set_symptoms(symptoms)
            Patient.save_patient_list('patients_file.txt', patients)
            tk.Label(symptoms_window, text="Symptoms successfully added!", bg="#729DC8", fg="green").pack()

    def view_symptoms():
        patient_id = int(patient_id_entry.get()) - 1
        if patient_id not in range(len(patients)):
            tk.Label(symptoms_window, text="Invalid patient ID.", bg="#729DC8", fg="red").pack()
        else:
            patient = patients[patient_id]
            tk.Label(symptoms_window, text=f"Symptoms of {patient.full_name()}: {patient.print_symptoms()}", bg="#729DC8", fg="#333333").pack()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(symptoms_window, text="-----Manage Symptoms-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.pack(pady=(40, 20))

    tk.Label(symptoms_window, text="Enter Patient ID:", bg="#729DC8", fg="#333333").pack(pady=10)
    patient_id_entry = tk.Entry(symptoms_window)
    patient_id_entry.pack()

    tk.Label(symptoms_window, text="Enter Symptoms to Add:", bg="#729DC8", fg="#333333").pack(pady=10)
    symptoms_entry = tk.Entry(symptoms_window)
    symptoms_entry.pack()

    add_button = tk.Button(symptoms_window, text="Add Symptoms", command=add_symptoms)
    add_button.pack(pady=10)

    view_button = tk.Button(symptoms_window, text="View Symptoms", command=view_symptoms)
    view_button.pack(pady=10)

    back_button = tk.Button(symptoms_window, text="Back to Patient Page", command=lambda: open_patient_page(symptoms_window))
    back_button.pack(pady=20)

    symptoms_window.mainloop()



def open_admit_page(parent_window):
   
    parent_window.destroy()

    add_patient = tk.Tk()
    add_patient.title("Register Doctor")
    add_patient.geometry("1000x700")
    add_patient.configure(bg='#729DC8')

   
    tk.Label(add_patient, text="First Name:", bg="#729DC8").place(relx=0.45, rely=0.25, anchor="center")
    first_name_entry = tk.Entry(add_patient)
    first_name_entry.place(relx=0.56, rely=0.25, anchor="center")


   
    tk.Label(add_patient, text="Surname:", bg="#729DC8").place(relx=0.45, rely=0.3, anchor="center")
    surname_entry = tk.Entry(add_patient)
    surname_entry.place(relx=0.56, rely=0.3, anchor="center")

   
    tk.Label(add_patient, text="Age:", bg="#729DC8").place(relx=0.45, rely=0.35, anchor="center")
    age_entry = tk.Entry(add_patient)
    age_entry.place(relx=0.56, rely=0.35, anchor="center")

    tk.Label(add_patient, text="phone number:", bg="#729DC8").place(relx=0.45, rely=0.4, anchor="center")
    mobile_entry = tk.Entry(add_patient)
    mobile_entry.place(relx=0.56, rely=0.4, anchor="center")

    tk.Label(add_patient, text="Symptoms:", bg="#729DC8").place(relx=0.45, rely=0.45, anchor="center")
    symptoms_entry = tk.Entry(add_patient)
    symptoms_entry.place(relx=0.56, rely=0.45, anchor="center")

    tk.Label(add_patient, text="Postcode:", bg="#729DC8").place(relx=0.45, rely=0.5, anchor="center")
    postcode_entry = tk.Entry(add_patient)
    postcode_entry.place(relx=0.56, rely=0.5, anchor="center")
    
    enter_button = tk.Button(add_patient,text="submit",command=any)
    enter_button.place(relx=0.56, rely=0.55, anchor="center")

    
    def add():
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        age = age_entry.get()
        mobile = mobile_entry.get()
       
        postcode = postcode_entry.get()
        new_patient = Patient(first_name, surname, age, mobile, postcode)
       
        with open('patients_file.txt', 'a') as file:
             file.write(f"{new_patient.first_name},{new_patient.surname},{new_patient.age},{new_patient.mobile},{new_patient.postcode}\n")


        patients = Patient.read_patient_list('patients_file.txt')
        patients.append(new_patient)
        Patient.save_patient_list('patients_file.txt', patients)

        success_label = tk.Label(add_patient, text="Patient Added successfully!", bg="#729DC8").place(relx=0.5, rely=0.6, anchor="center")
        success_label.place(relx=0.5, rely=0.6, anchor="center")    
    

    back_button = tk.Button(add_patient, text="Back to Menu Page", command=lambda: open_menu(add_patient))
    back_button.place(relx=0.5, rely=0.7, anchor="center")

    enter_button = tk.Button(add_patient, text="Submit", command=add)
    enter_button.place(relx=0.56, rely=0.55, anchor="center")

    add_patient.mainloop() 
   

def open_admin_details_page(parent_window):
    parent_window.destroy()

    update_admin = tk.Tk()
    update_admin.title("Register Doctor")
    update_admin.geometry("1000x700")
    update_admin.configure(bg='#729DC8')
    
    ttk.Label(update_admin, text="Choose the field to be updated:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Button(update_admin, text="Update Username", command=update_admin.update_username).grid(row=1, column=0, pady=5)
    ttk.Button(update_admin, text="Update Password", command=update_admin.update_password).grid(row=2, column=0, pady=5)
    ttk.Button(update_admin, text="Update Address", command=update_admin.update_address).grid(row=3, column=0, pady=5)

def update_username(self):
        new_username = tk.simpledialog.askstring("Update Username", "Enter the new username:")
        if new_username:
            message = self.admin.update_username(new_username)
            messagebox.showinfo("Success", message)

def update_password(self):
        new_password = tk.simpledialog.askstring("Update Password", "Enter the new password:")
        if new_password:
            confirm_password = tk.simpledialog.askstring("Confirm Password", "Enter the new password again:")
            if confirm_password == new_password:
                message = self.admin.update_password(new_password)
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", "Passwords do not match.")

def update_address(self):
        new_address = tk.simpledialog.askstring("Update Address", "Enter the new address:")
        if new_address:
            message = self.admin.update_address(new_address)
            messagebox.showinfo("Success", message)

        
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "123"
        self.address = "N/A"

    def update_username(self, new_username):
        self.username = new_username
        return "Username updated successfully."

    def update_password(self, new_password):
        self.password = new_password
        return "Password updated successfully."

    def update_address(self, new_address):
        self.address = new_address
        return "Address updated successfully."

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        self.admin = Admin()
        
        ttk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = ttk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(root, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.message_label = ttk.Label(root, text="")
        self.message_label.grid(row=2, column=0, columnspan=2, pady=5)
        
        ttk.Button(root, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)
    
    def verify_login(self, username, password):
        return username == self.admin.username and password == self.admin.password

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.verify_login(username, password):
            self.message_label.config(text="Login successful!")
            self.open_menu()
        else:
            self.message_label.config(text="Please try again")
    

    
    def open_admin_details_page(self, parent_window):
        parent_window.destroy()
        
        update_admin = tk.Tk()
        update_admin.title("Update Admin Details")
        update_admin.geometry("1000x700")
        update_admin.configure(bg='#729DC8')
        
        ttk.Label(update_admin, text="Choose the field to be updated:").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(update_admin, text="Update Username", command=lambda: self.update_username(update_admin)).grid(row=1, column=0, pady=5)
        ttk.Button(update_admin, text="Update Password", command=lambda: self.update_password(update_admin)).grid(row=2, column=0, pady=5)
        ttk.Button(update_admin, text="Update Address", command=lambda: self.update_address(update_admin)).grid(row=3, column=0, pady=5)
        
    def update_username(self, parent_window):
        new_username = simpledialog.askstring("Update Username", "Enter the new username:", parent=parent_window)
        if new_username:
            message = self.admin.update_username(new_username)
            messagebox.showinfo("Success", message, parent=parent_window)

    def update_password(self, parent_window):
        new_password = simpledialog.askstring("Update Password", "Enter the new password:", parent=parent_window)
        if new_password:
            confirm_password = simpledialog.askstring("Confirm Password", "Enter the new password again:", parent=parent_window)
            if confirm_password == new_password:
                message = self.admin.update_password(new_password)
                messagebox.showinfo("Success", message, parent=parent_window)
            else:
                messagebox.showerror("Error", "Passwords do not match.", parent=parent_window)

    def update_address(self, parent_window):
        new_address = simpledialog.askstring("Update Address", "Enter the new address:", parent=parent_window)
        if new_address:
            message = self.admin.update_address(new_address)
            messagebox.showinfo("Success", message, parent=parent_window)




def open_assign_doctor_page(parent_window):
    parent_window.destroy()       
    assign_doctor = tk.Tk()
    assign_doctor.title("Assign doctor to Patients")
    assign_doctor.geometry("1000x700")
    assign_doctor.configure(bg='#729DC8')

    with open("patients_file.txt", "r") as file:
        patient_list = file.readlines()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(assign_doctor, text="-----Select patient-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))
 
    headers = ["ID", "First Name", "Last Name", "Age", "Mobile", "Symptoms", "Postcode"]
    for col, header in enumerate(headers):
        tk.Label(assign_doctor, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')
    
    selected_patient = tk.IntVar()

    for i, patient_info in enumerate(patient_list, start=2):  
        patient_info = patient_info.strip().split(",")
        while len(patient_info) < 7:
            patient_info.append("None")

        tk.Radiobutton(assign_doctor, text=patient_info[0], variable=selected_patient, value=i-2, bg="#729DC8", fg="#333333").grid(row=i, column=0, pady=5, padx=10, sticky='nsew')
        for col, info in enumerate(patient_info, start=1):
            tk.Label(assign_doctor, text=info, bg="#729DC8", fg="#333333").grid(row=i, column=col, pady=5, padx=10, sticky='nsew')

        for col in range(8):
            assign_doctor.grid_columnconfigure(col, weight=1)

    select_button = tk.Button(assign_doctor, text="Select Patient", command=lambda: select_doctor( assign_doctor,selected_patient.get()))

    select_button.grid(row=len(patient_list) + 2, column=0, pady=10, padx=10, sticky='nsew')

    add_button = tk.Button(assign_doctor, text="Select Doctor", command=select_doctor)
    add_button.grid(row=len(patient_list) + 3, column=0, pady=10, padx=10, sticky='nsew')

   

    back_button = tk.Button(assign_doctor, text="Back to Main Page", command=lambda: open_menu(assign_doctor))
    back_button.grid(row=len(patient_list) + 3, column=0, pady=10, padx=10, sticky='nsew')

def select_doctor(parent_window,selected_patient_id):
    parent_window.destroy() 
    select_doctor = tk.Tk()
    select_doctor.title("Assign doctor to Patients")
    select_doctor.geometry("1000x700")
    select_doctor.configure(bg='#729DC8')

    with open("doctor.txt", "r") as file:
        doctor_list = file.readlines()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(select_doctor, text="-----Select doctor-----", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    headers = ["ID", "First Name", "Last Name", "Speciality"]
    for col, header in enumerate(headers):
        tk.Label(select_doctor, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    doctor_vars = []
    for i, doctor_info in enumerate(doctor_list, start=2):
        doctor_info = doctor_info.strip().split(",")
        while len(doctor_info) < 4:
            doctor_info.append("None")

        var = tk.StringVar(value=doctor_info[0])
        doctor_vars.append(var)

        tk.Radiobutton(select_doctor, text=str(i-1), variable=var, value=doctor_info[0], bg="#729DC8", fg="#333333").grid(row=i , column=0, pady=5, padx=10, sticky='nsew')
        for col, info in enumerate(doctor_info, start=1):
            tk.Label(select_doctor, text=info, bg="#729DC8", fg="#333333").grid(row=i + 1, column=col, pady=5, padx=10, sticky='nsew')

    for col in range(5):
        select_doctor.grid_columnconfigure(col, weight=1)

    assign_button = tk.Button(select_doctor, text="Assign", command=lambda: assign_patient_to_doctor( selected_patient_id,selected_patient_id, doctor_vars))
    assign_button.grid(row=6, column=0, columnspan=3, pady=(40, 20))
    

    back_button = tk.Button(select_doctor, text="Back to Main Menu", command=lambda: open_menu(select_doctor))
    back_button.place(relx=0.5, rely=0.5, anchor="center")

def assign_patient_to_doctor(parent_window, patient_id, doctor_vars):
    selected_doctor_id = None
    for var in doctor_vars:
        if var.get():
            selected_doctor_id = var.get()
            break

    

    with open("patients_file.txt", "r") as file:
        patient_list = file.readlines()
    with open("doctor.txt", "r") as file:
        doctor_list = file.readlines()

    selected_patient = None
    selected_doctor = None

    for patient_info in patient_list:
        patient_info = patient_info.strip().split(",")
        if patient_info[0] == str(patient_id):
            selected_patient = patient_info
            break

    for doctor_info in doctor_list:
        doctor_info = doctor_info.strip().split(",")
        if doctor_info[0] == selected_doctor_id:
            selected_doctor = doctor_info
            break

    if selected_patient and selected_doctor:
        message = f"Patient {selected_patient[1]} {selected_patient[2]} is assigned to Doctor {selected_doctor[1]} {selected_doctor[2]}"
        print(message)
        parent_window.destroy()
        assignment_window = tk.Toplevel()
        assignment_window.title("Assignment Result")
        assignment_window.geometry("1000x700")
        assignment_window.configure(bg='#729DC8')

        result_label = tk.Label(assignment_window, text=message, bg="#729DC8", fg="#333333", font=font.Font(size=15))
        result_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

        close_button = tk.Button(assignment_window, text="Close", command=assignment_window.destroy)
        close_button.grid(row=0, column=0, columnspan=3, pady=(40, 20))

        assignment_window.destroy()


class Doctor:
    def __init__(self, first_name, last_name, specialty, doctor_id):
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.appointments = []

    def set_appointments(self, appointment_time):
        self.appointments.append(appointment_time)
class HospitalManagementApp:
    def __init__(self, master, parent_window=None):
        self.master = master
        self.parent_window = parent_window
        if self.parent_window:
            self.parent_window.destroy()
        self.master.title("Hospital Management System")
        self.master.geometry("1000x700")
        self.master.configure(bg='#729DC8')

        self.patients = self.load_patients("patients_file.txt")
        self.doctors = self.load_doctors("doctor.txt")

        self.setup_gui()

    def load_patients(self, filename):
        patients = {}
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if len(data) == 5:
                    first_name, last_name, age, phone, postcode = data
                    patient_id = len(patients)  
                    patients[patient_id] = Patient(first_name, last_name, int(age), phone, postcode)
        return patients

    def load_doctors(self, filename):
        doctors = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 3:  
                        first_name, last_name, specialty = data
                        doctor_id = len(doctors)  
                        doctors[doctor_id] = Doctor(first_name, last_name, specialty, doctor_id)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return doctors

    def setup_gui(self):
        tk.Label(self.master, text="Choose the operation:", bg="#729DC8").grid(row=0, column=0, pady=(20, 10))
        tk.Button(self.master, text="1. Book your date", command=self.book_appointment).grid(row=1, column=0, pady=10)
        tk.Button(self.master, text="2. Check your status", command=self.check_status).grid(row=2, column=0, pady=10)

    def book_appointment(self):
        appointment_window = tk.Toplevel(self.master)
        appointment_window.title("Book Appointment")
        appointment_window.geometry("1000x700")
        appointment_window.configure(bg='#729DC8')

        tk.Label(appointment_window, text="Appointment Date and Time:", bg="#729DC8").pack(pady=(20, 10))

        tk.Label(appointment_window, text="Month:").pack()
        self.month_entry = tk.Entry(appointment_window)
        self.month_entry.pack()

        tk.Label(appointment_window, text="Day:").pack()
        self.day_entry = tk.Entry(appointment_window)
        self.day_entry.pack()

        tk.Label(appointment_window, text="Hour:").pack()
        self.hour_entry = tk.Entry(appointment_window)
        self.hour_entry.pack()

        tk.Label(appointment_window, text="Minute:").pack()
        self.minute_entry = tk.Entry(appointment_window)
        self.minute_entry.pack()

        tk.Label(appointment_window, text="Patient ID:").pack()
        self.patient_id_entry = tk.Entry(appointment_window)
        self.patient_id_entry.pack()

        tk.Label(appointment_window, text="Doctor ID:").pack()
        self.doctor_id_entry = tk.Entry(appointment_window)
        self.doctor_id_entry.pack()

        tk.Button(appointment_window, text="Submit", command=self.submit_appointment).pack(pady=20)

    def check_status(self):
        check_status_window = tk.Toplevel(self.master)
        check_status_window.title("Check Patient Status")
        check_status_window.geometry("1000x700")
        check_status_window.configure(bg='#729DC8')

        tk.Label(check_status_window, text="Enter Patient ID:").pack()
        self.patient_id_entry = tk.Entry(check_status_window)
        self.patient_id_entry.pack()

        tk.Button(check_status_window, text="Check Status", command=self.show_status).pack(pady=10)

    def submit_appointment(self):
        try:
            month = self.validate_int(self.month_entry.get(), "Month")
            day = self.validate_int(self.day_entry.get(), "Day")
            hour = self.validate_int(self.hour_entry.get(), "Hour")
            minute = self.validate_int(self.minute_entry.get(), "Minute")
            patient_id = self.validate_int(self.patient_id_entry.get(), "Patient ID")
            doctor_id = self.validate_int(self.doctor_id_entry.get(), "Doctor ID")

            print(f"Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Patient ID: {patient_id}, Doctor ID: {doctor_id}")

            appointment_time = datetime.datetime(2024, month, day, hour, minute, 0)

            print(f"Checking Patient ID: {patient_id} in {self.patients}")
            print(f"Checking Doctor ID: {doctor_id} in {self.doctors}")

            if patient_id in self.patients and doctor_id in self.doctors:
                patient = self.patients[patient_id]
                doctor = self.doctors[doctor_id]

                patient.add_appointment(appointment_time)
                patient.set_status("Approved (Date found)!")
                doctor.set_appointments(appointment_time)

                messagebox.showinfo("Success", "Appointment booked successfully!")
            else:
                raise ValueError("Invalid patient or doctor ID")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(f"Error: {e}")

    def validate_int(self, value, field_name):
        try:
            if not value.strip():
                raise ValueError(f"{field_name} cannot be empty")
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid value for {field_name}: {value}")

    def show_status(self):
        try:
            patient_id = self.validate_int(self.patient_id_entry.get(), "Patient ID")
            if patient_id in self.patients:
                patient = self.patients[patient_id]
                messagebox.showinfo("Status", patient.get_status())
            else:
                raise ValueError("Patient not found")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(f"Error: {e}")

    def run(self):
        self.master.mainloop()

from Patient import Patient   
def open_relocate_Patient_page(parent_window):
    parent_window.destroy()

    relocate_doctor = tk.Toplevel()
    relocate_doctor.title("Relocate ")
    relocate_doctor.geometry("1400x1200")
    relocate_doctor.configure(bg='#729DC8')

    with open("patients_file.txt", "r") as file:
        patient_list = file.readlines()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(relocate_doctor, text="Enter ID of Patient you want to Relocate:", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    headers = ["ID", "First Name", "Last Name", "Age", "Mobile","Postcode", "Symptoms"]
    for col, header in enumerate(headers):
        tk.Label(relocate_doctor, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    for i, patient_info in enumerate(patient_list, start=1):
        patient_info = patient_info.strip().split(",")
        while len(patient_info) < 7:
            patient_info.append("None")

        tk.Label(relocate_doctor, text=str(i), bg="#729DC8", fg="#333333").grid(row=i + 1, column=0, pady=5, padx=10, sticky='nsew')
        for col, info in enumerate(patient_info, start=1):
            tk.Label(relocate_doctor, text=info, bg="#729DC8", fg="#333333").grid(row=i + 1, column=col, pady=5, padx=10, sticky='nsew')

    for col in range(8):
        relocate_doctor.grid_columnconfigure(col, weight=1)


    
    patient_id = tk.Entry(relocate_doctor)
    patient_id.place(relx=0.2, rely=0.78, anchor="center")

    discharge_button = tk.Button(relocate_doctor, text="Relocate", command=lambda:select_doctor(patient_id.get(), relocate_doctor))
    discharge_button.place(relx=0.2, rely=0.82, anchor="center")

    back_button = tk.Button(relocate_doctor, text="Back to Menu Page", command=lambda: open_menu(relocate_doctor))   
    back_button.place(relx=0.6, rely=0.8, anchor="center")

def select_doctor(patient_id, parent_window):
    parent_window.destroy()

    select_doctor = tk.Toplevel()
    select_doctor.title("Select Doctor ")
    select_doctor.geometry("1400x1200")
    select_doctor.configure(bg='#729DC8')


    
    with open("doctor.txt", "r") as file:
        doctor_list = file.readlines()

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(select_doctor, text="Select ID of Doctor:", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    headers = ["ID","First Name", "Last Name", "Speciality"]
    for col, header in enumerate(headers):
        tk.Label(select_doctor, text=header, bg="#729DC8", font=header_font).grid(row=1, column=col, pady=10, padx=10, sticky='nsew')

    for i, doctor_info in enumerate(doctor_list, start=1):
        doctor_info = doctor_info.strip().split(",")
        while len(doctor_info) < 4:
            doctor_info.append("None")

        tk.Label(select_doctor, text=str(i), bg="#729DC8", fg="#333333").grid(row=i + 1, column=0, pady=5, padx=10, sticky='nsew')
        for col, info in enumerate(doctor_info, start=1):
            tk.Label(select_doctor, text=info, bg="#729DC8", fg="#333333").grid(row=i + 1, column=col, pady=5, padx=10, sticky='nsew')

    for col in range(4):
        select_doctor.grid_columnconfigure(col, weight=1)

    doctor_id = tk.Entry(select_doctor)
    doctor_id.place(relx=0.2, rely=0.78, anchor="center")

    select_button = tk.Button(select_doctor, text="Select Doctor", command=lambda:perform_relocate(patient_id, doctor_id.get(), select_doctor))
    select_button.place(relx=0.2, rely=0.82, anchor="center")

    back_button = tk.Button(select_doctor, text="Back to Menu Page", command=lambda: open_menu(select_doctor))   
    back_button.place(relx=0.6, rely=0.8, anchor="center")

    select_doctor.mainloop()
   
    
def perform_relocate(patient_id,doctor_id,parent_window):
    parent_window.destroy()

    perform_relocate = tk.Toplevel()
    perform_relocate.title("Select Doctor")
    perform_relocate.geometry("1400x1200")
    perform_relocate.configure(bg='#729DC8')

    large_font = font.Font(size=25)

    welcome_label = tk.Label(perform_relocate, text="Patient is Relocated:", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))
    
    back_button = tk.Button(perform_relocate, text="Back to Menu Page", command=lambda: open_menu(perform_relocate))   
    back_button.place(relx=0.4, rely=0.8, anchor="center")
    patients = load_patients()  
    doctors = load_doctors()  
    
    patients = load_patients() 
    doctors = load_doctors()

    patient_id = int(patient_id) - 1  
    doctor_id = int(doctor_id) - 1 

    if 0 <= patient_id < len(patients) and 0 <= doctor_id < len(doctors):
      
        patient = patients[patient_id]
        doctor = doctors[patient_id]

        if 'First Name' in patient and 'Last Name' in patient:
            full_name = f"{patient['First Name']} {patient['Last Name']}"
        else:
            full_name = "Unknown Name" 

        patient['Doctor ID'] = doctor['ID']

       
        if 'patients' not in doctor:
            doctor['patients'] = []
        doctor['patients'].append(patient['ID'])

    save_patients(patients)  
    save_doctors(doctors)       
    allocation_label = tk.Label(perform_relocate, text=f"Successfully relocated {full_name} to Dr. {doctors[doctor_id]['First Name']} {doctors[doctor_id]['Last Name']}.", bg="#729DC8", fg="#333333", font=large_font)
    allocation_label.grid(row=1, column=0, columnspan=3, pady=(20, 40))
 
        
    back_button = tk.Button(perform_relocate, text="Back to Menu Page", command=lambda: open_menu(perform_relocate))   
    back_button.place(relx=0.4, rely=0.8, anchor="center")


def load_patients():
    patients = []
    with open('patients_file.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(row)
    return patients

def load_doctors():
    doctors = []
    with open('doctor.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctors.append(row)
    return doctors

def save_patients(patients):
    with open('patients_file.txt', 'w', newline='') as file:
        fieldnames = ["ID", "First Name", "Last Name", "Age", "Mobile", "Symptoms", "Postcode", "Doctor ID"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

def save_doctors(doctors):
    with open('doctor.txt', 'w', newline='') as file:
        fieldnames = ["ID", "First Name", "Last Name", "Speciality"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(doctors)

class PatientAllocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Allocation System")

        self.welcome_label = tk.Label(root, text="Welcome to the Patient Allocation System")
        self.welcome_label.pack()

        self.back_button = tk.Button(root, text="Back to Menu Page", command=self.open_menu)
        self.back_button.pack()


import tkinter as tk
from tkinter import font

def open_management_report_page(parent_window):
    parent_window.destroy()

    
    management_report = tk.Toplevel()
    management_report.title("Hospital Management Report")
    management_report.geometry("1400x1200")
    management_report.configure(bg='#729DC8')

    large_font = font.Font(size=25)
    header_font = font.Font(size=15)

    welcome_label = tk.Label(management_report, text="Hospital Management Report:", bg="#729DC8", fg="#333333", font=large_font)
    welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))

    # Reading total number of doctors
    with open("doctor.txt", "r") as file:
        doctor_list = file.readlines()
        total_doctor = len(doctor_list)

    doctor_label = tk.Label(management_report, text=f"Total number of doctors: {total_doctor}", bg="#729DC8", fg="#333333", font=header_font)
    doctor_label.grid(row=1, column=0, pady=(10, 5))

    # Reading total number of patients
    with open("patients_file.txt", "r") as file:
        patient_list = file.readlines()
        total_patient = len(patient_list)

    patient_label = tk.Label(management_report, text=f"Total number of patients: {total_patient}", bg="#729DC8", fg="#333333", font=header_font)
    patient_label.grid(row=2, column=0, pady=(5, 10))

    # Counting patients based on illness
    total_number_of_patients_based_on_illness = {}
    with open("patients_file.txt", "r") as file:
        for line in file:
            patient_data = line.strip().split(",")
            if len(patient_data) >= 3:
                symptoms = patient_data[2].split(";")
                for symptom in symptoms:
                    if symptom.strip() not in total_number_of_patients_based_on_illness:
                        total_number_of_patients_based_on_illness[symptom.strip()] = 1
                    else:
                        total_number_of_patients_based_on_illness[symptom.strip()] += 1

    illness_label = tk.Label(management_report, text="Total number of patients based on illness:", bg="#729DC8", fg="#333333", font=header_font)
    illness_label.grid(row=3, column=0, pady=(10, 5))

    row_num = 4
    for symptom, count in total_number_of_patients_based_on_illness.items():
        symptom_label = tk.Label(management_report, text=f"{symptom}: {count} patients", bg="#729DC8", fg="#333333", font=header_font)
        symptom_label.grid(row=row_num, column=0, pady=(5, 2))
        row_num += 1

    appointments_label = tk.Label(management_report, text="Total number of appointments per doctor:", bg="#729DC8", fg="#333333", font=header_font)
    appointments_label.grid(row=row_num, column=0, pady=(20, 5))
    row_num += 1

    back_button = tk.Button(management_report, text="Back to Menu Page", command=lambda: open_menu(management_report))
    back_button.place(relx=0.5, rely=0.9, anchor="center")
    for doctor in doctors:
        doctor_name = doctor.first_name 
        doctor_appointments = doctor.get_appointments()
        print(doctor_appointments)
        doctor_label = tk.Label(management_report, text=f"{doctor_name}:", bg="#729DC8", fg="#333333", font=header_font)
        doctor_label.grid(row=row_num, column=0, pady=(5, 2))
        row_num += 1

        for month, count in doctor_appointments.items():
            appointment_label = tk.Label(management_report, text=f"   - {month}: {count} appointments", bg="#729DC8", fg="#333333", font=header_font)
            appointment_label.grid(row=row_num, column=0, pady=(2, 2))
            row_num += 1

    back_button = tk.Button(management_report, text="Back to Doctor Management", command=lambda: open_menu(management_report))
    back_button.place(relx=0.5, rely=0.7, anchor="center")

    management_report.mainloop()



   

def the_main_window():
    splash_screen.destroy()
    import tkinter as tk
    global main_window
    main_window = tk.Tk()
    main_window.title("Main Page")
    main_window.geometry("1000x800")
    main_window.configure(bg='#729DC8')
    
    global username_entry, password_entry, message_label
   
    large_font = font.Font(size=14)

    login_label = tk.Label(main_window,text="Login Page",bg="#729DC8",fg="#333333",font=large_font)
    pass_label = tk.Label(main_window,text="(username=admin,password=123)",bg="#729DC8",fg="#333333",font=large_font)
    username_label = tk.Label(main_window,text="username",bg="#729DC8",fg="#FFFFFF")
    username_entry = tk.Entry(main_window)
    password_label = tk.Label(main_window,text="Password",bg="#729DC8",fg="#FFFFFF")
    password_entry = tk.Entry(main_window,text="*")
    login_button = tk.Button(main_window,text="Login",command=login)
    message_label = tk.Label(main_window, text="", bg="#729DC8", fg="#FFFFFF")

    login_label.place(relx=0.54, rely=0.42, anchor="center")
    pass_label.place(relx=0.54, rely=0.46, anchor="center")
    username_label.place(relx=0.46, rely=0.5, anchor="center")
    username_entry.place(relx=0.56, rely=0.5, anchor="center")
    password_label.place(relx=0.46, rely=0.55, anchor="center")
    password_entry.place(relx=0.56, rely=0.55, anchor="center")
    login_button.place(relx=0.56, rely=0.6, anchor="center")
    message_label.place(relx=0.56, rely=0.63, anchor="center")

       
    
    main_window.mainloop()
    


splash_screen = tk.Tk()
splash_screen.title("Splash Screen")
splash_screen.geometry("790x600")



background_image = tk.PhotoImage(file="picture/last.png")
background_label = tk.Label(splash_screen, image=background_image)
background_label.place(relwidth=1, relheight=1)

progress_label = tk.Label(splash_screen, text="Loading...", font=("Arial", 12))
progress_label.place(relx=0.5, rely=0.85, anchor="center")

progress_bar_style = ttk.Style()
progress_bar_style.theme_use('default')
progress_bar_style.configure("red.Horizontal.TProgressbar", foreground='#FF0000', background='#FF0000') 

progress_bar = ttk.Progressbar(splash_screen, orient="horizontal", length=200, mode="determinate")
progress_bar.place(relx=0.5, rely=0.9, anchor="center")


for i in range(101):
    progress_bar["value"] = i
    splash_screen.update_idletasks()
    time.sleep(0.03)
    progress_label.config(text=f"Loading... {i}%")


splash_screen.after(750, the_main_window)
splash_screen.mainloop()
