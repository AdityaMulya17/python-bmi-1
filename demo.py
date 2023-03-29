bmi_value = 30
status = "Normal"

if(bmi_value < 18.5):
    status = "Underweight"
elif(bmi_value < 25 and bmi_value > 18.5):
    status = "Tidak Underweight"

print(status)