import requests
import os

def download_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Datos descargados y guardados en {filename}")
    else:
        print("Error al descargar los datos")

url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
filename = "heart_failure_data.csv"

download_data(url, filename)