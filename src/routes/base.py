from fastapi import APIRouter
import os 

base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def welcome():
    
    return{
        "message":"Welcom to my rag app production",
        "appName": os.getenv("APP_NAME"),
        "appVersion":os.getenv("APP_VERSION")
    }