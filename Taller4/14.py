#14.	Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta = float(input("Ingrese su renta anual: "))
if renta < 10000:
    tipo_impositivo = 0.05
elif renta < 20000 and renta >= 10000:
    tipo_impositivo = 0.15
elif renta < 35000 and renta >= 20000:
    tipo_impositivo = 0.2
elif renta < 60000 and renta >= 35000:
    tipo_impositivo = 0.3
else:
    tipo_impositivo = 0.45
print(f"El tipo impositivo que le corresponde es: {tipo_impositivo * 100}%")