from modul.bmi_calculator import get_bmi_value,get_bmi_status_lengkap,print_intro,end_program
      
while True:
    print_intro()
    opsi = input("Masukkan opsi: ")
    if(opsi == "1"):
        get_bmi_status_lengkap()
    elif(opsi == "2"):
        get_bmi_value()
    else:
        end_program()
        break