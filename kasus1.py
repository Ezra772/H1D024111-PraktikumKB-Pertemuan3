import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001, 100), 'harga')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1000), 'profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'stok')

barang_terjual['Rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['Sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['Tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])

permintaan['Rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['Sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['Tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

harga['Murah'] = fuzz.trimf(harga.universe, [0, 0, 30000])
harga['Sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 80000])
harga['Mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000])

profit['Rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['Sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 3000000])
profit['Tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

stok['Sedang'] = fuzz.trimf(stok.universe, [100, 500, 900])
stok['Banyak'] = fuzz.trimf(stok.universe, [600, 1000, 1000])

aturan1 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Tinggi'], stok['Banyak'])
aturan2 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan3 = ctrl.Rule(barang_terjual['Tinggi'] & permintaan['Sedang'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan4 = ctrl.Rule(barang_terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan5 = ctrl.Rule(barang_terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Tinggi'], stok['Banyak'])
aturan6 = ctrl.Rule(barang_terjual['Rendah'] & permintaan['Rendah'] & harga['Sedang'] & profit['Sedang'], stok['Sedang'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)

system.input['barang_terjual'] = 80
system.input['permintaan'] = 255
system.input['harga'] = 25000
system.input['profit'] = 3500000

system.compute()
hasil_stok = system.output['stok']

print(f"Barang Terjual = 80")
print(f"Permintaan = 255")
print(f"Harga per Item = Rp 25.000")
print(f"Profit = Rp 3.500.000")
print("-" * 30)
print(f"Hasil Prediksi Stok Makanan Adalah: {hasil_stok:.2f} unit")

stok.view(sim=system)
input("TEKAN ENTER untuk melanjutkan/menutup...")
