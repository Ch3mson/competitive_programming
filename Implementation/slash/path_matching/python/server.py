from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn

app = FastAPI()

class OpenApiHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # TODO: Implement
        
        response = await call_next(request)
        return response

# Apply the middleware
app.add_middleware(OpenApiHandlerMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=3000, reload=True)