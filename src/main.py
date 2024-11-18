from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# GLOBAL MODULE
from config import global_settings
from router import api_router

app = FastAPI(title="LLAMADex",
              version='0.0.1',
              description="")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[global_settings.FRONTEND_URL],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

app.include_router(api_router,
                   prefix=global_settings.API_V_STR)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",
                host=global_settings.BACKEND_HOST,
                port=global_settings.BACKEND_PORT,
                log_level='info', reload=True if global_settings.ENVIRONMENT != "PRODUCTION" else False)