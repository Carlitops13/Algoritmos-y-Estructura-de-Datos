#5.	El director de una escuela está organizando un viaje de estudios,
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
# La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, 
# el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
# sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y
# lo que debe pagar cada alumno por el viaje.


costoRentaBus= 4000
alumnos  = int(input("Ingrese el número de alumnos: "))
if alumnos >= 100:
    costo_porAlumno= 65
    costo_total= costo_porAlumno * alumnos
    print("El costo finaal es: ", costo_total)
elif alumnos >= 50 and alumnos <= 99:
    costo_porAlumno= 70
    costo_total= costo_porAlumno * alumnos
    print("El costo finaal es: ", costo_total)
elif alumnos >= 30 and alumnos <= 49:
    costo_porAlumno= 95
    costo_total= costo_porAlumno * alumnos
    print("El costo finaal es: ", costo_total)
elif alumnos < 30:
    print("El costo final es: ", costoRentaBus)
else:
    print("El número de alumnos no es válido")