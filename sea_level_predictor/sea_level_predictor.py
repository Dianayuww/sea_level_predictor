import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Fungsi untuk memprediksi dan memplot data
def draw_plot():
    # Membaca data dari CSV
    data = pd.read_csv('epa-sea-level.csv')

    # Membuat plot scatter
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Garis tren pertama (seluruh data)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Untuk tahun 1880-2050
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best fit line (1880-2050)')

    # Garis tren kedua (data dari tahun 2000 hingga terakhir)
    data_recent = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, [slope_recent * year + intercept_recent for year in years_extended], label='Best fit line (2000-2050)', color='red')

    # Menambahkan label dan judul
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Menyimpan gambar
    plt.savefig('sea_level_plot.png')
    plt.show()
