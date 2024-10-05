# import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')

hour_clean = pd.read_csv('hour_clean.csv')
month_usage_clean = pd.read_csv('month_usage_clean.csv')
season_usage_clean = pd.read_csv('season_usage_clean.csv')

st.title('Analisis Data Musiman dan Bulanan Penyewaan Sepeda: Tren dan Faktor Penentu')

st.write('''
    Selamat datang di **"Analisis Data Musiman dan Bulanan Penyewaan Sepeda: Tren dan Faktor Penentu"**. 
    Pada web ini, kami menyajikan analisis mendalam mengenai pola penggunaan sepeda berdasarkan musim dan bulan, serta mengeksplorasi faktor-faktor yang mempengaruhi tren tersebut. 
    Dengan memanfaatkan data historis, saya akan menjawab dua pertanyaan utama : Pada musim apa jumlah penyewa sepeda paling banyak? dan Pada bulan apa jumlah penyewa sepeda paling banyak dan apa faktor penyebabnya?
''')

pilih_pertanyaan = st.selectbox(
    label='Pilihlah pertanyaan analisis yang ingin anda ketahui jawabannya berikut ini',
    options=[
        'Pada musim apa jumlah penyewa sepeda paling banyak?', 
        'Pada bulan apa jumlah penyewa sepeda paling banyak dan apa faktor penyebabnya?'
    ]
)

if pilih_pertanyaan == 'Pada bulan apa jumlah penyewa sepeda paling banyak dan apa faktor penyebabnya?':
    st.subheader("Analisis Penyewaan Sepeda Berdasarkan Bulan")
    
    st.write('Tabel 1 : Data Penyewaan Sepeda Berdasarkan Bulan')
    st.dataframe(data=month_usage_clean.reset_index(drop=True), width=500, height=150)
    
    st.write('Grafik Visualisasi Tabel 1')
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(5, 3))
        plt.plot(month_usage_clean['mnth'], month_usage_clean['cnt'], marker='o', color='blue')
        plt.title('Jumlah penyewa Berdasarkan Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah penyewa')
        plt.xticks(month_usage_clean['mnth'])  # Show months as labels
        plt.grid()
        st.pyplot(plt)
    
    with col2:
        plt.figure(figsize=(5, 3))
        plt.bar(month_usage_clean['mnth'], month_usage_clean['cnt'], color='green')
        plt.title('Jumlah Penyewa per Bulan (Bar Chart)')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Penyewa')
        plt.xticks(month_usage_clean['mnth'])
        plt.grid()
        st.pyplot(plt)
        
    st.write("""
             Berdasarkan visualisasi pada grafik di atas, diperoleh insight berupa :
             - Bulan dengan jumlah penyewa sepeda paling banyak adalah bulan Agustus.
             - Bulan dengan jumlah penyewa sepeda paling sedikit adalah bulan Januari.
             - Jumlah penyewa sepeda mengalami uptren dari bulan Januari hingga bulan Mei.
             - Jumlah penyewa sepeda mengalami sideways dari bulan Mei hingga Oktober.
             - Jumlah penyewa sepeda mengalami downtren dari bulan Oktober hingga Desember.
             """)
    st.subheader('Analisis Cuaca sebagai Faktor Penyebab Minat Penyewaan Sepeda')
    st.write('Tabel 2 : Data Catatan Cuaca')
    st.dataframe(data=hour_clean.reset_index(drop=True), width=500, height=150)
    st.write("""             
             Berdasarkan Tabel 2, makna setiap kolom :
             - dteday : menyatakan tanggal
             - season : menyatakan musim (1 -> semi, 2 -> panas, 3 -> gugur, 4 -> dingin)
             - mnth : menyatakan bulan
             - weathersit : menyatakan kondisi cuaca
             - temp : menyatakan suhu dalam celsius
             - windspeed : menyatakan kecepaan udara
             - cnt : menyatakan banyaknya penyewa sepeda pada saat itu
             """)
    
    st.write('Tabel 3 : Korelasi Kondisi Cuaca terhadap Penyewa Sepeda dari Tabel 2')
    correlation_table = hour_clean[['mnth', 'cnt', 'temp', 'weathersit', 'windspeed','season']].corr()
    st.dataframe(data=correlation_table, width=500, height=150)
    st.write('''
             Berdasarkan Tabel 3, diperoleh insight :
             - Terdapat korelasi positif yang kuat antara jumlah penyewaan (cnt) dan suhu (temp), yang menunjukkan bahwa saat suhu meningkat, jumlah penyewaan juga cenderung meningkat.
             - Terdapat korelasi negatif antara jumlah penyewaan (cnt) dan kondisi cuaca (weathersit). Ini menunjukkan bahwa kondisi cuaca yang buruk cenderung mengurangi jumlah penyewaan.
             - Terdapat korelasi negatif antara jumlah penyewaan (cnt) dan kecepatan angin (windspeed). Ini menunjukkan saat kecepatan angin meningkat, jumlah penyewaan cenderung menurun.
             - Terdapat korelasi positif antara jumlah penyewaan (cnt) dan musim (season). Ini menunjukkan bahwa musim tertentu cenderung meningkatkan jumlah penyewaan.
             ''')
    
    st.subheader('Kesimpulan')
    st.write('''Jumlah penyewa sepeda paling banyak pada rentang bulan Mei hingga Oktober, terutama pada bulan Agustus. Hal ini dipengaruhi oleh faktor cuaca pada bulan tersebut.
             Masyarakat cenderung ingin menyewa sepeda pada saat memasukki musim semi hingga berakhirnya musim panas, pada bulan April hingga Oktober.
             Masyarakat cenderung menghindari menyewa sepeda pada masa peralihan dari musim panas ke musim dingin hingga berakhirnya musim dingin, dari bulan November hingga bulan Maret.
             ''')
    
    
