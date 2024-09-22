import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:...\side_effect_data 1.xlsx"
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler
print(df.isnull().sum())

# Checking the current distribution of the 'Cinsiyet' (Gender) column
cinsiyet_dagilimi = df['Cinsiyet'].value_counts(normalize=True)
print(cinsiyet_dagilimi)
# Getting the current gender distribution in the 'Cinsiyet' column
cinsiyet_dagilimi = df['Cinsiyet'].value_counts(normalize=True)
# Retrieving the indices of rows with missing values in the 'Cinsiyet' column
missing_indices = df[df['Cinsiyet'].isnull()].index
# Calculating the number of missing values to be filled
num_missing = len(missing_indices)
num_women = int(num_missing * cinsiyet_dagilimi['Female'])  # Number of women to fill
num_men = num_missing - num_women  # Number of men to fill
# Generating random gender values according to the observed proportions
random_gender = np.random.choice(['Female', 'Male'], size=num_missing, 
                                 p=[cinsiyet_dagilimi['Female'], cinsiyet_dagilimi['Male']])
# Filling the missing gender values
df.loc[missing_indices, 'Cinsiyet'] = random_gender
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)  # 1 satır, 2 sütun, 1. grafik
cinsiyet_dagilimi_after = df['Cinsiyet'].value_counts(normalize=True)
cinsiyet_dagilimi_after.plot.pie(autopct='%1.1f%%', colors=['lightcoral', 'lightseagreen'], startangle=90)
plt.title('Eksik Doldurulduktan Sonra Cinsiyet Dağılımı')
plt.ylabel('')

# İl sütunundaki benzersiz (unique) illeri görüntüleme
unique_iller = df['Il'].unique()
print(f"İl sütunundaki benzersiz iller: {unique_iller}")
# İl sütunundaki benzersiz değerlerin sayısı
unique_count = df['Il'].nunique()
print(f"İl sütununda {unique_count} farklı il bulunmaktadır.")
# İl sütunundaki mevcut şehirlerin dağılımını inceleme
il_distribution = df['Il'].value_counts(normalize=True)
print("Mevcut şehirlerin oranları:")
print(il_distribution)
# İl sütunundaki eksik veri sayısını bulma
missing_il_count = df['Il'].isnull().sum()
print(f"İl sütununda {missing_il_count} eksik değer var.")
# Her şehre atanacak eksik veri sayısını hesaplama
missing_il_allocation = (il_distribution * missing_il_count).round().astype(int)
print("Her şehre atanacak eksik veri sayısı:")
print(missing_il_allocation)
# Eksik verilerin indekslerini bulma
missing_il_indices = df[df['Il'].isnull()].index
# Her şehrin frekansına göre eksik verileri doldurmak için şehirlerin bir listesini oluşturma
fill_values = np.hstack([[city] * count for city, count in missing_il_allocation.items()])
# Eksik verileri doldurmak için şehir listesini karıştıralım (shuffle) ki dengeli bir dağılım olsun
np.random.shuffle(fill_values)
# Eksik verileri doldurma
df.loc[missing_il_indices, 'Il'] = fill_values
# Doldurma işleminden sonra kontrol edelim
print(df['Il'].isnull().sum())  # 0 olmalı, yani tüm eksik veriler doldurulmuş olmalı.

# Alerjilerim sütunundaki benzersiz değerlerin sayısı
unique_allergies = df['Alerjilerim'].nunique()
print(f"Alerjilerim sütununda {unique_allergies} farklı alerji tipi var.")
# Benzersiz (unique) alerji türlerini inceleme
unique_allergy_list = df['Alerjilerim'].unique()
print("Benzersiz alerji türleri:")
print(unique_allergy_list)
# Alerji türlerinin dağılımı
allergy_distribution = df['Alerjilerim'].value_counts()
print("Alerjilerim sütunundaki verilerin dağılımı:")
print(allergy_distribution) 
plt.figure(figsize=(10, 6))
sns.countplot(y='Alerjilerim', data=df, order=df['Alerjilerim'].value_counts().index[:10], palette='Set3')
plt.title('En Sık Görülen 10 Alerji Türü')
plt.xlabel('Kişi Sayısı')
plt.ylabel('Alerji Türü')
plt.show()  
# En sık görülen ilk 10 alerji türünü bulma
top_10_allergies = df['Alerjilerim'].value_counts().index[:10]
print("En sık görülen ilk 10 alerji türü:")
print(top_10_allergies)
# Eksik Alerjilerim değerlerinin indekslerini bulma
missing_allergies_indices = df[df['Alerjilerim'].isnull()].index
# Eksik değerleri rastgele bir şekilde en sık görülen ilk 10 alerji türünden biriyle doldurma
df.loc[missing_allergies_indices, 'Alerjilerim'] = np.random.choice(top_10_allergies, size=len(missing_allergies_indices), replace=True)  

