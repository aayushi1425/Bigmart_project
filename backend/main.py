from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from database.connection import Database
from routes import products, categories, newsletters

load_dotenv()

app = FastAPI(
    title="BigMart API",
    description="Backend API for BigMart e-commerce platform",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(newsletters.router, prefix="/api/v1/newsletter", tags=["newsletter"])

@app.on_event("startup")
async def startup_db_client():
    await Database.connect_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await Database.close_db()

@app.get("/")
async def root():
    return {"message": "Welcome to BigMart API"} 