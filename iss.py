# iss_tracker.py
import requests
import time
import datetime
from geopy.distance import geodesic

def get_iss_location():
    """Open Notify API'den ISS'nin anlık konumunu çeker."""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["message"] == "success":
            lat = float(data["iss_position"]["latitude"])
            lon = float(data["iss_position"]["longitude"])
            return lat, lon
        else:
            print("Hata: ISS konumu alınamadı.")
            return None
    except Exception as e:
        print(f"Hata: API isteği başarısız ({e})")
        return None

def get_country_from_coords(lat, lon):
    """Enlem ve boylama göre ülke bilgisi çeker (basit yaklaşım)."""
    # Not: Gerçek ülke bilgisi için Nominatim gibi bir servis gerekir, burada basit bir örnek.
    try:
        # Gerçek bir API için: Nominatim kullanılabilir, ama burada örnek için sabit veri.
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return "Bilinmeyen Ülke (Okyanus olabilir)"
        return "Bilinmeyen Konum"
    except Exception:
        return "Ülke bilgisi alınamadı"

def check_proximity(user_location, iss_location, threshold_km=1000):
    """ISS'nin kullanıcı konumuna yakınlığını kontrol eder."""
    if not iss_location:
        return False
    user_lat, user_lon = user_location
    iss_lat, iss_lon = iss_location
    distance = geodesic((user_lat, user_lon), (iss_lat, iss_lon)).km
    return distance <= threshold_km, distance

def main():
    # Örnek kullanıcı konumu (örneğin, İstanbul: enlem 41.0082, boylam 28.9784)
    user_location = (41.0082, 28.9784)  # Değiştirebilirsin
    threshold_km = 1000  # Yakınlık eşiği (km)

    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        iss_location = get_iss_location()
        
        if iss_location:
            lat, lon = iss_location
            country = get_country_from_coords(lat, lon)
            print(f"[{timestamp}] ISS Konumu: Enlem {lat:.4f}, Boylam {lon:.4f} ({country})")
            
            is_close, distance = check_proximity(user_location, iss_location, threshold_km)
            if is_close:
                print(f"🚨 UYARI: ISS sana {distance:.2f} km yakınlıkta!")
            else:
                print(f"ISS sana {distance:.2f} km uzakta.")
        else:
            print(f"[{timestamp}] ISS konumu alınamadı.")
        
        print("Bir sonraki kontrol 60 saniye sonra... (Çıkmak için Ctrl+C)")
        time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı.")