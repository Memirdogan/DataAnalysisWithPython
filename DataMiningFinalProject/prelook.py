import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

# CSV dosyasından veriyi yükleme
df = pd.read_csv('genisletilmis_musteri_veri_seti.csv')

# Verinin ilk 5 satırını görüntüleme
print("Veri Setinin İlk 5 Satırı:")
print(df.head())

# Veri setinin genel bilgilerini görüntüleme
print("\nVeri Setinin Genel Bilgileri:")
print(df.info())

# Sayısal sütunların istatistiksel özetini görüntüleme
print("\nSayısal Sütunların İstatistiksel Özeti:")
print(df.describe())

# Kategorik sütunların benzersiz değerlerini ve sayılarını görüntüleme
print("\nKategorik Sütunların Benzersiz Değerleri:")
for column in df.select_dtypes(include=['object']).columns:
    print(f"{column}: {df[column].nunique()} farklı değer")

# Her bir sütunun eksik değerlerini kontrol etme
print("\nHer Bir Sütundaki Eksik Değerlerin Sayısı:")
print(df.isnull().sum())
