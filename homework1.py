# perhitungan_ukt
print('nama harus lengkap')
nama = input('nama : ')
umur = int(input('umur : '))
pekerjaan_ayah = input('pekerjaan ayah : ')
print('untuk penghasilan hanya input angkanya saja tanpa titik ataupun koma')
penghasilan_ayah = int(input('penghasilan per bulan : '))
pekerjaan_ibu = input('pekerjaan ibu : ')
penghasilan_ibu = int(input('penghasilan perbulan : '))
print('tanggungan adalah semua anak kandung dari orang tua peserta')
jumlah_tanggungan = int(input('jumlah tanggungan : '))
print('masukan dalam meter persegi')
panjang_rumah = int(input('panjang rumah : '))
lebar_rumah = int(input('lebar rumah :'))
motor = int(input('motor yang dimiliki : '))
mobil = int(input('mobil yang dimiliki : '))
print('umr hanya memakai angka tanpa titik dan koma')
umr = int(input('umr daerah anda : '))
bebas_ukt = (input('punya KIP atau bidik misi? '))

# perhitungan

lolos = ['iya','Iya','ya']
gaji_pokok = penghasilan_ayah + penghasilan_ibu
taggungan = jumlah_tanggungan * 100000
luas_rumah = panjang_rumah * lebar_rumah
pajak_rumah =luas_rumah * 1000
perhitungan_motor = motor * 300000
perhitungan_mobil = mobil * 500000
hasil_utama = gaji_pokok + taggungan + perhitungan_mobil + perhitungan_motor + pajak_rumah
diskon = umr * 3 
kalkulasi = hasil_utama - diskon
print('kuliah gratis') if bebas_ukt in lolos else print('ukt bergolongan dengan ukt : ',kalkulasi)

