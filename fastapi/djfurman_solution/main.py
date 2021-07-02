from fastapi import FastAPI

from models import ClientInput


app = FastAPI()


@app.route("/area", ["POST"])
async def compute_area(input: ClientInput):
    pass
