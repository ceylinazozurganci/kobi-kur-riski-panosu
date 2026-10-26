import os
import json
import requests

# GitHub Secrets'tan API anahtarını al
api_key = os.environ.get("EVDS_API_KEY")

# TCMB EVDS API adresi (USD ve EUR satış kurları)
url = f"https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.USD.A-TP.DK.EUR.A&type=json"

headers = {
    "key": api_key
}

try:
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # data klasörü yoksa oluştur ve veriyi JSON olarak kaydet
    os.makedirs("data", exist_ok=True)
    with open("data/kurlar.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Veri başarıyla çekildi ve data/kurlar.json dosyasına kaydedildi.")
except Exception as e:
    print("Veri çekme hatası:", e)
