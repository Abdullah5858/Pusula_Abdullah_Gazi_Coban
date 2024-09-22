import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\coban\Desktop\ornek_proje\side_effect_data 1.xlsx"
df = pd.read_excel("side_effect_data 1.xlsx")
df
df.head()
df.info()
df.shape
df.isnull()
df.isnull().sum()
df[df.duplicated()]
df.dtypes
df.describe()
df.describe().T

# Eksik verileri yüzdesel olarak görüntüleyin
missing_data = df.isnull().mean() * 100
print(missing_data)

# Eksik veriler için bir ısı haritası (heatmap) oluşturun
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Eksik Verilerin Isı Haritası')
plt.show()

# Kategorik ve sayısal sütunları ayırın
categorical_columns = df.select_dtypes(include=['object']).columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
print(f"Kategorik Sütunlar: {categorical_columns}")
print(f"Sayısal Sütunlar: {numerical_columns}")

# Kategorik sütunlardaki benzersiz değerlerin sayısını görelim
for column in df.select_dtypes(include='object').columns:
    print(f"{column}: {df[column].nunique()} unique values")
sns.countplot(x=df['Cinsiyet'])
plt.title('Cinsiyet Dağılımı')
plt.xticks(rotation=90)
plt.show()  

sns.countplot(x=df['Il'])
plt.title('İl Dağılımı')
plt.xticks(rotation=90)
plt.show()

sns.countplot(x=df['Ilac_Adi'])
plt.title('İlaç Adı Dağılımı')
plt.xticks(rotation=90)
plt.show()

sns.countplot(x=df['Yan_Etki'])
plt.title('Yan Etki Dağılımı')
plt.xticks(rotation=90)
plt.show()

# Kronik hastalıklara sahip kullanıcıları inceleyelim
plt.figure(figsize=(14,6))
sns.countplot(x='Kronik Hastaliklarim', data=df, palette='Spectral')
plt.title('Kronik Hastalık Dağılımı')
plt.xticks(rotation=90)
plt.show()

# Sayısal sütunlar için temel istatistikler
df.describe()

# Kategorik sütunlardaki benzersiz değerler
for col in categorical_columns:
    print(f"{col} sütunundaki benzersiz değerler:")
    print(df[col].value_counts())
    print("\n")

# Sayısal değişkenler için histogramlar
numeric_columns = ['Kilo', 'Boy']
for col in numeric_columns:
    sns.histplot(df[col], kde=True)
    plt.title(f'{col} Dağılımı')
    plt.show()

# Korelasyon matrisi (sadece sayısal değişkenler için)
plt.figure(figsize=(10, 6))
corr_matrix = df[['Kilo', 'Boy']].corr()

# Isı haritası ile korelasyon matrisi
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Sayısal Değişkenler Arasındaki Korelasyon')
plt.show()

# Cinsiyet ve Yan Etki arasındaki ilişkiyi inceleme
plt.figure(figsize=(8, 4))
sns.countplot(x='Cinsiyet', hue='Yan_Etki', data=df, palette='Set1')
plt.title('Cinsiyet ve Yan Etki İlişkisi')
plt.legend(title='Yan Etki', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Kronik hastalıklar ve yan etki arasındaki ilişkiyi inceleme
plt.figure(figsize=(15, 6))
sns.countplot(x='Kronik Hastaliklarim', hue='Yan_Etki', data=df, palette='Set1')
plt.title('Kronik Hastalıklar ve Yan Etki İlişkisi')
plt.xticks(rotation=90)  # Hastalık isimlerinin daha rahat okunması için döndürme
plt.legend(title='Yan Etki', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# İlaç kullanım süresi (gün farkı) hesaplama
df['Ilac_Kullanma_Suresi'] = (df['Ilac_Bitis_Tarihi'] - df['Ilac_Baslangic_Tarihi']).dt.days

# İlaç kullanım süresi ve yan etki arasındaki ilişki
plt.figure(figsize=(10, 6))
sns.boxplot(x='Yan_Etki', y='Ilac_Kullanma_Suresi', data=df, palette='Set3')
plt.title('İlaç Kullanma Süresi ve Yan Etki İlişkisi')
plt.xticks(rotation=90)
plt.show()

# Alerjiler ve yan etki arasındaki ilişkiyi inceleme
plt.figure(figsize=(10, 6))
sns.countplot(x='Alerjilerim', hue='Yan_Etki', data=df, palette='Set2')
plt.title('Alerjiler ve Yan Etki İlişkisi')
plt.xticks(rotation=90)
plt.legend(title='Yan Etki', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
