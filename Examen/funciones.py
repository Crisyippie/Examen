import json, random, csv

# FUNCION DE ASIGNACION DE SUELDOS
def asignar_sueldos(trabajadores_con_sueldo):
    # TRABAJADORES DE LA EMPRESA SIN EL SUELDO
    trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
    # TRABAJADORES DE LA EMPRESA CON UN SUELDO DEFINIDO 
    trabajadores_con_sueldo = {}

    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000) # A SUELDO SE LE ASIGNA UN VALOR ENTRE 300.000 Y 2.500.000
        trabajadores_con_sueldo[trabajador] = sueldo 
    # CREA EL ARCHIVO QUE CONTIENE LOS SUELDOS 
    with open('trabajadores.json','w') as archivo:
        json.dump(trabajadores_con_sueldo,archivo,indent=4)

        print("¡Archivo creado con exito!")
        return trabajadores_con_sueldo

# FUNCIONE DE CLASIFICAR 
def clasificar_sueldos(trabajadores_con_sueldo):

    # CLASIFICACIONES
    menor_800 = {}
    entre_800_y_2000000 = {}
    superior_a_2000000 = {}

    # LEE EL ARCHIVO 
    with open('trabajadores.json','r') as archivo:
        trabajadores = json.load(archivo)

        for nombre,sueldo in trabajadores.items():
            if sueldo < 800000:
                menor_800[nombre] = sueldo 
            elif sueldo >= 800000 and sueldo <= 2000000:
                entre_800_y_2000000[nombre] = sueldo
            elif sueldo > 2000000:
                superior_a_2000000[nombre] = sueldo
        print("     [- Clasificacion -]")

        print("\nSueldos menores a $800.000\n")
        for nombre,sueldo in menor_800.items():
            print(nombre,sueldo)

        print("\nSueldos entre $800.000 y $2.000.000\n")
        for nombre,sueldo in entre_800_y_2000000.items():
            print(nombre,sueldo)

        print("\nSueldos superiores a 2.000.000\n")
        for nombre,sueldo in superior_a_2000000.items():
            print(nombre,sueldo)


def estadisticas(trabajadores_con_sueldo):

    sueldos = [0]

    with open('trabajadores.json','r') as archivo:
        trabajadores = json.load(archivo)

        for trabajador,sueldo in trabajadores.items():
            sueldos.append(sueldo)

        sueldo_mas_bajo = min(sueldos)
        sueldo_mas_alto = max(sueldos)
        promedio_sueldos = sum(sueldos) / len(sueldos)

        print(f"Sueldo mas bajo: ",{sueldo_mas_bajo})
        print(f"Sueldo mas alto: ",{sueldo_mas_alto})
        print(f"Promedio de Sueldos: ",{promedio_sueldos})


def reporte_sueldos(trabajadores_con_sueldo):

    tabla = []
    
    with open('trabajadores.json','r') as archivo:
        trabajadores = json.load(archivo)

        for trabajador,sueldo in trabajadores.items():
            
            sueldo_base = sueldo 
            desc_salud = sueldo * 0.7
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp

            tabla.append({
                'trabajador': trabajador,
                'sueldo Base' : sueldo_base,
                'Desc Salud' : desc_salud,
                'Desc AFP' : desc_afp,
                'Sueldo liquido' : sueldo_liquido
            })
            tabla_copia = tabla

        print(tabla)
        with open('tabla.csv','w',newline=None) as archivo_csv:
            escribir_csv = csv.writer(archivo_csv)
            
            escribir_csv.writerow('tabla')
            for datos in tabla:
                escribir_csv.writerows(datos)
            

            
            