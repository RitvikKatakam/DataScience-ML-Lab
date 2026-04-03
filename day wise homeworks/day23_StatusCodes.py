#their r series of status codes
#1. two series
#2. 2xx
#3. 4xx
#4. 5xx

#two series
"""
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_400_BAD_REQUEST
status.HTTP_404_NOT_FOUND
status.HTTP_500_INTERNAL_SERVER_ERROR
"""
#200 series
from fastapi import FastAPI,status
app = FastAPI()
@app.get("/home",status_code=status.HTTP_200_OK)
async def home():
    return ("sucess")

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created"}