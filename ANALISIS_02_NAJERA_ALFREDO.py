"""
Alfredo Nájera Nájera

24 septiembre 2020
"""

# Cargamos el modulo para archivos csv
import csv

# %%
'''En esta parte analizaremos un poco la base de datos para visualizar su
contenido y ver las variables, si hay problemas con ellas y conocer un poco 
a detalle de las mismas.'''

# Abrimos el archivo
with open("synergy_logistics_database.csv", "r") as db:
    
    # Leemos el archivo como diccionario
    lector = csv.DictReader(db)
    
    # Recorremos todo el archivo renglón por renglón
    for linea in lector:
        continue

    ''' Imprimimos el valor de nuestro último elemento de la lista para 
    viausalizar que tenemos en los datos'''
    # print(linea)
    
    
# Creamos listas para guardar los valores distintos de cada llave de la base

# Lista para guardar las direcciones que existen
direcciones = []
# Lista que sirve para guardar los países de origen que existen
paises_origen = []
# Lista que sirve para guardar los países de destino que existen
paises_destino = []
# Lista para guardar los años que existen
anios = []
# Lista para guardar los productos que existen
productos = []
# Lista para guardar los modos de transporte que existen
modo_trans = []
# Lista para guardar el nombre de las distintas compañías que hay en la base
companias = []


''' Función que sirve para buscar valores distintos entre sí en una base
de datos (la que estamos trabajando) y guardar esos valores en una lista.
Lo anterior con propósito de no tener valores que realmente son igual pero
por errores de escritura sean considerados distintos, por ejemplo, China y
china.
Recibe como parámetros la clave a buscar y la lista donde se guardarán
los valores distintos.'''    
def buscador_base(clave, lista_valores):
    # Abrimos la base de datos que estamos utilizando
    with open("synergy_logistics_database.csv", "r") as db:
        # Creamos el objeto lector
        lector = csv.DictReader(db)
        # Recorremos cada elemento de nuestro archivo
        for linea in lector:
            # Condicional para validar los elementos de dicha clave
            if linea[clave] not in lista_valores:
                # Agregamos los valores que no están
                lista_valores.append(linea[clave])
        
# Aplicamos la función para cada clave con su respectiva lista
buscador_base("direction", direcciones)
buscador_base("origin", paises_origen)
buscador_base("destination", paises_destino)
buscador_base("year", anios)
buscador_base("product", productos)
buscador_base("transport_mode", modo_trans)
buscador_base("company_name", companias)
    
'''Si observamos nuestras variables en el caso de estar en Spyder, podemos
ver que ninguna lista que guardar los distintos tipos de variables que existen
en nuestra base tienen errores de escritura o se repiten de dos formas distintas
como lo mencioné al crear la función, en caso de no poder usar el explorador
de variables por no estar en Spyder, es necesario quitar las líneas de comentarios
para poder visualizarlas.'''

# print(direcciones)
# print(paises_origen)
# print(paises_destino)
# print(anios)
# print(productos)
# print(modo_trans)
# print(companias)

# %%

'''Abrimos una nueva celda de Spyder para resolver el punto u opción 1'''
# Abrimos el archivo
with open("synergy_logistics_database.csv", "r") as db:
    
    # Creamos el objeto de lectura
    lector = csv.DictReader(db)
    
    # Creamos una variable donde almacenaremos nuestra información
    db_copia = []
    
    ''' Hacemos la copia de nuestra base de datos en la variable para
    trabajar con ella'''
    for linea in lector:
        db_copia.append(linea)

# Visualizamos la lista con la que vamos a trabajar en su primer renglón
# print(db_copia[0])

