# step 1: importing the base call of pydantic
from pydantic import BaseModel

# pydantic class
class Patient(BaseModel):
    # type validation
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data has been inserted in the database")

# step 2: validation object: 
# now we will create a dictonary before instanciationg the object
patient_info={"name":"ashutosh",
             "age":30}

# object creation
patient1 = Patient(**patient_info) #** is used to unpack the dictionary

insert_patient_data(patient1)