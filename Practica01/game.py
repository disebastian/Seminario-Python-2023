from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
operators_without_division = ["+", "-", "*"]

# Cantidad de cuentas a resolver
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

# Contador de respuestas correctas o incorrectas del usuario.
right_answers = 0
wrong_answers = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    if number_2 != 0:
        operator = choice(operators)
    else:
        # Para evitar la division de un numero por 0:
        operator = choice(operators_without_division)
        
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    
    # Le pedimos al usuario el resultado (se permite ingresar nros con coma)
    result = float(input("resultado: "))
    
    # Verificación de acierto/desacierto de la respuesta del usuario y cantidades de ellos
    match operator:
        case '+':
            correct_result = number_1 + number_2
        case '-':
            correct_result = number_1 - number_2
        case '*':
            correct_result = number_1 * number_2
        case '/':
            correct_result = number_1 / number_2            

    if result == correct_result:
        print('¡El resultado ingresado es correcto!')
        right_answers += 1
    else:
        print(f'El resultado ingresado no es correcto. La respuesta correcta es {correct_result}')
        wrong_answers += 1
    
    print()
    
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
print(f"\nTardaste {total_time.seconds} segundos.")

# Cantidad de aciertos/desaciertos
print(f'Cantidad de respuestas correctas = {right_answers} \nCantidad de respuestas incorrectas = {wrong_answers}')

#---------
#Situacion que quedan por resolver:
#Ingresos no debidos del usuario (falta una verificacion de que lo que se ingresa por teclado sean numeros)