from pydantic import BaseModel
from typing import List, Optional
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None
    allergic: List[str]
    contact_detail: Dict[str, str]
    
# function 1
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergic)
    print(patient.contact_detail)
    print("data has been inserted in the database")
# function 2

patient_info={
    "name":"ashutosh",
    "age":30,
    "weight":70.5,
    "married":False,
    "allergic":["pollen","dust"],
    "contact_detail":{"Phone":"XXXXXXXXXX"}
}

Patient1 = Patient(**patient_info)

#function calling
insert_patient_data(Patient1)