# Kronik Hastalıklarım sütunundaki eksik veri sayısını bulma
missing_chronic_diseases = df['Kronik Hastaliklarim'].isnull().sum()
total_rows = df.shape[0]
print(f"Kronik Hastalıklarım sütununda {missing_chronic_diseases} eksik değer var.")
print(f"Bu, toplam kayıtların {missing_chronic_diseases / total_rows * 100:.2f}%'ine denk geliyor.")
# Kronik Hastalıklarım sütunundaki benzersiz değerlerin sayısı
unique_chronic_diseases = df['Kronik Hastaliklarim'].nunique()
print(f"Kronik Hastalıklarım sütununda {unique_chronic_diseases} farklı kronik hastalık tipi var.")
# Benzersiz (unique) kronik hastalık türlerini inceleme
unique_chronic_disease_list = df['Kronik Hastaliklarim'].unique()
print("Benzersiz kronik hastalık türleri:")
print(unique_chronic_disease_list)
# Kronik Hastalık türlerinin dağılımı
chronic_disease_distribution = df['Kronik Hastaliklarim'].value_counts()
print("Kronik Hastalıklarım sütunundaki verilerin dağılımı:")
print(chronic_disease_distribution)
# En sık görülen ilk 10 kronik hastalığı ve frekanslarını bulma
top_10_chronic_diseases = df['Kronik Hastaliklarim'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_chronic_diseases.values, y=top_10_chronic_diseases.index, palette='Set2')
plt.title('En Sık Görülen İlk 10 Kronik Hastalık Türü')
plt.xlabel('Frekans (Kişi Sayısı)')
plt.ylabel('Kronik Hastalık Türü')
plt.show()
# En sık görülen ilk 10 hastalık türünü bulma
top_10_chronic_diseases = df['Kronik Hastaliklarim'].value_counts().index[:10]
print("En sık görülen ilk 10 kronik hastalık türü:")
print(top_10_chronic_diseases)
# Eksik Kronik Hastalıklarım değerlerinin indekslerini bulma
missing_chronic_disease_indices = df[df['Kronik Hastaliklarim'].isnull()].index
# Eksik değerleri rastgele bir şekilde en sık görülen ilk 10 hastalık türünden biriyle doldurma
df.loc[missing_chronic_disease_indices, 'Kronik Hastaliklarim'] = np.random.choice(top_10_chronic_diseases, size=len(missing_chronic_disease_indices), replace=True)  

# Baba ve Anne Kronik Hastalıkları sütunlarındaki en sık görülen ilk 10 hastalıkları bulma
top_10_baba_diseases = df['Baba Kronik Hastaliklari'].value_counts().nlargest(10)
top_10_anne_diseases = df['Anne Kronik Hastaliklari'].value_counts().nlargest(10)
# En sık görülen hastalıkları yazdırma
print(f"Baba Kronik Hastalıkları sütununda en sık görülen 10 hastalık:")
print(top_10_baba_diseases)
print(f"\nAnne Kronik Hastalıkları sütununda en sık görülen 10 hastalık:")
print(top_10_anne_diseases)
# Baba Kronik Hastalıkları eksikse ve Anne Kronik Hastalıkları doluysa, Baba'yı Anne ile doldur
df.loc[df['Baba Kronik Hastaliklari'].isnull() & df['Anne Kronik Hastaliklari'].notnull(), 'Baba Kronik Hastaliklari'] = df['Anne Kronik Hastaliklari']
# Anne Kronik Hastalıkları eksikse ve Baba Kronik Hastalıkları doluysa, Anne'yi Baba ile doldur
df.loc[df['Anne Kronik Hastaliklari'].isnull() & df['Baba Kronik Hastaliklari'].notnull(), 'Anne Kronik Hastaliklari'] = df['Baba Kronik Hastaliklari']  

