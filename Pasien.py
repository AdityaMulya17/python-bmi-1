class Pasien():
    # "Wira",27,20
    def __init__(self,nama,umur,bmi):
        self.nama = nama
        self.umur = umur
        self.bmi = bmi
    
    def get_nama(self):
        return self.nama
    
    def get_umur(self):
        return self.umur
    
    def greet_pasien(self):
        return "Selamat Datang " + self.nama
