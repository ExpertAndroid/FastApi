from fastapi import FastAPI
from routes import router as task_router  # Import the router from routes.py
from auth import router as auth_router    # Import the router from auth.py

# Create a FastAPI instance
app = FastAPI()

# Include the task router
app.include_router(task_router)

# Include the auth router
app.include_router(auth_router)