'''Función que se encargará de ordenar el número de veces que se utiliza una ruta
de acuerdo a la dirección que le indiquemos, además de ordenarla también no solo por
el número de veces que se utiliza sino por su valor también.
Recibe como parámetro la dirección ya sea Imports o Exports'''
def opcion1(direccion):
    # Creamos listas para guardar las variables que usaremos
    # Lista para guardar los diccionarios con la dirección indicada
    auxiliar = []
    # Lista para guardar las rutas que hay en la dirección indicada
    lista_rutas = []
    # Lista que guarda listas con los datos que requerimos
    # Esta ordenada por el número de veces que se utilizó una ruta de mayor a menor
    lista_orden_ruta = []
    # Lista que guarda listas con los datos que requerimos
    # Esta ordenada por el valor de las rutas de mayor a menos
    lista_orden_valor = []
    '''Listas que guardan diccionarios con los siguientes datos:
       país de origen, país de destino, número de veces que se recorre la ruta,
       valor total que produce la ruta, número de veces que esa ruta utilizo 
       transporte por mar, aire, rieles o carreteras. Ambas ordenadas de mayor a
       menor, la primera por el número de veces que se utilizó la ruta, la segunda
       por el valor total que produce esa ruta'''
    lista_dic_ruta = []
    lista_dic_valor = []
    
    # Ciclo para recorrer nuestra base completa
    for linea in db_copia:
        # Condicional para separar por dirección
        if linea["direction"] == direccion:
            # Agregamos a la lista los diccionarios que cumplan la condición
            auxiliar.append(linea)
    
    # Ciclo para recorrer la lista que contiene datos de una sola direccion
    for aux in auxiliar:
        # Condicional para separar las rutas sin repeticiones
        if [aux["origin"], aux["destination"]] not in lista_rutas:
            # Agregamos las rutas a una lista
            lista_rutas.append([aux["origin"], aux["destination"]])
    
    # Ciclo for para recorrer las listas de rutas
    for ruta in lista_rutas:
        # Variable que contara el número de veces que se utiliza una ruta
        contador = 0
        # Variable que guardará el valor total que produce la ruta
        suma = 0
        # Variable que contará el número de veces que una ruta es por mar
        contador_mar = 0
        # Variable que contará el número de veces que una ruta es por aire
        contador_aire = 0
        # Variable que contará el número de veces que una ruta es por riel
        contador_riel = 0
        # Variable que contará el número de veces que una ruta es por carretera
        contador_carretera = 0
        # Ciclo para recorrer la lista que tiene los datos de la direccón que indicamos
        for linea in auxiliar:
            # Condicional que valida si el pais de origen y destino coincide con la ruta
            if ruta[0] == linea["origin"] and ruta[1] == linea["destination"]:
                # Aumentamos por cada coincidencia de ruta el valor del contador
                contador += 1
                # Aumentamos por cada coincidencia el valor que produce la ruta
                # Se convierte a entero pues estaba como cadena
                suma += int(linea["total_value"])
                # Condicional para validar que una ruta fue por mar
                if linea["transport_mode"] == "Sea":
                    # Contador que aumenta 1 por cada vez que utiliza el mar
                    contador_mar += 1
                # Condicional para validar que una ruta fue por aire
                elif linea["transport_mode"] == "Air":
                    # Contador que aumenta 1 por cada vez que utiliza el aire
                    contador_aire += 1
                # Condicional para validar que una ruta fue por riel
                elif linea["transport_mode"] == "Rail":
                    # Contador que aumenta 1 por cada vez que utiliza el riel
                    contador_riel += 1
                # Condicional para validar que una ruta fue por carretera
                elif linea["transport_mode"] == "Road":
                    # Contador que aumenta 1 por cada vez que utiliza el carretera
                    contador_carretera += 1
        # Aquí al acabar los registros de una ruta los agregamos a una nueva lista
        lista_orden_ruta.append([ruta[0], ruta[1], contador, suma, contador_mar,
                                 contador_aire, contador_riel, contador_carretera])
    
    # Ordenamos la lista de listas por el número de recorridos de cada ruta
    lista_orden_ruta.sort(key = lambda x : x[2], reverse = True)
    # Ordenamos la lista de listas por el valor producido de cada ruta
    lista_orden_valor = sorted(lista_orden_ruta, key = lambda x : x[3], reverse = True)
    
    # Ciclo para pasar toda la lista anterior a una lista con diccionarios (ordenada por recorridos)
    for elemento in lista_orden_ruta:
        # Cada iteración creamos un diccionario nuevo
        dic_aux = {}
        # Ponemos las claves de cada valor con su respectivo valor
        dic_aux["Origen"] = elemento[0]
        dic_aux["Destino"] = elemento[1]
        dic_aux["Numero_recorridos"] = elemento[2]
        dic_aux["Valor_total"] = elemento[3]
        dic_aux["Numero_mar"] = elemento[4]
        dic_aux["Numero_aire"] = elemento[5]
        dic_aux["Numero_riel"] = elemento[6]
        dic_aux["Numero_carretera"] = elemento[7]
        # Agregamos cada diccionario a una lista
        lista_dic_ruta.append(dic_aux)
    
    # Ciclo para pasar toda la lista anterior a una lista con diccionarios (ordenada por valor de la ruta)
    for elemento in lista_orden_valor:
        dic_aux = {}
        # Ponemos las claves de cada valor con su respectivo valor
        dic_aux["Origen"] = elemento[0]
        dic_aux["Destino"] = elemento[1]
        dic_aux["Numero_recorridos"] = elemento[2]
        dic_aux["Valor_total"] = elemento[3]
        dic_aux["Numero_mar"] = elemento[4]
        dic_aux["Numero_aire"] = elemento[5]
        dic_aux["Numero_riel"] = elemento[6]
        dic_aux["Numero_carretera"] = elemento[7]
        # Agregamos cada diccionario a una lista
        lista_dic_valor.append(dic_aux)
    
    # Regresamos las listas ordenadas que contienen diccionarios
    return lista_dic_ruta, lista_dic_valor


