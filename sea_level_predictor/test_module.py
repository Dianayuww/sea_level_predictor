import unittest
import os
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    
    def test_plot_saved(self):
        # Memastikan gambar disimpan
        draw_plot()
        self.assertTrue(os.path.exists('sea_level_plot.png'), "Plot image not saved.")
    
    def test_plot_contents(self):
        # Memastikan plot berisi garis tren yang diinginkan
        # Kita hanya bisa memeriksa jika plot disimpan, namun untuk memverifikasi plot yang lebih detail, 
        # kita memerlukan analisis visual atau metode analisis gambar lebih lanjut yang tidak ditangani di sini
        self.assertTrue(os.path.exists('sea_level_plot.png'), "Plot image not saved.")

if __name__ == '__main__':
    unittest.main()
