from pydantic import BaseModel, computed_field
from typing import List, Optional, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: Optional[bool] = None
    allergic: List[str]
    contact_detail: Dict[str, str]
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
   
# function 1
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergic)
    print(patient.contact_detail)
    print("BMI:", patient.calculate_bmi)
    print("data has been inserted in the database")
# function 2

patient_info={
    "name":"ashutosh",
    "age":65,
    "weight":70.5,
    "height":1.75,
    "married":False,
    "allergic":["pollen","dust"],
    "contact_detail":{"Phone":"XXXXXXXXXX", "emergency":"123456789"}
}

Patient1 = Patient(**patient_info)

#function calling
insert_patient_data(Patient1)