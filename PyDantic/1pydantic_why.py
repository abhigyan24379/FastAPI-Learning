from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict,Optional, Annotated

class Patient(BaseModel):
    
    name:str = Annotated[str, Field(max_length=50, title='Name of the oatient', description="Give your name "
                                    ,examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedUrl: AnyUrl
    age: int
    
    # weight: float = Field(gt=0)
    weight: Annotated[float, Field(gt=0, strict=True)]
    
    # married : bool = False
    married : Annotated[bool, Field(default=None, description="Is the patient married")]
    
    # allergies:Optional[List[str]] = None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    
    contact_details: Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains= ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not in domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls,value ):
        if 0< value < 100:
            return value
        else:
            raise ValueError('Age should be in b/w 0 and 100')

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    
    # if type(name) == str and type(age) == int:
    #     if age < 0:
    #         raise ValueError('Age cannot be negative')
    #     print(name)
    #     print(age)
    # else:
    #     raise TypeError("Incorrect data type")
    

patient_info = {'name':'nitish', 'email':'abhs@hdfc.com', 'linkedUrl':'https://linkedIn.com',
                'age': 30, 'weight':75.2,  
                 'contact_details':{
                    'email':'abs@gmail.com',
                    'phn':'23545443'
                }}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)