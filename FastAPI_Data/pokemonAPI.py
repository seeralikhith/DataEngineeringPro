from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "CSV to JSON API with FastAPI"}

@app.get("/csv-to-json/")
def convert_csv_to_json():
    file_path = "D:/GitHub/DataEngineeringPro/FastAPI_Data/Data/Pokemon.csv" 
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="CSV file not found")

    try:
        df = pd.read_csv(file_path)
        df.replace(r'^\s*$', np.nan, regex=True, inplace=True)  # Replace empty strings with NaN
        json_data = df.where(pd.notnull(df), None).to_dict(orient="records")    # Convert NaN to None for proper JSON serialization
        return {"data": json_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
