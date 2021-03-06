from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return 'jenkidns test succefully~'


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, log_level="info" )
