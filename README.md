# Analisis Data Musiman dan Bulanan Penyewaan Sepeda: Tren dan Faktor Penentu 🚲📉📈☁️

## Deskripsi Proyek 📃
Proyek ini merupakan analisis data menggunakan bahasa pemrograman Python. Tujuannya adalah untuk menjawab beberapa pertanyaan bisnis terkait dataset yang digunakan. Dalam proyek ini, dilakukan pembersihan data, eksplorasi data, serta visualisasi untuk mendukung jawaban atas pertanyaan yang diajukan.

## Pemilik 👨🏻‍🦱 :
Nama: Luthfi Mahendra Widiarto

Email: lmahendraw@gmail.com

## Pertanyaan Bisnis 🙋🏻‍♂️
Analisis ini fokus pada beberapa pertanyaan bisnis utama:

- Pada musim apa jumlah pengguna sepeda paling banyak?

- Pada bulan apa jumlah pengguna sepeda paling banyak, dan apa faktor penyebabnya?

## Tools dan Library yang Digunakan ⚙️
- Python

- Streamlit

- Pandas

- Seaborn

- Matplotlib

## Struktur Notebook 🚧
### 1. Pendahuluan
Menjelaskan tujuan proyek dan pertanyaan bisnis yang akan dijawab.

### 2. Import Packages
Mengimpor semua library yang diperlukan, termasuk:

- pandas untuk manipulasi data

- seaborn dan matplotlib untuk visualisasi

- streamlit untuk antarmuka aplikasi web
### 3. Pembersihan Data
Melakukan pembersihan data untuk menghilangkan data yang tidak relevan dan menangani data yang hilang.

### 4. Eksplorasi Data
Melakukan eksplorasi data untuk mendapatkan insight awal mengenai pola-pola dalam dataset.

### 5. Visualisasi Data
Menggunakan grafik untuk memvisualisasikan hasil analisis data, termasuk grafik batang dan heatmap untuk menunjukkan tren penggunaan sepeda.

### 6. Eksplorasi dan Penjelasan Hasil
Menjelaskan hasil eksplorasi data yang telah divisualisasikan untuk menjawab pertanyaan bisnis.

## Setup Environment - Anaconda 🐍
conda create --name bike_sharing-ds python=3.9

conda activate bike_sharing-ds

pip install -r requirements.txt

## Setup Environment - Shell/Terminal ⬇️
mkdir proyek_analisis_data_luthfi

cd proyek_analisis_data_luthfi

pipenv install

pipenv shell

pip install -r requirements.txt

## Run steamlit app 🏃🏻‍♂️‍➡️
streamlit run dashboard.py

## Hasil analisis 💁🏻‍♂️
- Conclution pertanyaan 1
  
Jumlah penyewa sepeda meningkat drastis dari musim semi hingga musim panas, dan menurun ketika memasukki musim dingin. Hal ini menunjukkan bahwa masyarakat cenderung ingin bersepeda pada saat memasukki musim semi hingga musim panas. Sedangkan ketika musim dingin, sedikit masyarakat yang ingin menyewa sepeda. Hal ini juga menunjukkan bahwa faktor cuaca sangat berpengaruh terhadap minat masyarakat dalam menggunakan sepeda

- Conclution pertanyaan 2
  
Jumlah penyewa sepeda paling banyak pada rentang bulan Mei hingga Oktober, terutama pada bulan Agustus. Hal ini dipengaruhi oleh faktor cuaca pada bulan tersebut. Masyarakat cenderung ingin menyewa sepeda pada saat memasukki musim semi hingga berakhirnya musim panas, pada bulan April hingga Oktober. Masyarakat cenderung menghindari menyewa sepeda pada masa peralihan dari musim panas ke musim dingin hingga berakhirnya musim dingin, dari bulan November hingga bulan Maret.
