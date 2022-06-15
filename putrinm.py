class nilai_akhir:
	print("<><><><><>Akumulasi Nilai Akhir<><><><><>")

	
	def __init__(self, Nama, Kehadiran, Tugas, UTS, UAS):
		self.Nama = Nama
		self.Kehadiran = Kehadiran
		self.Tugas = Tugas
		self.UTS = UTS
		self.UAS = UAS
		
	def nilai(self):
		print('Nama	: ' + self.Nama)
		print('Kehadiran	: ' + self.Kehadiran)
		print('Tugas	: ' + self.Tugas)
		print('UTS	: ' + self.UTS)
		print('UAS	: ' + self.UAS)
		
	def akumulasi(nilai):
		if nilai >= 80	:
			print('Sangat baik	:	A')
		elif nilai >= 70	:
			print('Baik	:	B')
		elif nilai >= 55	:
			print('Cukup	:	C')
		elif nilai >= 40	:
			print('Kurang	:	D')
		elif nilai <= 39	:
			print('Sangat buruk	:	E')
		if nilai >= 60	:
			print('Keterangan	:	Lulus')
		else :
			print('Keterangan	:	Tidak Lulus')

		
class nilai_akhir():
	pass

Nama = input('Nama		: ')
Kehadiran = input('Kehadiran	: ')
Tugas = input('Tugas		: ')
UTS = input('UTS		: ')
UAS = input('UAS		: ')