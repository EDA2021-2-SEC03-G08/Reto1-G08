"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from App.model import SortArtworks
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas para un rango de años")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")

def printLastArtists(Artists):
    LastArtists = lt.subList(Artists,lt.size(Artists)-4,3)
    i = 1
    for Artist in lt.iterator(LastArtists):
        print(str(i) + '. Name: ' + Artist['DisplayName'] +',', 'Biography:', Artist['ArtistBio'] + '.')
        i += 1

def printLastArtworks(Artworks):
    LastArtworks = lt.subList(Artworks,lt.size(Artworks)-4,3)
    i = 1
    for Artwork in lt.iterator(LastArtworks):
        print(str(i) + '. Title: ' + Artwork['Title'] +',', 'Date:', Artwork['Date'] +',',
        'Medium:', Artwork['Medium'] +',', 'Classification:', Artwork['Classification'] + '.')
        i+=1

def printReq1Answer(SortedArtists,StartYear,EndYear):
    if lt.size(SortedArtists) > 0:
        print('Se encontró(aron)', str(lt.size(SortedArtists)), 'artista(s) entre el año',
        str(StartYear), 'y', str(EndYear) + '.')
        input('Presione "Enter" para continuar.')
        
        if lt.size(SortedArtists) > 6:
            print('Los primeros 3 y 3 últimos artistas encontrados fueron:\n')
            i = 1
            while i <= 3:
                Artist = lt.getElement(SortedArtists,i-1)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
            print('...')
            i = lt.size(SortedArtists)-2
            while i <= lt.size(SortedArtists):
                Artist = lt.getElement(SortedArtists,i-1)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
        else:
            print('El(los) artista(s) encontrado(s) fue(ron):\n')
            i = 1
            while i <= lt.size(SortedArtists):
                Artist = lt.getElement(SortedArtists,i-1)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
    else:
        print('No se encontró ningún artista para el rango de años dado.')
    input('Presione "Enter" para continuar.\n')

def printReq2Answer(SortedArtworks,StartYear,EndYear):
    if lt.size(SortedArtworks) > 0:
        print('Se encontró(aron)', str(lt.size(SortedArtworks)), 'obra(s) entre el año',
        str(StartYear), 'y', str(EndYear) + '.')
        input('Presione "Enter" para continuar.')
        
        if lt.size(SortedArtworks) > 6:
            print('Las primeras 3 y 3 últimas obras encontradas fueron:\n')
            i = 1
            while i <= 3:
                artwork = lt.getElement(SortedArtworks,i-1)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Categoría:', str(artwork['Cataloged']) + ',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
            print('...')
            i = lt.size(SortedArtworks)-2
            while i <= lt.size(SortedArtworks):
                artwork = lt.getElement(SortedArtworks,i-1)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Categoría:', str(artwork['Cataloged']) + ',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
        else:
            print('La(s) obra(s) encontrada(s) fue(ron):\n')
            i = 1
            while i <= lt.size(SortedArtworks):
                artwork = lt.getElement(SortedArtworks,i-1)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Categoría:', str(artwork['Cataloged']) + ',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
    else:
        print('No se encontró ninguna obra para el rango de años dado.')
    input('Presione "Enter" para continuar.\n')
    

"""
Menu principal
"""
catalog = None
Artists = None
Artworks = None
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        listaValida = False
        while listaValida:
            list_type = int(input("Seleccione el tipo de representación de lista\n (1.) ARRAY_LIST (2.) LINKED_LIST"))
            if(list_type != 1 and list_type != 2):
                print("Por favor ingrese una opción válida")
            else:
                listaValida = True
        
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadArtists(catalog)
        controller.loadArtworks(catalog)
        Artists = catalog['artists']
        Artworks = catalog['artworks']
        print('Total de artistas cargados: ' + str(lt.size(Artists)))
        print('Total de obras cargadas: ' + str(lt.size(Artworks)))
        input('Presione "Enter" para continuar.')

        print('\nInformación de últimos artistas de la lista:\n')
        printLastArtists(Artists)
        input('Presione "Enter" para continuar.')

        print('\nInformación de últimas obras de la lista:\n')
        printLastArtworks(Artworks)
        input('Presione "Enter" para continuar.\n')
        
    
    elif catalog == None:
        print('Debe cargar los datos antes de seleccionar cualquier opción.')
        input('Presione "Enter" para continuar.\n')
    
    elif int(inputs[0]) == 2:
        StartYear = int(input('Brinde el año inicial del rango: '))
        EndYear = int(input('Brinde el año final del rango: '))
        artistsInRange = controller.ArtistsInRange(Artists,StartYear,EndYear)
        SortedArtists = controller.SortChronologically(artistsInRange)
        printReq1Answer(SortedArtists,StartYear,EndYear)

    elif int(inputs[0]) == 3:
        StartYear = input('Brinde la fecha inicial del rango: ')
        EndYear = input('Brinde la fecha final del rango: ')
        
        sampleValido = False
        while not sampleValido:
            sample_size = input('Escoja el tamaño de muestra: ')
            if sample_size.isnumeric():
                sample_size = int(sample_size)
                sampleValido = True
            else:
                print("Por favor ingrese una opción válida")
        
        sortValido = False
        while not sortValido:
            sort_type = int(input("Seleccione el tipo de sort\n (1.) QuickSort (2.) Insert (3.) Shell (4.) Selection (5.) Merge"))
            if(sort_type != 1 and sort_type != 2 and sort_type != 3 and sort_type != 4 and sort_type != 5):
                print("Por favor ingrese una opción válida")
            else:
                sortValido = True
        artworksInRange = controller.ArtworksInRange(Artworks,StartYear,EndYear,list_type,sample_size)
        sorted_artworks = SortArtworks(artworksInRange,sort_type)

        printReq2Answer(sorted_artworks,StartYear,EndYear)

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
