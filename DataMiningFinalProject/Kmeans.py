import pandas as pd
from sklearn.cluster import KMeans

# CSV dosyasından veriyi yükleme
df = pd.read_csv('genisletilmis_musteri_veri_seti.csv')

# 'Cinsiyet' sütununu kaldırma
df = df.drop('Cinsiyet', axis=1)

# K-means modelini oluşturma
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df[['YıllıkGelir', 'Yaş', 'HarcamaSkoru']])

# Her bir müşteri için atanan küme etiketlerini alın
df['Segment'] = kmeans.labels_

# Her bir kümenin merkezlerini görüntüleme
print("Küme Merkezleri:")
print(kmeans.cluster_centers_)

# Her bir küme için özet istatistikler
print("\nKüme Özet İstatistikleri:")
print(df.groupby('Segment').describe())

# Her bir kümenin özelliklerini analiz etme
for i in range(3):
    print(f"\nSegment {i+1} için Özellikler:")
    segment_df = df[df['Segment'] == i].drop('Segment', axis=1)
    print(segment_df.mean())
