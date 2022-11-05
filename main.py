from datetime import datetime, date
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root():
  return {"Welcome": "Hello, World"}

@app.get("/day")
def day_of_year():
    day_of_year = datetime.now().timetuple().tm_yday
    return int(day_of_year)

@app.get("/percent")
def percentage_of_year():
    day_of_year = datetime.now().timetuple().tm_yday
    percentage_year_complete = (day_of_year/365)*100
    print(type(percentage_year_complete))
    

    return percentage_year_complete

@app.get("/progress")
def progressbar():
    day_of_year = datetime.now().timetuple().tm_yday
    percentage = (day_of_year/365)*100
    bar = '◾' * int(percentage) + '-' * (100-int(percentage))
    bar = '😎' * int(percentage) + '-' * (100-int(percentage))
    # display = f"\r|{bar}| {percentage:.2f}%", end="\r"
    return f"{bar}| {percentage:.2f}%"
    
