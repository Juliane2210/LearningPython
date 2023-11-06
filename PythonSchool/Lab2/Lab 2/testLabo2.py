def celsius_en_fahrenheit (temp_Celsius):
    temp_Fahrenheit = (temp_Celsius * 9.0/5.0) + 32
    return temp_Fahrenheit



t_celsius = 100
t_fahrenheit = celsius_en_fahrenheit(t_celsius) 
print(t_celsius, "Celsius est", t_fahrenheit, "Fahrenheit." )