from modul.bmi_calculator import get_bmi
      
berat_badan = float(input("Masukkan berat badan: "))
tinggi_badan = float(input("Masukkan tinggi badan: "))
bmi = get_bmi(berat_badan,tinggi_badan)

if(bmi < 18.5):
    print("Underweight")
elif(18.5 < bmi and bmi <24.9):
    print("Normal")
else:
    print("Obesitas")