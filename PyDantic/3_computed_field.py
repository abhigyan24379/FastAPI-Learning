from pydantic import BaseModel, EmailStr , computed_field
from typing import List, Dict , Optional     

class Patient(BaseModel):
    
    name : str
    email:EmailStr
    age:int
    weight: float
    height:float
    married: bool = False
    allergies:Optional[List[str]] = None
    contact_details:Dict[str,str]
    
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/ (self.height**2) , 2)
        return bmi
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print("BMI" , patient.calculate_bmi)
    
patient_info = {'name':'nitish', 'email':'abhs@hdfc.com', 'linkedUrl':'https://linkedIn.com',
                'age': 30, 'weight':75.2,  
                'height':1.72,
                 'contact_details':{
                    'email':'abs@gmail.com',
                    'phn':'23545443'
                }}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)