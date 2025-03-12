from fastapi import FastAPI
from ..py.day_query import single_day_top_sales

app = FastAPI()
print(app.root_path_in_servers)

@app.get("/sales/{day:str}")
async def getDayTopSales(day: str):

    [theater, sales] = single_day_top_sales(day)

    return {"theater": theater, "total": sales, "day": day}