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

# now we will export our model
temp = patient1.model_dump(exclude={"adress"}) # it will convert into dictionary
demp = patient1.model_dump_json(include={"name", "age", "gender"}) # it will convert into json format
print(temp)
print(demp)
# print(type(temp))
# print(type(demp))
# You can also include or exclude the feild by passing them to teh specific dump model
