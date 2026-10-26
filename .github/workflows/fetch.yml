name: Otomatik Kur Verisi Çekme

on:
  schedule:
    - cron: '0 9 * * *'
  workflow_dispatch:

jobs:
  fetch:
    runs-on: ubuntu-latest
    steps:
      - name: Depoyu Klonla
        uses: actions/checkout@v3

      - name: Python Kur
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Kütüphaneleri Yükle
        run: pip install requests

      - name: Veriyi Çek
        env:
          EVDS_API_KEY: ${{ secrets.EVDS_API_KEY }}
        run: python fetch_data.py

      - name: Değişiklikleri Depoya Kaydet
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "Otomatik kur verisi güncellendi" || exit 0
          git push
