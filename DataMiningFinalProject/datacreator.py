import pandas as pd
import random

# Rastgele veri üretimi için yardımcı fonksiyonlar
def generate_age():
    return random.randint(18, 70)

def generate_gender():
    return random.choice(['Erkek', 'Kadın'])

def generate_income():
    return random.randint(20000, 100000)

def generate_spending_score():
    return random.randint(1, 100)

def generate_days_since_last_purchase():
    return random.randint(1, 365)

# Veri seti oluşturma
data = {
    'MüşteriID': list(range(1, 501)),
    'Yaş': [generate_age() for _ in range(500)],
    'Cinsiyet': [generate_gender() for _ in range(500)],
    'YıllıkGelir': [generate_income() for _ in range(500)],
    'HarcamaSkoru': [generate_spending_score() for _ in range(500)],
    'SonAlışveriştenBeriGün': [generate_days_since_last_purchase() for _ in range(500)]
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# CSV dosyasına yazma
df.to_csv('genisletilmis_musteri_veri_seti.csv', index=False)

print("Genişletilmiş CSV dosyası oluşturuldu.")
