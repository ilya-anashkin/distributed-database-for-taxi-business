from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

def main():
    """
    Main function
    """
    run(
        app="app.app:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=4
    )

if __name__ == "__main__":
    main()
