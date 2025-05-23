#Realizar una calculadora que sume, reste, multiplique, divida, potencia
#Suma
nombre= input("Por favor ingrese su Nombre: ")
print ("Bienvenido ", nombre)
print ("Ingrese dos números")
num1= int(input ("Ingrese el primer número: "))
num2= int(input ("Ingrese el segundo número:  ")) 
suma=num1+num2
print ("La suma de los dos números es: ", suma )
resta=num1-num2
print ("La resta de los los números es: " ,resta )
mult= num1*num2
print (" La multiplicación de los números es: ",mult )
div= num1/num2
print ("La división de los números es: ", round(div,3) )
expo= num1**num2
print ("La potencia de los números es: ", expo )
mod= num1%num2
print ("El módulo de los números es: ", mod )


