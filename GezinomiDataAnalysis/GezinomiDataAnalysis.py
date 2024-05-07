# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz

import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df = pd.read_excel('Dataset/miuul_gezinomi.xlsx')
print(df.head())
print(df.shape)
print(df.info())