# Guardamos el resultado de la función en variables
exp_ruta, exp_valor = opcion1("Exports")
imp_ruta, imp_valor = opcion1("Imports")

# Imprimimos todas las respuestas de forma agradable
print("\nLas rutas de exportación más demandas por número de recorridos son:\n")
for i in range(10):
    print(1+i, ".- De ", exp_ruta[i]["Origen"], " a ", exp_ruta[i]["Destino"],
          " con ", exp_ruta[i]["Numero_recorridos"], " recorridos")

print("\nLas rutas de exportación que producen más valor son:\n")
for i in range(10):
    print(1+i, ".- De ", exp_valor[i]["Origen"], " a ", exp_valor[i]["Destino"],
          " con ", exp_valor[i]["Valor_total"], " unidades")
    
print("\nLas rutas de importación más demandas por número de recorridos son:\n")
for i in range(10):
    print(1+i, ".- De ", imp_ruta[i]["Origen"], " a ", imp_ruta[i]["Destino"],
          " con ", imp_ruta[i]["Numero_recorridos"], " recorridos")

print("\nLas rutas de importación que producen más valor son:\n")
for i in range(10):
    print(1+i, ".- De ", imp_valor[i]["Origen"], " a ", imp_valor[i]["Destino"],
          " con ", imp_valor[i]["Valor_total"], " unidades")
# %%

''' Abrimos una nueva celda de Spyder para resolver la opción 2'''

# Lista que guardará la copia del archivo
copia_db = []

# Abrimos el archivo y creamos una copia del documento para trabajarla
with open("synergy_logistics_database.csv", "r") as db:
    # Creamos el objeto lector
    lector = csv.DictReader(db)
    
    # Creamos copia del archivo con el que vamos a trabajar
    for linea in lector:
        copia_db.append(linea)
        

# Visualizamos el primer elemento de la copia
# print(copia_db[0])

