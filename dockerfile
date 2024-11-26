# Gunakan image Python sebagai base
FROM python:3.9-slim

# Atur direktori kerja
WORKDIR /app

# Salin file requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode
COPY . .

# Expose port untuk aplikasi Flask
EXPOSE 5000

# Command untuk menjalankan aplikasi
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
