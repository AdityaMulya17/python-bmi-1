import os

class Aplikasi():
    
    # konstruktor
    def __init__(self,nama,tinggi_badan,berat_badan):
        self.nama = nama
        self.tinggi_badan = tinggi_badan
        self.berat_badan = berat_badan
    
    # method
    def get_info_pasien(self):
        print("Nama: {}, Tinggi Badan: {}, Berat Badan: {}".format(self.nama,self.tinggi_badan,self.berat_badan))
    
    # method
    def get_bmi_lengkap(self):
        bmi_value = self.berat_badan/(self.tinggi_badan**2)
        status = "Belum Diukur"
        if(bmi_value < 18.5):
            status = "Underweight"
        elif(bmi_value < 25 and bmi_value > 18):
            status = "Normal"
        else:
            status="Obesity"
        print("Pasien "+self.nama+" BMI: "+str(bmi_value))
        return status
    
