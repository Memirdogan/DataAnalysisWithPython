import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasından veriyi yükleme
df = pd.read_csv('genisletilmis_musteri_veri_seti.csv')

# Gelir Dağılımı Histogramı
plt.figure(figsize=(10, 6))
plt.hist(df['YıllıkGelir'], bins=20, color='skyblue', edgecolor='black')
plt.title('Gelir Dağılımı Histogramı')
plt.xlabel('Yıllık Gelir')
plt.ylabel('Frekans')
plt.grid(True)
plt.savefig('gelir_dagilimi_histogrami.png')
plt.show()

# Yaş Dağılımı Histogramı
plt.figure(figsize=(10, 6))
plt.hist(df['Yaş'], bins=20, color='salmon', edgecolor='black')
plt.title('Yaş Dağılımı Histogramı')
plt.xlabel('Yaş')
plt.ylabel('Frekans')
plt.grid(True)
plt.savefig('yas_dagilimi_histogrami.png')
plt.show()

# Harcama Skorları Dağılımı Histogramı
plt.figure(figsize=(10, 6))
plt.hist(df['HarcamaSkoru'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Harcama Skorları Dağılımı Histogramı')
plt.xlabel('Harcama Skoru')
plt.ylabel('Frekans')
plt.grid(True)
plt.savefig('harcama_skorlari_histogrami.png')
plt.show()

# Yaş ve Harcama Skorları Dağılımı Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Yaş'], df['HarcamaSkoru'], color='orange', alpha=0.5)
plt.title('Yaş ve Harcama Skorları Dağılımı Scatter Plot')
plt.xlabel('Yaş')
plt.ylabel('Harcama Skoru')
plt.grid(True)
plt.savefig('yas_harcama_skorlari_scatter_plot.png')
plt.show()
