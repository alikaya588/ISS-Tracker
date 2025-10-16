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

3.Script’i çalıştırın:
  python iss_tracker.py

  Kullanım
iss_tracker.py içindeki user_location değişkenini kendi enlem ve boylamınızla güncelleyin (örneğin, İstanbul için (41.0082, 28.9784)).
Script, ISS’nin konumunu ve sana olan mesafesini gösterir.
ISS 1000 km’den yakınsa uyarı verir.
Notlar
Open Notify API’si ücretsizdir ve kimlik doğrulama gerektirmez.
Ülke bilgisi şu an basit bir yer tutucudur; gerçek ülke bilgisi için Nominatim API’si eklenebilir.
Kendi konumunuzu Google Maps’ten enlem/boylam olarak alabilirsiniz.
Gelecek İyileştirmeler
Ülke bilgisi için Nominatim entegrasyonu.
E-posta veya SMS bildirimleri ekleme.
