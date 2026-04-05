import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

kejelasan_informasi['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi['Cukup Memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100])

kejelasan_persyaratan['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan['Cukup Memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])

kemampuan_petugas['Tidak Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas['Cukup Memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])

ketersediaan_sarpras['Tidak Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [0, 0, 60, 75])
ketersediaan_sarpras['Cukup Memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras['Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [75, 90, 100, 100])

kepuasan['Tidak Memuaskan'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 100])
kepuasan['Kurang Memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 100, 175])
kepuasan['Cukup Memuaskan'] = fuzz.trimf(kepuasan.universe, [100, 175, 275])
kepuasan['Memuaskan'] = fuzz.trimf(kepuasan.universe, [250, 325, 400])
kepuasan['Sangat Memuaskan'] = fuzz.trapmf(kepuasan.universe, [325, 350, 400, 400])

KI = kejelasan_informasi
KP = kejelasan_persyaratan
KemP = kemampuan_petugas
KS = ketersediaan_sarpras
TM = 'Tidak Memuaskan'
CM = 'Cukup Memuaskan'
M = 'Memuaskan'

aturan1  = ctrl.Rule(KI[TM] & KP[TM] & KemP[TM] & KS[TM], kepuasan['Kurang Memuaskan'])
aturan2  = ctrl.Rule(KI[TM] & KP[TM] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan3  = ctrl.Rule(KI[TM] & KP[TM] & KemP[TM] & KS[M], kepuasan['Cukup Memuaskan'])
aturan4  = ctrl.Rule(KI[TM] & KP[TM] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan5  = ctrl.Rule(KI[TM] & KP[TM] & KemP[CM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan6  = ctrl.Rule(KI[TM] & KP[TM] & KemP[CM] & KS[M], kepuasan['Cukup Memuaskan'])
aturan7  = ctrl.Rule(KI[TM] & KP[TM] & KemP[M] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan8  = ctrl.Rule(KI[TM] & KP[TM] & KemP[M] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan9  = ctrl.Rule(KI[TM] & KP[TM] & KemP[M] & KS[M], kepuasan['Memuaskan'])
aturan10 = ctrl.Rule(KI[TM] & KP[CM] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan11 = ctrl.Rule(KI[TM] & KP[CM] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan12 = ctrl.Rule(KI[TM] & KP[CM] & KemP[TM] & KS[M], kepuasan['Cukup Memuaskan'])
aturan13 = ctrl.Rule(KI[TM] & KP[CM] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan14 = ctrl.Rule(KI[TM] & KP[CM] & KemP[CM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan15 = ctrl.Rule(KI[TM] & KP[CM] & KemP[CM] & KS[M], kepuasan['Memuaskan'])
aturan16 = ctrl.Rule(KI[TM] & KP[CM] & KemP[M] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan17 = ctrl.Rule(KI[TM] & KP[CM] & KemP[M] & KS[CM], kepuasan['Memuaskan'])
aturan18 = ctrl.Rule(KI[TM] & KP[CM] & KemP[M] & KS[M], kepuasan['Memuaskan'])
aturan19 = ctrl.Rule(KI[TM] & KP[M] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan20 = ctrl.Rule(KI[TM] & KP[M] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan21 = ctrl.Rule(KI[TM] & KP[M] & KemP[TM] & KS[M], kepuasan['Memuaskan'])
aturan22 = ctrl.Rule(KI[TM] & KP[M] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan23 = ctrl.Rule(KI[TM] & KP[M] & KemP[CM] & KS[CM], kepuasan['Memuaskan'])
aturan24 = ctrl.Rule(KI[TM] & KP[M] & KemP[CM] & KS[M], kepuasan['Memuaskan'])
aturan25 = ctrl.Rule(KI[TM] & KP[M] & KemP[M] & KS[TM], kepuasan['Memuaskan'])
aturan26 = ctrl.Rule(KI[TM] & KP[M] & KemP[M] & KS[CM], kepuasan['Memuaskan'])
aturan27 = ctrl.Rule(KI[TM] & KP[M] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])
aturan28 = ctrl.Rule(KI[CM] & KP[TM] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan29 = ctrl.Rule(KI[CM] & KP[TM] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan30 = ctrl.Rule(KI[CM] & KP[TM] & KemP[TM] & KS[M], kepuasan['Cukup Memuaskan'])
aturan31 = ctrl.Rule(KI[CM] & KP[TM] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan32 = ctrl.Rule(KI[CM] & KP[TM] & KemP[CM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan33 = ctrl.Rule(KI[CM] & KP[TM] & KemP[CM] & KS[M], kepuasan['Memuaskan'])
aturan34 = ctrl.Rule(KI[CM] & KP[TM] & KemP[M] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan35 = ctrl.Rule(KI[CM] & KP[TM] & KemP[M] & KS[CM], kepuasan['Memuaskan'])
aturan36 = ctrl.Rule(KI[CM] & KP[TM] & KemP[M] & KS[M], kepuasan['Memuaskan'])
aturan37 = ctrl.Rule(KI[CM] & KP[CM] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan38 = ctrl.Rule(KI[CM] & KP[CM] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan39 = ctrl.Rule(KI[CM] & KP[CM] & KemP[TM] & KS[M], kepuasan['Memuaskan'])
aturan40 = ctrl.Rule(KI[CM] & KP[CM] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan41 = ctrl.Rule(KI[CM] & KP[CM] & KemP[CM] & KS[CM], kepuasan['Memuaskan'])
aturan42 = ctrl.Rule(KI[CM] & KP[CM] & KemP[CM] & KS[M], kepuasan['Memuaskan'])
aturan43 = ctrl.Rule(KI[CM] & KP[CM] & KemP[M] & KS[TM], kepuasan['Memuaskan'])
aturan44 = ctrl.Rule(KI[CM] & KP[CM] & KemP[M] & KS[CM], kepuasan['Memuaskan'])
aturan45 = ctrl.Rule(KI[CM] & KP[CM] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])
aturan46 = ctrl.Rule(KI[CM] & KP[M] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan47 = ctrl.Rule(KI[CM] & KP[M] & KemP[TM] & KS[CM], kepuasan['Memuaskan'])
aturan48 = ctrl.Rule(KI[CM] & KP[M] & KemP[TM] & KS[M], kepuasan['Memuaskan'])
aturan49 = ctrl.Rule(KI[CM] & KP[M] & KemP[CM] & KS[TM], kepuasan['Memuaskan'])
aturan50 = ctrl.Rule(KI[CM] & KP[M] & KemP[CM] & KS[CM], kepuasan['Memuaskan'])
aturan51 = ctrl.Rule(KI[CM] & KP[M] & KemP[CM] & KS[M], kepuasan['Sangat Memuaskan'])
aturan52 = ctrl.Rule(KI[CM] & KP[M] & KemP[M] & KS[TM], kepuasan['Memuaskan'])
aturan53 = ctrl.Rule(KI[CM] & KP[M] & KemP[M] & KS[CM], kepuasan['Sangat Memuaskan'])
aturan54 = ctrl.Rule(KI[CM] & KP[M] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])
aturan55 = ctrl.Rule(KI[M] & KP[TM] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan56 = ctrl.Rule(KI[M] & KP[TM] & KemP[TM] & KS[CM], kepuasan['Cukup Memuaskan'])
aturan57 = ctrl.Rule(KI[M] & KP[TM] & KemP[TM] & KS[M], kepuasan['Memuaskan'])
aturan58 = ctrl.Rule(KI[M] & KP[TM] & KemP[CM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan59 = ctrl.Rule(KI[M] & KP[TM] & KemP[CM] & KS[CM], kepuasan['Memuaskan'])
aturan60 = ctrl.Rule(KI[M] & KP[TM] & KemP[CM] & KS[M], kepuasan['Memuaskan'])
aturan61 = ctrl.Rule(KI[M] & KP[TM] & KemP[M] & KS[TM], kepuasan['Memuaskan'])
aturan62 = ctrl.Rule(KI[M] & KP[TM] & KemP[M] & KS[CM], kepuasan['Memuaskan'])
aturan63 = ctrl.Rule(KI[M] & KP[TM] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])
aturan64 = ctrl.Rule(KI[M] & KP[CM] & KemP[TM] & KS[TM], kepuasan['Cukup Memuaskan'])
aturan65 = ctrl.Rule(KI[M] & KP[CM] & KemP[TM] & KS[CM], kepuasan['Memuaskan'])
aturan66 = ctrl.Rule(KI[M] & KP[CM] & KemP[TM] & KS[M], kepuasan['Memuaskan'])
aturan67 = ctrl.Rule(KI[M] & KP[CM] & KemP[CM] & KS[TM], kepuasan['Memuaskan'])
aturan68 = ctrl.Rule(KI[M] & KP[CM] & KemP[CM] & KS[CM], kepuasan['Memuaskan'])
aturan69 = ctrl.Rule(KI[M] & KP[CM] & KemP[CM] & KS[M], kepuasan['Sangat Memuaskan'])
aturan70 = ctrl.Rule(KI[M] & KP[CM] & KemP[M] & KS[TM], kepuasan['Memuaskan'])
aturan71 = ctrl.Rule(KI[M] & KP[CM] & KemP[M] & KS[CM], kepuasan['Sangat Memuaskan'])
aturan72 = ctrl.Rule(KI[M] & KP[CM] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])
aturan73 = ctrl.Rule(KI[M] & KP[M] & KemP[TM] & KS[TM], kepuasan['Memuaskan'])
aturan74 = ctrl.Rule(KI[M] & KP[M] & KemP[TM] & KS[CM], kepuasan['Memuaskan'])
aturan75 = ctrl.Rule(KI[M] & KP[M] & KemP[TM] & KS[M], kepuasan['Sangat Memuaskan'])
aturan76 = ctrl.Rule(KI[M] & KP[M] & KemP[CM] & KS[TM], kepuasan['Memuaskan'])
aturan77 = ctrl.Rule(KI[M] & KP[M] & KemP[CM] & KS[CM], kepuasan['Sangat Memuaskan'])
aturan78 = ctrl.Rule(KI[M] & KP[M] & KemP[CM] & KS[M], kepuasan['Sangat Memuaskan'])
aturan79 = ctrl.Rule(KI[M] & KP[M] & KemP[M] & KS[TM], kepuasan['Sangat Memuaskan'])
aturan80 = ctrl.Rule(KI[M] & KP[M] & KemP[M] & KS[CM], kepuasan['Sangat Memuaskan'])
aturan81 = ctrl.Rule(KI[M] & KP[M] & KemP[M] & KS[M], kepuasan['Sangat Memuaskan'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9, aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18, aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27, aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36, aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45, aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54, aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63, aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72, aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81])
system = ctrl.ControlSystemSimulation(engine)

system.input['kejelasan_informasi'] = 80
system.input['kejelasan_persyaratan'] = 60
system.input['kemampuan_petugas'] = 50
system.input['ketersediaan_sarpras'] = 90

system.compute()
hasil_kepuasan = system.output['kepuasan']

print(f"Kejelasan Informasi = 80")
print(f"Kejelasan Persyaratan = 60")
print(f"Kemampuan Petugas = 50")
print(f"Ketersediaan Sarpras = 90")
print("-" * 40)
print(f"Hasil Tingkat Kepuasan Pelayanan Adalah: {hasil_kepuasan:.2f}")

kepuasan.view(sim=system)
input("TEKAN ENTER untuk melanjutkan/menutup...")