elif pilih_pertanyaan == 'Pada musim apa jumlah penyewa sepeda paling banyak?':
    st.subheader("Analisis Penyewaan Sepeda Berdasarkan Musim")
    
    st.write('Tabel 1 : Data penyewaan Sepeda berdasarkan Musim')
    st.dataframe(data=season_usage_clean.reset_index(drop=True), width=500, height=150)
    
    st.write('Grafik Visualisasi Tabel 1')
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(5, 3))
        plt.plot(season_usage_clean['season'], season_usage_clean['cnt'], marker='o', color='red')
        plt.title('Jumlah penyewa Berdasarkan Musim')
        plt.xlabel('Musim')
        plt.ylabel('Jumlah penyewa')
        plt.xticks(season_usage_clean['season'])  # Show seasons as labels
        plt.grid()
        st.pyplot(plt)
    
    with col2:
        plt.figure(figsize=(5, 3))
        plt.bar(season_usage_clean['season'], season_usage_clean['cnt'], color='purple')
        plt.title('Jumlah penyewa per Musim (Bar Chart)')
        plt.xlabel('Musim')
        plt.ylabel('Jumlah penyewa')
        plt.xticks(season_usage_clean['season'])
        plt.grid()
        st.pyplot(plt)
        
    st.write("""
             Berdasarkan visualisasi pada grafik di atas, diperoleh insight berupa :
             - Musim dengan jumlah penyewa sepeda paling banyak adalah musim ke-3 yaitu musim panas.
             - Musim dengan jumlah penyewa sepeda paling sedikit adalah musim ke-1 yaitu musim semi.
             - Jumlah penyewa sepeda mengalami uptren dari musim semi hingga musim panas.
             - Jumlah penyewa sepeda mengalami downtren dari musim panas ke musim dingin.
             """)
    st.subheader("Kesimpulan")
    st.write('''Jumlah penyewa sepeda meningkat drastis dari musim semi hingga musim panas, dan menurun ketika memasukki musim dingin. Hal ini menunjukkan bahwa
             masyarakat cenderung ingin bersepeda pada saat memasukki musim semi hingga musim panas. Sedangkan ketika musim dingin, sedikit masyarakat yang ingin menyewa sepeda.
             Hal ini juga menunjukkan bahwa faktor cuaca sangat berpengaruh terhadap minat masyarakat dalam menggunakan sepeda''')
