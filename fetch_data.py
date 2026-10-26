import os
import json
import requests

# data klasörünü oluştur
os.makedirs("data", exist_ok=True)

api_key = os.environ.get("EVDS_API_KEY")
data = None

# 1. TCMB EVDS API Denemesi
if api_key:
    try:
        url = "https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.USD.A-TP.DK.EUR.A&type=json"
        headers = {"key": api_key}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
    except Exception as e:
        print("EVDS Hata:", e)

# 2. EVDS Olmazsa Frankfurter API Denemesi
if not data:
    try:
        response = requests.get("https://api.frankfurter.app/latest?from=USD&to=TRY", timeout=10)
        if response.status_code == 200:
            data = response.json()
    except Exception as e:
        print("Frankfurter Hata:", e)

# 3. İkisi de Olmazsa Garanti Yedek Veri
if not data:
    data = {
        "status": "ok",
        "rates": {"USD": 34.25, "EUR": 37.10},
        "source": "Yedek Veri"
    }

# Dosyayı kaydet
with open("data/kurlar.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("data/kurlar.json dosyasi basariyla olusturuldu.")
