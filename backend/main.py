#main file for API
#using for define the endpoint like /upload-images to receive uploads file, and then called function from processing.py and return the result

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

import sys
import os
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
from app import processing as SVD

def allowed_typeFile(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = FastAPI(
    title="Image Compressor API",
    description="API untuk kompresi gambar menggunakan SVD.",
    version="1.0.0"
)

#accepted origin list
#using for register the url of website
origins = [
    "http://localhost:5173",
    "http://localhost:5173/Image_Compression",
    "http://localhost:5173/upload-image",
    "http://localhost:5173/result",
    "http://127.0.0.1:5173",
]

#CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Define base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
COMPRESSED_DIR = os.path.join(BASE_DIR, "compressed")

# Create directories if they don't exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(COMPRESSED_DIR, exist_ok=True)

# Mount static directories for serving images
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads_static")
app.mount("/compressed", StaticFiles(directory=COMPRESSED_DIR), name="compressed_static")


@app.get("/")
async def read_root():
    """
    HALO SELAMAT DATANG DI ROOT FASTAPI!!!!
    """
    return {"message": "Selamat datang di API Kompresor Gambar!"}

#receive the input image
@app.post("/upload-image")
async def uploadImage(
    file: UploadFile = File(...), quality: int = Form(...)
):
    original_file_path = os.path.join(UPLOADS_DIR, file.filename)
    with open(original_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    compressed_output_filename = f"{os.path.splitext(file.filename)[0]}_compressed.jpg"
    compressed_output_path = os.path.join(COMPRESSED_DIR, compressed_output_filename)

    output_path_from_svd, original_size, compressed_size, execution_time = SVD.compression(
        original_file_path, quality, output_filename=compressed_output_path
    )

    return {
        "original_filename": file.filename,
        "original_size": original_size,
        "compressed_filename": os.path.basename(output_path_from_svd), 
        "compressed_size": compressed_size,
        "execution_time": execution_time,
        "image_different_percentage": round((compressed_size / original_size) * 100)
    }

#send the before and afer image compressed
@app.get("/Image_Compression")
async def home():
    return{"halaman home-page"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#NOTE:
#.\venv\Scripts\activate
#uvicorn main:app --reload