from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from validation_schema import Payment

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/payment/validate")
def validate_payment(
    payload: Payment,
):
    #API BODY
    
    return {"message": "Payment Details Validated Successfully", "data": payload}
    
    


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001, reload=True)






