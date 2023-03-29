import os

def get_bmi_value():
    """
        Calculate BMI Value
    """
    os.system("clear")
    berat_badan = float(input("Masukkan berat badan (kg): "))
    os.system("clear")
    tinggi_badan = float(input("Masukkan tinggi badan (meter): "))
    os.system("clear")
    print("BMI Kamu: "+str(berat_badan/(tinggi_badan**2)))
    input()
    os.system("clear")

def print_intro():
    print("Selamat Datang di Aplikasi Cek BMI")
    print("Opsi: ")
    print("1. Cek BMI ")
    print("2. Get BMI Value ")
    print("3. Keluar ")

def cek_bmi_status(bmi_value):
    """
        Calculate BMI Value and Return Result
    """
    if(bmi_value < 18.5):
        status = "Underweight"
    elif(bmi_value < 25 and bmi_value > 18):
        status = "Normal"
    else:
        status="Obesity"
    return status

def get_bmi_status_lengkap():
    os.system("clear")
    berat_badan = float(input("Masukkan berat badan (kg): "))
    os.system("clear")
    tinggi_badan = float(input("Masukkan tinggi badan (meter): "))
    os.system("clear")
    bmi_value = berat_badan/(tinggi_badan**2)
    status = "Belum Diukur"
    if(bmi_value < 18.5):
        status = "Underweight"
    elif(bmi_value < 25 and bmi_value > 18):
        status = "Normal"
    else:
        status="Obesity"
    print("Status Kamu: "+status)
    input()
    os.system("clear")
    
def end_program():
    os.system("clear")
    print("Terima Kasih Sudah Menggunakan Aplikasi BMI")
    input()
    