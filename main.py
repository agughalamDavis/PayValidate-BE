from typing import Union
from fastapi import FastAPI
import uvicorn
from validation_schema import Payment

app = FastAPI()




@app.post("/payment/validate")
def validate_payment(
    payload: Payment,
):
    #body
    
    return {"message": "Payment Details Validated Successfully", "data": payload}
    
    


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001, reload=True)






