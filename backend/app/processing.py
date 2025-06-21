#BERISI ALGORITMA UNTUK PERHITUNGAN SVD
import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPRESSED_DIR = os.path.join(BASE_DIR, "compressed")

os.makedirs(COMPRESSED_DIR, exist_ok=True)

#FUNCTION UNTUK MENERIMA UPLOAD GAMBAR
#--MENERIMA URL GAMBAR DARI JS
#--MENYIMPAN GAMBAR YANG DIUPLOAD KE FOLDER UPLOADS/
#--MENGIRIMKAN RETURN VALUE DARI GAMBAR YANG TELAH DI CONVERT

#Preparing
def receiveImage(path_gambar):
    #load and convert to RGB format
    if path_gambar.endswith(".jpg") or path_gambar.endswith(".png"):
        gambarToCompress = cv2.imread(path_gambar)
        if gambarToCompress is None:
            print(f"gambar di {path_gambar} tidak dapat dibaca")
            return "error"
        Matrix_R, Matrix_G, Matrix_B = cv2.split(gambarToCompress)

        return Matrix_R, Matrix_G, Matrix_B

#SVD DECOMPOSITION
def decomposition(Matrix_R, Matrix_G, Matrix_B, quality_persen):
    Matrix_R_norm = Matrix_R / 255.0
    Matrix_G_norm = Matrix_G / 255.0
    Matrix_B_norm = Matrix_B / 255.0
    
    U_R, S_R, Vt_R = np.linalg.svd(Matrix_R_norm, full_matrices=False)
    U_G, S_G, Vt_G = np.linalg.svd(Matrix_G_norm, full_matrices=False)
    U_B, S_B, Vt_B = np.linalg.svd(Matrix_B_norm, full_matrices=False)
    
    rank = len(S_R)
    
    k = max(1, int(rank * (quality_persen / 100.0)))
    
    R_compressed = np.matrix(U_R[:, :k]) @ np.diag(S_R[:k]) @ np.matrix(Vt_R[:k, :])
    G_compressed = np.matrix(U_G[:, :k]) @ np.diag(S_G[:k]) @ np.matrix(Vt_G[:k, :])
    B_compressed = np.matrix(U_B[:, :k]) @ np.diag(S_B[:k]) @ np.matrix(Vt_B[:k, :])
    
    R_compressed = np.clip(R_compressed * 255, 0, 255)
    G_compressed = np.clip(G_compressed * 255, 0, 255)
    B_compressed = np.clip(B_compressed * 255, 0, 255)
    
    compressed_image = cv2.merge([
        R_compressed.astype(np.uint8),
        G_compressed.astype(np.uint8),
        B_compressed.astype(np.uint8)
    ])
    
    return compressed_image

def compression(image_path, compression_rate, output_filename):
    start_time = time.time()
    original_file_size = os.path.getsize(image_path)
    
    Matrix_R, Matrix_G, Matrix_B = receiveImage(image_path)
    
    quality_percent = 100 - compression_rate
    compressed_image = decomposition(Matrix_R, Matrix_G, Matrix_B, quality_percent)
    end_time = time.time()
    execution_time = end_time - start_time
    
    if compressed_image is None:
        print(f"gagal melakukan compression {image_path}")
        return None
    
    output_path = os.path.join(COMPRESSED_DIR, output_filename)
    compressed_file_size = None
    
    try:
        cv2.imwrite(output_path, compressed_image)
        if os.path.exists(output_path):
            compressed_file_size = os.path.getsize(output_path)
            
            original_file_sizeIn_KB = round(original_file_size / 1024, 2)
            compressed_file_sizeIn_KB = round(compressed_file_size / 1024, 2)
            executionTime = round(execution_time, 2)
            return output_path, original_file_sizeIn_KB, compressed_file_sizeIn_KB, executionTime
    except Exception as e:
        print(f"error {e}")
        return None, round(original_file_size / 1024, 2), None


#FUNCTION UNTUK MELAKUKAN COMPRESSION (MAIN FUNCTION)
#--MENERIMA PARAMETER GAMBAR
#--MENERIMA PARAMETER NILAI SKALA UNTUK KOMPRESI
#--MENYIMPAN GAMBAR YANG BERHASIL DI KOMPRESI KE DALAM PATH FOLDER COMPRESSED/
#--MENGIRIMKAN RETURN VALUE DARI GAMBAR YANG BERHASIL DIKOMPRESI KE FE UNTUK DIUNDUH USER