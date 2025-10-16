# ISS-Tracker
Bu proje, Uluslararası Uzay İstasyonu’nun (ISS) anlık konumunu (enlem, boylam) ve hangi ülke üzerinde olduğunu Open Notify API’sini kullanarak çeker ve terminalde gösterir. Ayrıca, belirli bir konuma yakınsa (örneğin, senin konumuna) bir uyarı verir
# ISS Tracker

Bu proje, Uluslararası Uzay İstasyonu’nun (ISS) anlık konumunu takip eder ve belirli bir konuma yakınsa uyarı verir. Open Notify API’sini kullanır.

## Özellikler
- ISS’nin anlık enlem ve boylamını çeker.
- Kullanıcının konumuna göre ISS’nin yakınlığını hesaplar (varsayılan: 1000 km).
- Her 60 saniyede bir konum güncellenir ve terminalde gösterilir.

## Kurulum
1. Python 3.x kurulu olmalı.
2. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
