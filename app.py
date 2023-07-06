from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5050)
