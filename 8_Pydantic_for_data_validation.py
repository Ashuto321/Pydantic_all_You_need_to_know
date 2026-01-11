from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name: str = Annotated[str, Field(max_length=50, description="Name of the patient in max 50 characters", example=["Ashutosh Pandey"])]
    email: EmailStr
    linkdin_Url: AnyUrl
    age: int = Field(gt=0, lt=100) 
    weight: float = Field(gt=0)
    married: Optional[bool]=None
    allergic:List[str]
    Contact_detail: Dict[str,str]
    
    
    # creation our function to perform
    
def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.email)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergic)
        print(patient.Contact_detail)
        print("data has been inserted in the database")
        

patient_info={
    "name":"ashutosh",
    "email":"abc@gamil.com",
    "age":30,
    "linkdin_Url":"http://linkdin.com/1234",
    "weight":10,
    "married":False,
    "allergic":["pollen","dust"],
    "Contact_detail":{"Phone":"XXXXXXXXXX"}
}   

Patient1 = Patient(**patient_info)
#function calling
insert_patient_data(Patient1)