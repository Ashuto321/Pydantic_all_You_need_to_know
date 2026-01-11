from pydantic import BaseModel

# for compled feild like adress we will create a class model address
class Adress(BaseModel):
    city:str
    state: str
    country: str
    pincode: int
    
class Patient(BaseModel):
    name:str
    age:int 
    gender: str
    adress: Adress  # nested model
    
# first we will create the address object
address_info={
    "city": "New Delhi",
    "state": "Delhi",
    "country":"India",
    "pincode": 110001
}
# creating the object
address1 = Adress(**address_info)

# now we will create the Patient Object
patient_info={
    "name": "Ashutohs_Pandey",
    "age": 30,
    "gender":"male",
    "adress": address1 # passing the adress object
}

# creating the patient object
patient1 = Patient(**patient_info)

print(patient1.adress.city)
print(patient1.adress.state)
# anyinfo through patient object you can get for adress

