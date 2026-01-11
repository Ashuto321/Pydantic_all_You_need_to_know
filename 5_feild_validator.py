from pydantic import BaseModel,Field, field_validator,EmailStr, AnyUrl
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    # we will use this method with a decorator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # we will create a valid domain
        valid_domains = ["hdfc.com","icici.com"]
        
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")
        return value
    
    # for transformation also we will use the same
    @field_validator('name')
    @classmethod
    def transformers(cls, value):
        return value.upper()

def insert_into_patient_detail(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("data has been inserted in the database")
    
# we will create a dictonary for our data valodation

Patient_info ={'name':'Ashutosh Pandey',
               'age':30,    
               'weight':70.5,
               'email':'ashutosh@hdfc.com',
               'married':False,
                'allergies':['pollen','dust'],
                'contact_details':{'Phone':'XXXXXXXXXX'}}


# creating the oject for our class
Patient1 = Patient(**Patient_info)
# now we will make a function call for this 
insert_into_patient_detail(Patient1)