# Kız Kardeş ve Erkek Kardeş Kronik Hastalıkları sütunlarındaki en sık görülen ilk 10 hastalıkları bulma
top_10_kiz_kardes_diseases = df['Kiz Kardes Kronik Hastaliklari'].value_counts().nlargest(10)
top_10_erkek_kardes_diseases = df['Erkek Kardes Kronik Hastaliklari'].value_counts().nlargest(10)
# En sık görülen hastalıkları yazdırma
print(f"Kız Kardeş Kronik Hastalıkları sütununda en sık görülen 10 hastalık:")
print(top_10_kiz_kardes_diseases)
print(f"\nErkek Kardeş Kronik Hastalıkları sütununda en sık görülen 10 hastalık:")
print(top_10_erkek_kardes_diseases)
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.barplot(x=top_10_kiz_kardes_diseases.values, y=top_10_kiz_kardes_diseases.index, palette='Set3')
plt.title('Kız Kardeş Kronik Hastalıkları - İlk 10')
plt.xlabel('Frekans (Kişi Sayısı)')
plt.ylabel('Kronik Hastalık Türü')
plt.subplot(1, 2, 2)
sns.barplot(x=top_10_erkek_kardes_diseases.values, y=top_10_erkek_kardes_diseases.index, palette='Set2')
plt.title('Erkek Kardeş Kronik Hastalıkları - İlk 10')
plt.xlabel('Frekans (Kişi Sayısı)')
plt.ylabel('Kronik Hastalık Türü')
plt.tight_layout()
plt.show()  

# Erkek Kardeş Kronik Hastalıkları eksikse ve Kız Kardeş Kronik Hastalıkları doluysa, Erkek Kardeş'i Kız Kardeş ile doldur
df.loc[df['Erkek Kardes Kronik Hastaliklari'].isnull() & df['Kiz Kardes Kronik Hastaliklari'].notnull(), 'Erkek Kardes Kronik Hastaliklari'] = df['Kiz Kardes Kronik Hastaliklari']
# Kız Kardeş Kronik Hastalıkları eksikse ve Erkek Kardeş Kronik Hastalıkları doluysa, Kız Kardeş'i Erkek Kardeş ile doldur
df.loc[df['Kiz Kardes Kronik Hastaliklari'].isnull() & df['Erkek Kardes Kronik Hastaliklari'].notnull(), 'Kiz Kardes Kronik Hastaliklari'] = df['Erkek Kardes Kronik Hastaliklari']
# Kız ve Erkek Kardeş Kronik Hastalıkları eksikse ve Anne doluysa, Kız veya Erkek Kardeş'i Anne ile doldur
df.loc[df['Kiz Kardes Kronik Hastaliklari'].isnull() & df['Anne Kronik Hastaliklari'].notnull(), 'Kiz Kardes Kronik Hastaliklari'] = df['Anne Kronik Hastaliklari']
df.loc[df['Erkek Kardes Kronik Hastaliklari'].isnull() & df['Anne Kronik Hastaliklari'].notnull(), 'Erkek Kardes Kronik Hastaliklari'] = df['Anne Kronik Hastaliklari']
# Kız ve Erkek Kardeş Kronik Hastalıkları eksikse ve Baba doluysa, Kız veya Erkek Kardeş'i Baba ile doldur
df.loc[df['Kiz Kardes Kronik Hastaliklari'].isnull() & df['Baba Kronik Hastaliklari'].notnull(), 'Kiz Kardes Kronik Hastaliklari'] = df['Baba Kronik Hastaliklari']
df.loc[df['Erkek Kardes Kronik Hastaliklari'].isnull() & df['Baba Kronik Hastaliklari'].notnull(), 'Erkek Kardes Kronik Hastaliklari'] = df['Baba Kronik Hastaliklari']  

