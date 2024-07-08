# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df = pd.read_excel('Dataset/miuul_gezinomi.xlsx')
print(df.head())
print(df.shape)
print(df.info())

# Soru 2: Kaç unique şehir vardır, frekansları nelerdir?

print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# Soru 3: kaç unique concept vardır

print(df["ConceptName"].nunique())

# Soru 4: Hangi conceptten kaçar tane satış gerçekleşmiştir

print(df["ConceptName"].value_counts())

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru 6: Concept türlerine göre ne kadar kazanılmış?

df.groupby("ConceptName").agg({"Price": "sum"})

# Soru 7: Şehirlere göre PRICE ortalamaları nedir?

df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru 8: Concept türlerine göre PRICE ortalamaları nedir?

df.groupby("ConceptName").agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?

df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

#######################################################
# Görev 2: satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çevirin
#######################################################

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["last minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

#######################################################
# Görev 3: Şehir, Concept, [EB_Score, Sezon, CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız
#######################################################

# Şehir-Concept-EB Score kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"], observed=False).agg({"Price": ["mean", "count"]})

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"], observed=False).agg({"Price": ["mean", "count"]})

# Şehir-Concept-CInday kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"], observed=False).agg({"Price": ["mean", "count"]})


#############################################
# GÖREV 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

#############################################
# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
agg_df.reset_index(inplace=True)

agg_df.head()
#############################################
# GÖREV 6: Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)


#############################################
# GÖREV 7: Personaları segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT", observed=False).agg({"Price": ["mean", "max", "sum"]})

#############################################
# GÖREV 8: Oluşan son df'i price değişkenine göre sıralayınız.
# "ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?
#############################################
agg_df.sort_values(by="Price")


new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]

