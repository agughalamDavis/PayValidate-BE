from pydantic import BaseModel
from datetime import date, datetime
from pydantic import BaseModel, root_validator, validator
from fastapi import HTTPException, status
from utils import luhns_algorithm


class Payment(BaseModel):
    card_name: str
    card_number: str
    cvv: str
    expiry_date: date

    @root_validator(pre=True)
    @classmethod
    def validate_expiry_date(cls, values):
        expiry_date = values.get("expiry_date")
        today = datetime.today()
        date_format = '%Y-%m-%d'
        try:
            expiry_date = datetime.strptime(expiry_date, date_format)
        except Exception:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Date Format! Please use Y-m-d")

        if expiry_date < today :
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Card has expired!")
        
        return values


    @root_validator(pre=True)
    @classmethod
    def validate_card_number(cls, values):
        card_number = values.get("card_number")
       
        if len(card_number) < 16 or len(card_number) > 19:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Card Number!")


        #luhn algorithm
        check_digit = card_number[-1]
        if int(check_digit) != luhns_algorithm(card_number=card_number):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Card Number!")

        print(luhns_algorithm(card_number=card_number))
        return values


    @root_validator(pre=True)
    @classmethod
    def validate_cvv(cls, values):
        cvv = values.get("cvv")
        card_number = values.get("card_number")

        if card_number[0:2] == "34" or card_number[0:2] == "37":
            if len(cvv) != 4:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Card Details!")
        else: 
            if len(cvv) != 3:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Card Details!")
        
        return values

