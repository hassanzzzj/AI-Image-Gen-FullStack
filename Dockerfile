# 1. Light-weight Python image
FROM python:3.9-slim

# 2. Container ke andar folder setup
WORKDIR /app

# 3. Pehle requirements install karte hain (ye caching mein madad karta hai)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Baqi sara code copy karo
COPY . .

# 5. Streamlit ki port expose karo
EXPOSE 8501

# 6. Seedha app chalao (Healthcheck ke baghair taake error na aaye)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]