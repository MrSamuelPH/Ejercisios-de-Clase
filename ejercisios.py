def calcular_digito_verificador(rol):
    rol = rol.replace('-', '')  # Remover el guión si existe
    rol_invertido = rol[::-1]

    suma = 0
    multiplicador = 2

    for digito in rol_invertido:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    return rol + '-' + str(digito_verificador)


rol_utfsm = input("Ingrese el rol UTFSM: ")
digito_verificador = calcular_digito_verificador(rol_utfsm)

print("El dígito verificador del rol UTFSM", rol_utfsm, "es:", digito_verificador)