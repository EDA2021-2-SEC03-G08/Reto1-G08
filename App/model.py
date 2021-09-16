"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de artistas y obras.
    """
    catalog = {'artists': None,'artworks': None}
    return catalog

def addArtists(catalog, artists_file,list_type):
    catalog['artists'] = lt.newList(datastructure=list_type,filename=artists_file)

def addArtworks(catalog, artworks_file, list_type):
    catalog['artworks'] = lt.newList(datastructure=list_type,filename=artworks_file)

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def ArtistsInRange(Artists,StartYear,EndYear,list_type):
    artistsInRange = lt.newList(datastructure=list_type)
    posList = 0
    while posList < lt.size(Artists):
        Artist = lt.getElement(Artists,posList)
        Year = int(Artist['BeginDate'])
        if Year >= StartYear and Year <= EndYear:
            lt.addLast(artistsInRange,Artist)
        posList += 1
    return artistsInRange


def SortChronologically(artistsInRange):
    for pos1 in range(lt.size(artistsInRange)):
        minPos = pos1
        for pos2 in range(pos1+1, lt.size(artistsInRange)):
            YearMin = lt.getElement(artistsInRange,minPos)['BeginDate'] 
            Year2 = lt.getElement(artistsInRange,pos2)['BeginDate'] 
            if Year2 < YearMin:
                minPos = pos2

        lt.exchange(artistsInRange,minPos,pos1)
    sortedArtists = artistsInRange
    return sortedArtists

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
Args:
artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """     

    


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento