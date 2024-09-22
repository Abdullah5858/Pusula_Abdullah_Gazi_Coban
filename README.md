# Pusula_Abdullah_Gazi_Coban

```markdown
# Drug Side Effects Analysis

Bu proje, ilaç yan etkileriyle ilgili bir veri seti üzerinde veri keşfi (EDA), veri ön işleme (Data Pre-Processing) ve özellik mühendisliği (Feature Engineering) gerçekleştirmeyi amaçlamaktadır. Çalışma, Python programlama dili ve çeşitli kütüphaneler kullanılarak yapılmıştır.

## Proje İçeriği

### 1. Exploratory Data Analysis (EDA)
- **Amaç**: Veriyi anlamak ve genel yapısını incelemek.
- **Yöntemler**: Kategorik ve sayısal verilerin dağılımlarını analiz etmek ve görselleştirmek.
- **Kullanılan Kütüphaneler**: Pandas, Matplotlib, Seaborn
- **EDA İçeriği**:
  - Kategorik ve sayısal değişkenlerin incelenmesi.
  - Verinin genel yapısı ve özet istatistiklerinin çıkarılması.
  - Histogramlar, kutu grafikleri ve dağılım grafikleriyle verinin görselleştirilmesi.

### 2. Data Pre-Processing
- **Amaç**: Modelleme öncesinde veriyi temizlemek ve uygun hale getirmek.
- **Yöntemler**:
  - Eksik verilerin doldurulması.
  - Kategorik değişkenlerin kodlanması (One-Hot Encoding).
  - Verideki anomalilerin düzeltilmesi.
- **Özellikle işlenen alanlar**:
  - Eksik sütunlar: Cinsiyet, İl, Alerjilerim, Kronik Hastalıklar vb.
  - Kilo, boy gibi değişkenler üzerinde işlem yapılması.

### 3. Feature Engineering
- **Amaç**: Model için ek özellikler oluşturmak.
- **Yöntemler**:
  - Yaş değişkeninin oluşturulması (Doğum tarihinden hesaplanarak).
  - İlaç kullanım süresinin hesaplanması.
  - Vücut Kitle İndeksi (BMI) hesaplama.

## Proje Klasör Yapısı

```plaintext
/drug-side-effects-analysis
│
├── data/                          # Verilerin yer aldığı klasör
│   └── side_effect_data_1.xlsx     # Örnek veri dosyası
│
├── notebooks/                     # Jupyter Notebook dosyaları
│   └── Data Science Stajyeri Vaka Çalışması.ipynb
│
├── scripts/                       # Python script dosyaları
│   ├── data_pre-processing.py      # Veri ön işleme
│   ├── eda.py                      # Veri keşfi (EDA)
│   └── feature_engineering.py      # Özellik mühendisliği
│
├── README.md                      # Proje açıklamaları (bu dosya)
└── requirements.txt               # Gerekli Python kütüphaneleri
```

## Kullanılan Kütüphaneler

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Gerekli kütüphaneleri kurmak için `requirements.txt` dosyasını kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

## Projeyi Çalıştırma Adımları

1. **Veri Setini Yükleyin**:
   - `data/side_effect_data_1.xlsx` dosyasını kullanarak veriyi yükleyin.

2. **Veri Keşfi (EDA)**:
   - `scripts/eda.py` dosyasını çalıştırarak veri keşfi adımlarını gerçekleştirin.

3. **Veri Ön İşleme**:
   - `scripts/data_pre-processing.py` dosyasını çalıştırarak veriyi temizleyin ve hazırlayın.

4. **Özellik Mühendisliği**:
   - `scripts/feature_engineering.py` dosyasını çalıştırarak yeni özellikler oluşturun.

## Sonuçlar

Proje sonucunda elde edilen bulgular:
- En sık görülen yan etkiler: Yorgunluk, Kabızlık, Çarpıntı vb.
- Eksik verilerin belirlenmesi ve doldurulması.
- Modelleme için uygun hale getirilmiş veri seti.

## GitHub Projesi

Bu proje, [GitHub repository'mde](https://github.com/Abdullah5858/Pusula_Abdullah_Gazi_Coban) yer almaktadır. Kodları incelemek ve çalıştırmak için repository'i klonlayabilir veya indirebilirsiniz.

## İletişim

- **Ad**: Abdullah Gazi Çoban
- **E-posta**: cobanabdullahgazi@gmail.com
```

### Açıklamalar:
- **Başlıklar ve İçerik**: Projeyi anlaşılır kılmak için net başlıklar ve açıklamalar kullandım.
- **Klasör Yapısı**: Proje dosyalarının nasıl organize edildiğini gösterdim.
- **Kütüphaneler**: Projeyi çalıştırmak için gerekli kütüphaneleri ve kurulum komutunu verdim.
- **İletişim Bilgileri**: Kendi adını, soyadını ve e-posta adresini eklemeyi unutma.

Bu şablon, hem projeni iyi bir şekilde anlatır hem de gerekli bilgileri açık bir şekilde sunar. GitHub üzerinde README dosyasını güncelleyerek kullanabilirsin.
