# Función que separa las letras mayúsculas y minúsculas de la cadena que recibe como parámetro, además
# identifica posibles errores de la cadena como la presencia de dígitos, caracteres especiales o si viene vacía.

def separa_letras(cadena1):  # Recibe la variable cadena1 como parámetro
    cadena = str(cadena1)  # Convierte la cadena en una variable de tipo string
    caracteres_especiales = "!\"#$%&'()*+, -./:;<=>?@[]/^_`{|}~"  # Contiene todos los caracteres especiales
    estado = 0  # Se inicializa el valor de estado

    if not cadena.strip():  # If para identificar si la cadena se encuentra vacía
        estado = -300  # En caso de que la cadena esté vacía, el codigo de error es -300

    for caracter in cadena:  # Este ciclo recorre todos los caracteres para identificar dígitos o caracteres especiales
        if caracter.isdigit():  # Busca dígitos
            estado = -100  # En caso de que haya un digito en la cadena, el codigo de error es -100

        elif caracter in caracteres_especiales:  # Busca caracteres especiales
            estado = -200  # En caso de que haya un caracter especial en la cadena, el codigo de error es -200

        else:  # En caso de que no encuentre errores, el codigo de exito único es 0
            estado = 0

    letras_mayusculas = ""  # Se inician las variables que contienen las letras mayúsculas y minúsculas
    letras_minusculas = ""

    for letra in cadena:  # Este ciclo recorre los caracteres de la cadena e identifica las matusculas y minusculas
        if letra.isupper():  # True en caso de que la letra de la iteración actual sea mayúscula
            letras_mayusculas += letra  # Se concatena la letra de la iteración actual a la cadena de mayúsculas
        elif letra.islower():  # True en caso de que la letra de la iteración actual sea minúscula
            letras_minusculas += letra  # Se concatena la letra de la iteración actual a la cadena de minúsculas

    if estado != 0:  # Si se encontró algún error, retora el código de error único y None para los espacios de letras
        return estado, None, None

    else:  # Si no se encontró ningún error, se retorna el código de éxito único y las letras mayúsculas y minúsculas
        return estado, letras_mayusculas, letras_minusculas


# La función potencia_manual recibe una base y una potencia como parámetros y realiza la operación de potencia
# Además, identifica si las variables recibidas como parámetro no son números y, si es el caso, devuelve un código
# de error único.
def potencia_manual(base, potencia):  # Recibe las variables base y potencia como parámetros
    if isinstance(base, str) or isinstance(potencia, str):  # True si alguno de los parámetros es de tipo string
        estado = -400  # En dicho caso se retorna el código de error único -400 y None para el espacio de resultado.
        return estado, None
    else:
        estado = 0  # En el caso contrario, se retorna un código de éxito único 0

    if potencia == 0:  # Se calcula el caso especial en el que el valor del exponente sea 0
        return estado, 1  # Se retorna el resultado 1 sin importar el valor de la base

    else:  # Si la potencia es diferente de 0:
        resultado = 0  # Se inicializa el valor de resultado en 0 puesto que después se incrementa
        aux = base  # Se guarda el valor de base en la variable aux, para realizar el incremento inicial

        for i in range(1, potencia):  # Se repite el ciclo según el valor de la potencia.

            for j in range(base):  # Se suma a resultado una cantidad de veces según el valor de base
                resultado += aux  # El valor que se suma depende del resultado anterior (base en el caso inicial)
            aux = resultado  # Aux guarda el valor de aux para que en la siguiente suma se incremente como potencia
            resultado = 0  # Se devuelve el resultado a 0 para que no se sume la cantidad anterior a la potencia actual

        return estado, aux  # Una vez se calculan todas las potencias se retorna el codigo de éxito y la potencia (aux)
