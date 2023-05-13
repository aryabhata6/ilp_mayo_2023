# entradas de datos
#declarar o crear variables 
number_1 = input("Escribe el 1er numero: ")
number_2= input("Escribe el 2do numero: ")


#procesos(calculos matematicos o logicos)
suma=number_1 + number_2
resta=number_1 - number_2
multiplicacion=number_1*number_2
division=number_1/number_2
potencia_1=number_1**number_2
potencia_2=pow(number_1,number_2)
cuadrado=number_1**2
cubo=pow(number_2,3)


modulo_residuo = (20 % 6)


#salida de datos
print("la suma es =",suma)
print("la suma es =",str(suma)) #concatenacion (union de 2 o mas textos)
print("la resta es =",resta)
print("la suma es =",{suma})
#casteo es la conversion de un tipo de dato a otro tipo de dato
print("la multiplicacion es =",multiplicacion)
print("la division es =",round(division,2))
print("la potencia es =",number_1**number_2)
print("el cuadrado es = ",pow(number_1,number_2))
print("el cubo es =",pow(number_2,3))
print('el resultado de modulo o residuo de 20%6 =')
