import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import statsmodels.formula.api as sm 
sns.set(style='dark')

# Load dataset yang sudah diproses dan disimpan sebelumnya
all_data = pd.read_csv("all_data.csv") 


# Ubah tipe data 'dteday' menjadi datetime
all_data['dteday'] = pd.to_datetime(all_data['dteday'])


# Ubah nilai numerik pada kolom 'season' menjadi label musim
all_data['season'] = all_data['season'].map({1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'})

# Ubah nilai numerik pada kolom 'weathersit' menjadi label cuaca
all_data['weathersit'] = all_data['weathersit'].map({1: 'Cerah', 2: 'Berkabut/Berawan', 3: 'Hujan Ringan/Bersalju', 4: 'Hujan Lebat/Badai'})

# Ubah nilai numerik pada kolom 'weekday' menjadi label hari
all_data['weekday'] = all_data['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})

# Ubah nilai numerik pada kolom 'mnth' menjadi label bulan
all_data['mnth'] = all_data['mnth'].map({1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'})

# Ubah nilai numerik pada kolom 'yr' menjadi label tahun
all_data['yr'] = all_data['yr'].map({0: 2011, 1: 2012})


# Judul dashboard
st.title('Dashboard Penyewaan Sepeda')
# headline
st.markdown("Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan faktor cuaca dan waktu.")


st.sidebar.header('Filter data berdasarkan:')

# Filter berdasarkan cuaca
selected_weathersit = st.sidebar.selectbox('Pilih Cuaca', all_data['weathersit'].unique())

# Filter berdasarkan hari
selected_weekday = st.sidebar.selectbox('Pilih Hari', all_data['weekday'].unique())

# Filter berdasarkan bulan
selected_mnth = st.sidebar.selectbox('Pilih Bulan', all_data['mnth'].unique())

# Filter data berdasarkan pilihan filter
filtered_data = all_data[(all_data['weathersit'] == selected_weathersit) &
                      (all_data['weekday'] == selected_weekday) &
                      (all_data['mnth'] == selected_mnth)]

# Visualisasi data

# Grafik Bar
# Assuming you have Streamlit widgets for filtering
st.subheader('Grafik Bar Jumlah Penyewaan berdasarkan Hari, Bulan, dan Cuaca yang difilter')
fig, ax = plt.subplots(figsize=(10, 6))
plt.title(f'Grafik Bar Jumlah Penyewaan pada hari {selected_weekday}, bulan {selected_mnth}, dan cuaca {selected_weathersit}')
sns.barplot(x='dteday', y='cnt', data=filtered_data, ax=ax)
plt.xlabel('Tanggal Penyewaan (dteday)', labelpad=17)
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(fig)


# Scatter plot untuk melihat korelasi antara suhu dan jumlah penyewaan
st.subheader("Korelasi antara Suhu dan Jumlah Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['temp'], filtered_data['cnt'], alpha=0.5)
plt.title('Korelasi antara Suhu dan Jumlah Penyewaan Sepeda')
plt.xlabel('Suhu (temp)', labelpad=10)
plt.ylabel('Jumlah Penyewaan (cnt)')
plt.grid(True)
st.pyplot(plt)

# Insight
st.subheader("Insight")
st.write("- Terdapat korelasi positif yang kuat antara suhu dan jumlah penyewaan sepeda. Semakin tinggi suhu, semakin banyak orang yang menyewa sepeda.")


# Scatter plot untuk melihat korelasi antara suhu dan jumlah penyewaan
st.subheader("Distribusi Jumlah Penyewaan Sepeda Bulanan")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='mnth', y='cnt', data=filtered_data)
plt.title('Distribusi Jumlah Penyewaan Sepeda Bulanan')
plt.xlabel('Bulan (mnth)')
plt.ylabel('Jumlah Penyewaan (cnt)')
plt.grid(True)
st.pyplot(plt)

# Insight berdasarkan bulan
if selected_mnth == 'Januari':
    st.write("- **Januari:** Jumlah penyewaan biasanya rendah karena cuaca dingin. Pertimbangkan untuk menawarkan diskon atau promo khusus.")
elif selected_mnth == 'Februari':
    st.write("- **Februari:** Jumlah penyewaan masih relatif rendah, tetapi mungkin mulai meningkat seiring dengan mendekatnya musim semi. Perhatikan tren cuaca dan sesuaikan stok sepeda.")
elif selected_mnth == 'Maret':
    st.write("- **Maret:** Jumlah penyewaan cenderung meningkat seiring dengan datangnya musim semi dan cuaca yang lebih hangat. Pastikan ketersediaan sepeda yang cukup.")
elif selected_mnth == 'April':
    st.write("- **April:** Jumlah penyewaan biasanya tinggi, terutama pada hari-hari cerah dengan suhu yang nyaman. Pertimbangkan untuk menambah stok sepeda dan memperluas area layanan.")
elif selected_mnth == 'Mei':
    st.write("- **Mei:** Jumlah penyewaan tetap tinggi, terutama pada akhir pekan dan hari libur. Pastikan ketersediaan sepeda yang cukup dan lakukan perawatan rutin.")
elif selected_mnth == 'Juni':
    st.write("- **Juni:** Jumlah penyewaan biasanya tinggi, terutama pada musim panas. Pastikan ketersediaan sepeda yang cukup dan perhatikan kondisi cuaca.")
elif selected_mnth == 'Juli':
    st.write("- **Juli:** Jumlah penyewaan biasanya tinggi, terutama pada musim panas. Pastikan ketersediaan sepeda yang cukup dan perhatikan kondisi cuaca.")
elif selected_mnth == 'Agustus':
    st.write("- **Agustus:** Jumlah penyewaan biasanya tinggi, terutama pada musim panas. Pastikan ketersediaan sepeda yang cukup dan perhatikan kondisi cuaca.")
elif selected_mnth == 'September':
    st.write("- **September:** Jumlah penyewaan mulai menurun seiring dengan berakhirnya musim panas. Pertimbangkan untuk mengurangi stok sepeda dan fokus pada promosi untuk menarik pengguna.")
elif selected_mnth == 'Oktober':
    st.write("- **Oktober:** Jumlah penyewaan cenderung menurun seiring dengan penurunan suhu. Perhatikan tren cuaca dan sesuaikan stok sepeda.")
elif selected_mnth == 'November':
    st.write("- **November:** Jumlah penyewaan biasanya rendah karena cuaca dingin dan kondisi jalan yang mungkin licin. Pastikan sepeda dalam kondisi prima dan pertimbangkan untuk menawarkan diskon atau promo khusus.")
elif selected_mnth == 'Desember':
    st.write("- **Desember:** Jumlah penyewaan biasanya rendah karena cuaca dingin dan musim liburan. Pastikan sepeda dalam kondisi prima dan pertimbangkan untuk menawarkan promo khusus untuk acara liburan.")


# Scatter plot untuk melihat korelasi antara suhu dan jumlah penyewaan
st.subheader("Distribusi Jumlah Penyewaan Sepeda Harian")
plt.figure(figsize=(10, 6))
sns.boxplot(x='weekday', y='cnt', data=filtered_data)
plt.title('Distribusi Jumlah Penyewaan Sepeda Harian')
plt.xlabel('Hari (weekday)')
plt.ylabel('Jumlah Penyewaan (cnt)')
plt.grid(True)
st.pyplot(plt)


if selected_weekday in [0, 6]:  # Sabtu dan Minggu (0 dan 6)
    st.write("- Akhir pekan: Jumlah penyewaan cenderung lebih tinggi, terutama untuk tujuan rekreasi.")
else:  # Senin - Jumat (1 - 5)
    st.write("- Hari kerja: Jumlah penyewaan cenderung lebih tinggi pada jam sibuk, menunjukkan penggunaan untuk aktivitas komuter.")

# Box plot untuk melihat distribusi penyewaan berdasarkan cuaca
st.subheader("Distribusi Penyewaan Sepeda berdasarkan Cuaca")
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=filtered_data)
plt.title('Distribusi Penyewaan Sepeda berdasarkan Cuaca')
plt.xlabel('Cuaca (weathersit)')
plt.ylabel('Jumlah Penyewaan (cnt)')
plt.grid(True)
st.pyplot(plt)

# Insight berdasarkan cuaca
if selected_weathersit == 'Cerah':
    st.write("- **Cuaca Cerah:** Kondisi ideal untuk bersepeda, jumlah penyewaan cenderung tinggi. Pastikan ketersediaan sepeda yang cukup di lokasi-lokasi strategis.")
elif selected_weathersit == 'Berkabut/Berawan':
    st.write("- **Cuaca Berkabut/Berawan:** Jumlah penyewaan mungkin sedikit menurun, tetapi masih cukup tinggi. Perhatikan kondisi jalan dan pastikan keamanan pengguna.")
elif selected_weathersit == 'Hujan Ringan/Bersalju':
    st.write("- **Cuaca Hujan Ringan/Bersalju:** Jumlah penyewaan akan menurun secara signifikan. Pastikan sepeda dilengkapi dengan aksesori pelindung dan pertimbangkan untuk menawarkan promo khusus.")
elif selected_weathersit == 'Hujan Lebat/Badai':
    st.write("- **Cuaca Hujan Lebat/Badai:** Jumlah penyewaan akan sangat rendah. Pastikan keamanan pengguna dan pertimbangkan untuk menutup layanan sementara jika kondisi cuaca berbahaya.")

# Histogram untuk melihat distribusi jumlah penyewaan
st.subheader("Distribusi Jumlah Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['cnt'], bins=20)
plt.title('Distribusi Jumlah Penyewaan Sepeda')
plt.xlabel('Jumlah Penyewaan (cnt)')
plt.ylabel('Frekuensi')
plt.grid(True)
st.pyplot(plt)


# --- Layout menggunakan st.columns ---
# Bagi layar menjadi 2 kolom dan simpan variabel col1, col2
col1, col2 = st.columns(2)  



# Definisikan fungsi create_daily_rentals_df
def create_daily_rentals_df(df):
    """
    Fungsi ini membuat DataFrame baru yang berisi data penyewaan harian yang telah diagregasi.
    """
    daily_rentals_df = df.groupby('dteday')['cnt'].sum().reset_index()
    daily_rentals_df = daily_rentals_df.rename(columns={'cnt': 'total_rentals'})
    return daily_rentals_df

# Definisikan fungsi create_sum_rentals_by_weather_df
def create_sum_rentals_by_weather_df(df):
    """
    Fungsi ini membuat DataFrame baru yang berisi total penyewaan berdasarkan kondisi cuaca.
    """
    sum_rentals_by_weather_df = df.groupby('weathersit')['cnt'].sum().reset_index()
    sum_rentals_by_weather_df = sum_rentals_by_weather_df.rename(columns={'cnt': 'total_rentals'})
    return sum_rentals_by_weather_df

# Definisikan fungsi create_byseason_df
def create_byseason_df(df):
    """
    Fungsi ini membuat DataFrame baru yang berisi total penyewaan berdasarkan musim.
    """
    byseason_df = df.groupby('season')['cnt'].sum().reset_index()
    byseason_df = byseason_df.rename(columns={'cnt': 'total_rentals'})
    return byseason_df

def create_byday_df(df):
    """
    Fungsi ini membuat DataFrame baru yang berisi total penyewaan berdasarkan hari.
    """
    byday_df = df.groupby('weekday')['cnt'].sum().reset_index()
    byday_df = byday_df.rename(columns={'cnt': 'total_rentals'})
    return byday_df

def create_bymnth_df(df):
    """
    Fungsi ini membuat DataFrame baru yang berisi total penyewaan berdasarkan hari.
    """
    bymnth_df = df.groupby('mnth')['cnt'].sum().reset_index()
    bymnth_df = bymnth_df.rename(columns={'cnt': 'total_rentals'})
    return bymnth_df

# Panggil fungsi helper untuk menyiapkan data
daily_rentals_df = create_daily_rentals_df(all_data)
sum_rentals_by_weather_df = create_sum_rentals_by_weather_df(all_data)
byseason_df = create_byseason_df(all_data)
byday_df = create_byday_df(all_data)
bymnth_df = create_bymnth_df(all_data)
# ... (panggil fungsi lainnya)

# Tampilkan data dan visualisasi di dashboard
st.header('Jumlah Penyewaan Harian')
st.line_chart(daily_rentals_df.set_index('dteday')['total_rentals'])
st.write("- Jumlah penyewaan sepeda harian selalu meningkat di awal tahun dan mengalami penurunan di akhir tahun")

st.header('Jumlah Penyewaan berdasarkan Cuaca')
st.bar_chart(sum_rentals_by_weather_df.set_index('weathersit')['total_rentals'])
st.write("- Terlihat bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada cuaca cerah (weathersit = 1) dan menurun pada cuaca buruk (weathersit = 3 atau 4).")

st.header('Jumlah Penyewaan berdasarkan Musim')
st.bar_chart(byseason_df.set_index('season')['total_rentals'])
st.write("- Terdapat pola musiman dalam penyewaan sepeda, dengan peningkatan di musim panas dan penurunan di musim dingin. Rata-rata total penyewaan (cnt) lebih tinggi di musim panas dibandingkan musim dingin, ini menunjukkan bahwa orang cenderung lebih sering menyewa sepeda di musim panas.")

st.header('Jumlah Penyewaan berdasarkan Hari')
st.bar_chart(byday_df.set_index('weekday')['total_rentals'])
st.write("- Total penyewaan sepeda (cnt) lebih tinggi di hari kerja (Senin-Jumat) dibandingkan akhir pekan (Sabtu-Minggu), ini menunjukkan bahwa orang cenderung lebih sering menyewa sepeda untuk aktivitas komuter atau bekerja.")

st.header('Jumlah Penyewaan berdasarkan Bulan')
st.bar_chart(bymnth_df.set_index('mnth')['total_rentals'])
st.write("""
        **Pola Musiman:**
          - Terlihat adanya pola musiman yang jelas dalam data. Jumlah penyewaan sepeda cenderung meningkat secara signifikan di bulan-bulan musim panas (Juni, Juli, Agustus) dan menurun di bulan-bulan musim dingin (Desember, Januari, Februari).
          -  Pola musiman ini kemungkinan besar dipengaruhi oleh faktor cuaca. Orang cenderung lebih memilih untuk bersepeda saat cuaca hangat dan cerah, dibandingkan saat cuaca dingin dan tidak bersahabat.
        
        **Bulan dengan Penyewaan Tertinggi:**
         - Bulan dengan jumlah penyewaan sepeda tertinggi adalah bulan Juni, Juli, Agustus dan September.
         - Hal ini menunjukkan bahwa bulan-bulan musim panas merupakan periode puncak untuk bisnis penyewaan sepeda.
        
        **Bulan dengan Penyewaan Terendah:**
          + Bulan dengan jumlah penyewaan sepeda terendah adalah bulan Januari dan Februari.
          + Hal ini menunjukkan bahwa permintaan penyewaan sepeda menurun drastis di musim dingin.       
""")


# --- Fungsi Helper ---
def create_daily_rentals_df(df):
    daily_rentals_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum",  # Total penyewaan per hari
        "casual": "sum", # Total pengguna casual per hari
        "registered": "sum" # Total pengguna registered per hari
    })
    daily_rentals_df = daily_rentals_df.reset_index()
    daily_rentals_df.rename(columns={
        "cnt": "total_rentals",
        "casual": "casual_users",
        "registered": "registered_users"
    }, inplace=True)
    
    return daily_rentals_df


def create_sum_rentals_by_weather_df(df):
    sum_rentals_by_weather_df = df.groupby("weathersit").cnt.sum().sort_values(ascending=False).reset_index()
    return sum_rentals_by_weather_df

def create_byseason_df(df):
    byseason_df = df.groupby(by="season").cnt.sum().reset_index()
    byseason_df.rename(columns={
        "cnt": "total_rentals"
    }, inplace=True)
    return byseason_df


###

st.sidebar.header('Tampilkan data berdasarkan:')
selected_feature = st.sidebar.selectbox('Pilih Fitur', ['cnt', 'temp', 'hum', 'windspeed'])

# Menampilkan histogram dari fitur yang dipilih
st.header('Histogram ' + selected_feature)
fig, ax = plt.subplots()
ax.hist(all_data[selected_feature], bins=20)
st.pyplot(fig)

# --- Layout menggunakan st.columns dan st.container ---
col1, col2 = st.columns(2)

# --- Histogram di kolom pertama ---
with col1:
    st.subheader('Histogram Jumlah Penyewaan')
    fig, ax = plt.subplots()
    ax.hist(all_data['cnt'], bins=20)
    ax.set_xlabel('Jumlah Penyewaan (cnt)')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    st.markdown("**Insight:** Distribusi jumlah penyewaan sepeda cenderung menceng (skewed) ke kanan, menunjukkan bahwa terdapat beberapa hari dengan jumlah penyewaan yang sangat tinggi.")

# --- Scatter plot di kolom kedua ---
with col2:
    st.subheader('Scatter Plot Suhu vs. Jumlah Penyewaan')
    fig, ax = plt.subplots()
    ax.scatter(all_data['temp'], all_data['cnt'], alpha=0.5)
    ax.set_xlabel('Suhu (temp)')
    ax.set_ylabel('Jumlah Penyewaan (cnt)')
    st.pyplot(fig)
    st.markdown("**Insight:** Terdapat korelasi positif antara suhu dan jumlah penyewaan sepeda. Semakin tinggi suhu, semakin banyak orang yang menyewa sepeda.")

# --- Box plot di dalam expander ---
with st.expander("Box Plot Penyewaan berdasarkan Cuaca"):
    fig, ax = plt.subplots()
    sns.boxplot(x='weathersit', y='cnt', data=all_data, ax=ax)
    ax.set_xlabel('Cuaca (weathersit)')
    ax.set_ylabel('Jumlah Penyewaan (cnt)')
    st.pyplot(fig)
    st.markdown("**Insight:** Jumlah penyewaan sepeda cenderung lebih tinggi pada cuaca cerah (weathersit = 1) dan menurun pada cuaca buruk (weathersit = 3 atau 4).")

# --- Analisis Regresi ---
with st.expander("Analisis Regresi"):
    model = sm.ols(formula='cnt ~ temp + hum + windspeed + weekday + mnth + season', data=all_data)
    results = model.fit()
    st.write(results.summary())
    st.markdown("""
    **Insight:**
    - Variabel `temp`, `hum`, `windspeed`, `weekday`, `mnth`, dan `season` memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda.
    - Suhu (`temp`) memiliki pengaruh positif, artinya suhu yang lebih tinggi cenderung meningkatkan penyewaan.
    - Kelembapan (`hum`) dan Kecepatan Angin (`windspeed`) memiliki pengaruh negatif, artinya kelembapan dan kecepatan angin yang tinggi cenderung menurunkan total penyewaan sepeda""")


# --- Anomali Detection ---
with st.expander("Anomali Detection"):
    # Deteksi anomali menggunakan IQR untuk kolom 'cnt'
    Q1 = all_data['cnt'].quantile(0.25)
    Q3 = all_data['cnt'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Data anomali (outliers)
    outliers = all_data[(all_data['cnt'] < lower_bound) | (all_data['cnt'] > upper_bound)]
    
    # Menampilkan outlier pada tabel
    st.write("Data Anomali (cnt):")
    st.write(outliers)

    # Menampilkan insight
    st.markdown("""
    **Insight:**
    - Data anomali menunjukkan adanya penyewaan sepeda yang tidak biasa, 
      misalnya jumlah penyewaan yang sangat tinggi atau rendah di luar pola normal.
    - Anomali ini dapat disebabkan oleh berbagai faktor, seperti event khusus, 
      cuaca ekstrem, hari libur, atau error data.
    - Perlu dilakukan investigasi lebih lanjut untuk memahami penyebab anomali dan 
      mengambil tindakan yang tepat.
    - Dari hasil Anomali Detection tidak ditemukan keaneahan atau anomali data, 
      yang menunjukan bahwa tidak ada kejadian aneh pada saat pengambilan data tersebut.
    """)
