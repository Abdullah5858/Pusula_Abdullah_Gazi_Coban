import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:...\side_effect_data 1.xlsx
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler

# Doğum tarihine göre yaş hesaplayalım
df['Yas'] = pd.to_datetime('today').year - df['Dogum_Tarihi'].dt.year
print(df[['Dogum_Tarihi', 'Yas']].head())

plt.figure(figsize=(8,6))
sns.histplot(df['Yas'].dropna(), kde=True, color='blue')
plt.title('Yaş Dağılımı')
plt.xlabel('Yaş')
plt.ylabel('Frekans')
plt.show()

# İlaç kullanım süresini hesaplayalım
df['Ilac_Kullanim_Suresi'] = (df['Ilac_Bitis_Tarihi'] - df['Ilac_Baslangic_Tarihi']).dt.days
print(df[['Ilac_Baslangic_Tarihi', 'Ilac_Bitis_Tarihi', 'Ilac_Kullanim_Suresi']].head())
print(df['Ilac_Kullanim_Suresi'].describe())
plt.figure(figsize=(8,6))
sns.histplot(df['Ilac_Kullanim_Suresi'].dropna(), bins=30, kde=True, color='green')
plt.title('İlaç Kullanım Süresi Dağılımı (Gün)')
plt.xlabel('Kullanım Süresi (Gün)')
plt.ylabel('Frekans')
plt.show()
# Yeni bir sütun oluştur - Toplam Kullanım Süresi
df['Toplam_Kullanim_Suresi'] = df['Ilac_Kullanim_Suresi']
# İlk birkaç satırı kontrol edelim
print(df[['Ilac_Baslangic_Tarihi', 'Ilac_Bitis_Tarihi', 'Ilac_Kullanim_Suresi', 'Toplam_Kullanim_Suresi']].head())

from sklearn.cluster import KMeans

# Kullanıcıları yaş ve kilo gibi özelliklere göre gruplandıralım
X_cluster = df[['Yas', 'Kilo']].dropna()

# KMeans ile gruplandırma
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_cluster)
# Grupları görselleştirme
sns.scatterplot(x='Yas', y='Kilo', hue='Cluster', data=df)
plt.title('Kullanıcı Segmentasyonu')
plt.show()

# Vücut Kitle İndeksi (BMI) hesaplama
df['BMI'] = df['Kilo'] / (df['Boy'] / 100) ** 2
# Ailede kronik hastalık var mı? (Binary feature)
df['Ailede_Kronik_Hastalik'] = df[['Baba Kronik Hastaliklari', 'Anne Kronik Hastaliklari', 
                                   'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari']].notnull().any(axis=1).astype(int)
print(df[['BMI', 'Ailede_Kronik_Hastalik']])

pd.set_option('display.max_columns', None)
df.head()