# Función que obtiene el valor total por transporte de acuerdo a una direccion dada
def opcion2(direccion):
    
    # Contadores para guardar el número de veces que se usa el transporte y su valor
    contador_mar = 0
    contador_aire = 0
    contador_riel = 0
    contador_carretera = 0
    suma_mar = 0
    suma_aire = 0
    suma_riel = 0
    suma_carretera = 0
    
    # Ciclo que recorre toda la lista para obtener datos de la dirección que le sea dada
    for elemento in copia_db:
        # Condicional para validar la dirección
        if elemento["direction"] == direccion:
            # Condicional para validar el transporte por mar
            if elemento["transport_mode"] == "Sea":
                '''Operaciones para contar el número de veces que ocuparon este medio de transporte
                y guardar el valor total'''
                contador_mar += 1
                suma_mar += int(elemento["total_value"])
            # Condicional para validar el transporte por aire
            elif elemento["transport_mode"] == "Air":
                '''Operaciones para contar el número de veces que ocuparon este medio de transporte
                y guardar el valor total'''
                contador_aire += 1
                suma_aire += int(elemento["total_value"])
            # Condicional para validar el transporte por riel
            elif elemento["transport_mode"] == "Rail":
                '''Operaciones para contar el número de veces que ocuparon este medio de transporte
                y guardar el valor total'''
                contador_riel += 1
                suma_riel += int(elemento["total_value"])
            # Condicional para validar el transporte por carretera
            elif elemento["transport_mode"] == "Road":
                '''Operaciones para contar el número de veces que ocuparon este medio de transporte
                y guardar el valor total'''
                contador_carretera += 1
                suma_carretera += int(elemento["total_value"])
    
    # Lista para guardar todos las vías de transporte con sus respectivos datos
    lista_aux = [
        ["Mar", contador_mar, suma_mar],
        ["Aire", contador_aire, suma_aire],
        ["Riel", contador_riel, suma_riel],
        ["Carretera", contador_carretera, suma_carretera]
        ]
    
    # Ordenamos la lista por el valor que produjo o cuesta
    lista_aux.sort(key = lambda x : x[2], reverse = True)
    
    # Lista que tendra diccionarios con las respuestas anteriores, ya ordenadas
    lista_resultados = []
    
    # Ciclo para asignar a un diccionario valores de la lista auxiliar
    for i in range(len(lista_aux)):
        # Por cada iteración creamos un diccionario
        dic = {}
        # Agregamos el medio de transporte
        dic["Medio_transporte"] = lista_aux[i][0]
        # Agregamos el número de veces que se utilizó
        dic["Numero_recorridos"] = lista_aux[i][1]
        # Agregamos el valor total
        dic["Valor"] = lista_aux[i][2]
        # Agregamos el diccionario a la lista
        lista_resultados.append(dic)
    
    # Borramos la lista que sirvió para ordenar los valores
    del lista_aux
    
    # Imprimimos el mensaje con la consigna de forma agrable
    print("\nLos tres medios de transporte más importantes en " + direccion + " son: \n")
    for i in range(3):
        print(i+1, ".-" + lista_resultados[i]["Medio_transporte"] + " con un valor de "
              + str(lista_resultados[i]["Valor"]) + " unidades")
    return lista_resultados
        
# Usamos la función con ambas direcciones
opcion2_trans_exp = opcion2("Exports")
opcion2_trans_imp = opcion2("Imports")

# %%

'''Abrimos una nueva celda para la opción 2'''

'''Para esta parte debemos usar las variables de la opción 1, de esta forma
no escribimos tanto código'''

'''Función que recibe una lista con las rutas más utilizadas de acuerdo a una dirección,
ordenadas por el valor, estamos utilizando como parámetros una lista pero realmente
solo acepta las listas de la opción 1'''
def opcion3(lista = exp_valor):
    # Variable que guardará el valor total para la lista como argumento
    valor_total = 0
    # Ciclo para ir sumando todos los valores
    for valor in lista:
        # Vamos guardando todos los valores
        valor_total += valor["Valor_total"]
        
    # Lista para añadirle al parámetro una clave que tenga el porcentaje respecto al valor total
    for valor in lista:
        # Aqui hacemos la operación para el valor total redondeando a 3 decimales
        valor["Valor_porcentaje"] = round(valor["Valor_total"] / valor_total, 3)
    
    # Variable que nos indicará hasta que índice se alcanza el 80% o al menos el 80%
    indice = 0
    # Variable que guarda la suma de los porcentajes
    suma_porcentaje = 0
    
    # Ciclo para recorrer la lista como parámetro
    for valor in lista:
        # Condicional para no acumular más del 80% o al menos que no sume hasta el 100%
        if suma_porcentaje < 0.8:
            # Vamos guardando el valor del índice
            indice += 1
            # Vamos guardando el valor acumulado porcentual
            suma_porcentaje += valor["Valor_porcentaje"]
        
    # Condicional para saber que mensaje imprimir
    if lista == exp_valor:
        # Mensaje en el caso de exportaciones
        print("\nLos países que generan  aproximadamente el 80% del valor de las exportaciones son:\n")
        for i in range(indice):
            print(i+1, ".- País: " + lista[i]["Origen"])
            print("   Valor en porcentaje con respecto al total: " + str(round(lista[i]["Valor_porcentaje"] * 100, 2)) + "%")
    else:
        # Mensaje en el caso de importaciones
        print("\nLos países que generan  aproximadamente el 80% del valor de las importaciones son:\n")
        for i in range(indice):
            print(i+1, ".- País: " + lista[i]["Destino"])
            print("   Valor en porcentaje con respecto al total: " + str(round(lista[i]["Valor_porcentaje"] * 100, 2)) + "%")
    

            
            
# Aplicamos la función a la lista de exportaciones e importaciones
opcion3(exp_valor)
opcion3(imp_valor)

