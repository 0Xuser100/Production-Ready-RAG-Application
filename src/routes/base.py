from fastapi import APIRouter,Depends
import os 
from helpers.config import get_settings,Settings

base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def welcome(app_setting:Settings=Depends(get_settings)):
    
    app_name=app_setting.APP_NAME
    app_version=app_setting.APP_VERSION
    return{
        "message":"Welcom to my rag app production",
        "appName": app_name,
        "appVersion":app_version
    }