from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email: str #EmailStr for validation
    account_id: int
    
    #custom validation
    @validator("account_id")
    def validate_account_id(cls, value):
        if value <=0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

    

user = User(name="jack", email="jack@example.com",account_id=1234)

#user_data ={name: "jack", email: "jack@example.com",account_id: 1234}
#user = User(**user_data)#unpacking dictionary


#converting pydantic model to json
user_json_str = user.json() #json string
user_json_str = user.dict() #python dictionary

json_str = '{"name": "jack", "email": "jack@example.com"}'
user = User.parse_raw(json_str)

#python 3.6+
x: int = 0
