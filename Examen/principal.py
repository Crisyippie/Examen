import funciones as fn, json

trabajadores_con_sueldo = {}

with open('trabajadores.json','w') as archivo:
        json.dump(trabajadores_con_sueldo,archivo,indent=4)

while True: 
    print('''
                   [- Menu -]
          
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadísticas.
            4. Reporte de sueldos
            5. Salir del programa

            ''')
    
    try:
        opcion = int(input("Opción: "))
        if opcion in range(1,5):
            print("Ingresando...")
        else:
            print("¡Opcion fuera del rango!")
    except ValueError:
        print("¡Tiene que ser un numero, ingrese de nuevo!")
    else:
        if opcion == 1:
            trabajadores_con_sueldo = fn.asignar_sueldos(trabajadores_con_sueldo)
        elif opcion == 2:
            fn.clasificar_sueldos(trabajadores_con_sueldo)
        elif opcion == 3:
            fn.estadisticas(trabajadores_con_sueldo)
        elif opcion == 4:
            fn.reporte_sueldos(trabajadores_con_sueldo)
        elif opcion == 5:
            break