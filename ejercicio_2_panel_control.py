comando = input("Ingrese un código de comando (A, B, C o D): ").upper() #(.upper()) asi acepta letras mayusculas y minusculas cuando se ingresen 


match comando:
    case "A":
        print("Iniciando diagnóstico del sistema...")

    case "B":
        print("Activando enfriamiento de emergencia...")

    case "C" :
        print("Mostrando registro de errores...")

    case "D":
        print("Apagando el panel.")

    case _: 
        print("Comando no reconocido. Intente de nuevo.")