# Backend Logic - Handles core functionality & data processing for Wetlands MVP

# Routes & Controllers - Define API endpoints and business logic for processing requests and generating responses
from fastapi import FastAPI
# from uvicorn import run  # INSTEAD use uvicorn command in Terminal to start FastAPI app

# Database Connection - Establish connection to PostgreSQL database using credentials from .env file
app = FastAPI() # Initialize FastAPI app instance
# Route test with GET request to root endpoint ("/") that returns a simple JSON message to confirm API is working. This is a basic test route and can be expanded with more complex routes for handling specific data processing tasks related to the Wetlands MVP.
@app.get("/")                   # Define a simple route to test the API
def read_root():                # Handle GET request to the root endpoint
    return {"message": "Hello, World!"} # Return a JSON response with TEST msg.

# Uncomment the block below if you want to run the app directly
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)