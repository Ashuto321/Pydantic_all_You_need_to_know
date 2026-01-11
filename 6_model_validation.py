from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Optional, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None
    allergic: List[str]
    contact_detail: Dict[str, str]
    
    # again you have to create a decorator for model validation
    @model_validator(mode='after') 
    #no inputs just the mode.
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_detail:
            raise ValueError("Emergency contact is required for patients above 60 years")
        return model
    
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
    "age":65,
    "weight":70.5,
    "married":False,
    "allergic":["pollen","dust"],
    "contact_detail":{"Phone":"XXXXXXXXXX", "emergency":"123456789"}
}

Patient1 = Patient(**patient_info)

#function calling
insert_patient_data(Patient1)