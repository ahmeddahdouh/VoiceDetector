from fastapi import FastAPI
from app.core.database import engine
from app.end_points.routes import router
from app.models import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=800, reload=True)