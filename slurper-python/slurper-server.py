from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

#class InputData(BaseModel):
#    param: str

#def run_script(data: InputData):

@app.post("/api/v1/retrieve/")
def run_script():
    try:
        result = subprocess.check_output(['python3', './agents/agent-retrieval.py']) #, data.param])
        result = result.decode('utf-8')
    except Exception as e:
        return {"error": str(e)}

    return {"status": result}
