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

# Sidebar Menu
st.sidebar.markdown("### Proyek Analisis Data")
selected_option = st.sidebar.radio('Menu:', 
                                   ['Beranda', 'Pola Persewaan Sepeda', 'Pengaruh Jam dalam Sehari', 'Hubungan Kondisi Cuaca'])

# Main function
def main():
    bike_data = load_data()  # Memuat data
    if selected_option == 'Beranda':
        st.title('Analisis Frekuensi dan Visualisasi Data Persewaan Sepeda')
        st.write('Rifqi Khairullah Muhamad')
        st.write('ML-24')
        st.write('m200d4ky2358@bangkit.academy')
        st.write('Analisis data menyajikan tiga temuan utama terkait pola persewaan sepeda. Pertama, persewaan sepeda cenderung lebih tinggi pada hari-hari libur dibandingkan dengan hari kerja, menunjukkan adanya perbedaan pola persewaan antara kedua jenis hari tersebut. Kedua, terdapat pola penggunaan sepeda yang berkaitan dengan jam-jam sibuk pagi dan sore, dengan peningkatan signifikan pada jumlah penyewaan pada jam-jam awal pagi dan menjelang waktu pulang kerja. Ketiga, persewaan sepeda cenderung lebih tinggi pada kondisi cuaca yang cerah, diikuti oleh kondisi berawan, dan paling rendah pada kondisi hujan, menunjukkan bahwa kondisi cuaca mempengaruhi minat orang untuk menyewa sepeda. Temuan ini memberikan wawasan penting bagi pengelola penyewaan sepeda untuk memahami perilaku penyewa dan merencanakan strategi pemasaran yang tepat.')
    elif selected_option == 'Pola Persewaan Sepeda':
        plot_workingday_vs_holiday(bike_data)
    elif selected_option == 'Pengaruh Jam dalam Sehari':
        plot_hourly_rentals(bike_data)
    elif selected_option == 'Hubungan Kondisi Cuaca':
        plot_weather_condition(bike_data)

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