# Kan Grubu sütunundaki verilerin dağılımını hesaplama
kan_grubu_distribution = df['Kan Grubu'].value_counts()
# Grafik boyutunu ayarlama
plt.figure(figsize=(8, 6))
# Çubuk grafik oluşturma
sns.barplot(x=kan_grubu_distribution.index, y=kan_grubu_distribution.values, palette='Blues_d')
# Başlık ve eksen etiketlerini ekleme
plt.title('Kan Grubu Dağılımı')
plt.xlabel('Kan Grubu')
plt.ylabel('Frekans (Kişi Sayısı)')
# Grafiği gösterme
plt.show()
# Kan grubu kombinasyonlarına göre olası çocuk kan gruplarını tahmin eden fonksiyon
def tahmin_kan_grubu(anne_kan_grubu, baba_kan_grubu):
    # Eğer anne veya baba kan grubu eksikse None döndür
    if pd.isnull(anne_kan_grubu) or pd.isnull(baba_kan_grubu):
        return None

    # ABO sistemi için olası kombinasyonlar
    possible_blood_types = []
    if 'A' in anne_kan_grubu and 'A' in baba_kan_grubu:
        possible_blood_types = ['A', 'O']
    elif ('A' in anne_kan_grubu and 'B' in baba_kan_grubu) or ('B' in anne_kan_grubu and 'A' in baba_kan_grubu):
        possible_blood_types = ['A', 'B', 'AB', 'O']
    elif 'A' in anne_kan_grubu and 'O' in baba_kan_grubu or 'O' in anne_kan_grubu and 'A' in baba_kan_grubu:
        possible_blood_types = ['A', 'O']
    elif 'B' in anne_kan_grubu and 'B' in baba_kan_grubu:
        possible_blood_types = ['B', 'O']
    elif 'B' in anne_kan_grubu and 'O' in baba_kan_grubu or 'O' in anne_kan_grubu and 'B' in baba_kan_grubu:
        possible_blood_types = ['B', 'O']
    elif 'AB' in anne_kan_grubu and 'A' in baba_kan_grubu or 'A' in anne_kan_grubu and 'AB' in baba_kan_grubu:
        possible_blood_types = ['A', 'B', 'AB']
    elif 'AB' in anne_kan_grubu and 'B' in baba_kan_grubu or 'B' in anne_kan_grubu and 'AB' in baba_kan_grubu:
        possible_blood_types = ['A', 'B', 'AB']
    elif 'AB' in anne_kan_grubu and 'AB' in baba_kan_grubu:
        possible_blood_types = ['A', 'B', 'AB']
    elif 'AB' in anne_kan_grubu and 'O' in baba_kan_grubu or 'O' in anne_kan_grubu and 'AB' in baba_kan_grubu:
        possible_blood_types = ['A', 'B']
    elif 'O' in anne_kan_grubu and 'O' in baba_kan_grubu:
        possible_blood_types = ['O']

    # RhD sistemi için olasılıklar
    rh_anne = '+' if 'RH+' in anne_kan_grubu else '-'
    rh_baba = '+' if 'RH+' in baba_kan_grubu else '-'

    if rh_anne == '-' and rh_baba == '-':
        rh_factor = 'RH-'
    else:
        rh_factor = np.random.choice(['RH+', 'RH-'], p=[0.75, 0.25])  # %75 RH+, %25 RH- olasılığı

    # ABO ve RhD gruplarını birleştir
    if possible_blood_types:
        return np.random.choice(possible_blood_types) + " " + rh_factor
    else:
        return None

# Kan grubu doldurma fonksiyonu
def kan_grubu_doldur(row):
    if pd.isnull(row['Kan Grubu']):
        olasi_kan_grubu = tahmin_kan_grubu(row['Anne Kronik Hastaliklari'], row['Baba Kronik Hastaliklari'])
        if olasi_kan_grubu:
            return olasi_kan_grubu
    return row['Kan Grubu']  

# Eksik verileri ortalama ile doldurma (SimpleImputer ile)
imputer = SimpleImputer(strategy='mean')
# Kilo ve Boy sütunlarında eksik verileri dolduruyoruz
df['Kilo'] = imputer.fit_transform(df[['Kilo']])
df['Boy'] = imputer.fit_transform(df[['Boy']])

# Eksik verilerin doldurulması (örneğin, Cinsiyet sütunundaki eksik verileri doldurma işlemi)
df.loc[missing_indices, 'Cinsiyet'] = random_gender

# One-Hot Encoding uygulanması
categorical_columns = ['Cinsiyet', 'Uyruk', 'Il', 'Ilac_Adi', 'Yan_Etki', 'Alerjilerim', 
                       'Kronik Hastaliklarim', 'Baba Kronik Hastaliklari', 'Anne Kronik Hastaliklari', 
                       'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari', 'Kan Grubu']

# Kategorik sütunları One-Hot Encoding ile sayısal değerlere dönüştürme
df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)


(df_encoded.head())      













  

  
