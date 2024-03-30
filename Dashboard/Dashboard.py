import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menonaktifkan peringatan showPyplotGlobalUse
st.set_option('deprecation.showPyplotGlobalUse', False)

# Fungsi helper untuk membaca data
def load_data():
    bike_data = pd.read_csv('/workspaces/Proyek-Analisis-Data/Dashboard/all_data.csv')
    return bike_data

# Fungsi untuk menampilkan pola persewaan sepeda antara hari kerja dan hari libur
def plot_workingday_vs_holiday(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday_daily', y='cnt_daily', data=data)
    plt.title('Persewaan Sepeda antara Hari Kerja dan Hari Libur')
    plt.xlabel('Jenis Hari')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks([0, 1], ['Hari Libur', 'Hari Kerja'])
    st.pyplot()

# Fungsi untuk menampilkan pengaruh jam dalam sehari terhadap jumlah persewaan sepeda
def plot_hourly_rentals(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt_hourly', data=data[data['hr'] < 12], linestyle='dashed', color='blue', label='Pagi')
    sns.lineplot(x='hr', y='cnt_hourly', data=data[data['hr'] >= 12], color='orange', label='Sore')
    plt.title('Persewaan Sepeda Berdasarkan Jam dalam Sehari')
    plt.xlabel('Jam dalam Sehari')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(range(24))
    plt.legend(title='Pola Jam')
    plt.grid(True)
    st.pyplot()

# Fungsi untuk menampilkan hubungan kondisi cuaca dengan rata-rata persewaan sepeda
def plot_weather_condition(data):
    weather_summary = data.groupby('weathersit_daily')['cnt_daily'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit_daily', y='cnt_daily', data=weather_summary)
    plt.title('Rata-rata Persewaan Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Penyewaan')
    plt.xticks([0, 1, 2], ['Cerah', 'Berawan', 'Hujan'])
    st.pyplot()

# Fungsi untuk menampilkan distribusi frekuensi penyewaan sepeda
def plot_frequency_summary(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['cnt_daily'], bins=30, kde=True)
    plt.title('Distribusi Frekuensi Penyewaan Sepeda')
    plt.xlabel('Frekuensi')
    plt.ylabel('Jumlah Pelanggan')
    st.pyplot()

# Main function
def main():
    # Menyiapkan aplikasi Streamlit
    st.title('Analisis Frequency dan Visualisasi Data Persewaan Sepeda')

    # Memuat data
    bike_data = load_data()

    # Menampilkan grafik
    st.subheader('Grafik Pola Persewaan Sepeda antara Hari Kerja dan Hari Libur')
    plot_workingday_vs_holiday(bike_data)

    st.subheader('Grafik Pengaruh Jam dalam Sehari terhadap Jumlah Persewaan Sepeda')
    plot_hourly_rentals(bike_data)

    st.subheader('Grafik Hubungan Kondisi Cuaca dengan Rata-rata Persewaan Sepeda')
    plot_weather_condition(bike_data)

    st.subheader('Grafik Distribusi Frekuensi Penyewaan Sepeda')
    plot_frequency_summary(bike_data)

# Menjalankan aplikasi
if __name__ == '_main_':
    main()