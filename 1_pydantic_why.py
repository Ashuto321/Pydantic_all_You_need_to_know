# first problem is type validation which is not done in python 
# since pyhton is dynamically typed language

def insert_patient_data(name: str, age: int):
    
    if type(name)== str and type(age)== int:
        print(name)
        print(age)
        print("data has been inserted in the database")
        
    else:
        raise TypeError("Invalid data types for name or age")

# suppose there one more function for updation
def update_patient_data(name: str, age: int):
    
    if type(name)== str and type(age)== int:
        print(name)
        print(age)
        print("data has been updated in the database")
        
    else:
        raise TypeError("Invalid data types for name or age")

# conclusion: how many these type of function yu will write manually
# in production level coding 
# to manage this we use pydantic.


