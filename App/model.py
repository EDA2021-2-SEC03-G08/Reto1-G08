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

def addArtists(catalog, artists_file):
    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST',filename=artists_file)

def addArtworks(catalog, artworks_file):
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST',filename=artworks_file)

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def SortChronologically(Artists,StartYear,EndYear):
    SortedArtists = lt.newList(datastructure='ARRAY_LIST')
    posList = 0
    while posList < lt.size(Artists):
        Artist = lt.getElement(Artists,posList)
        Year = int(Artist['BeginDate'])
        if Year >= StartYear and Year <= EndYear:
            if lt.isEmpty(SortedArtists):
                lt.addFirst(SortedArtists,Artist)
            else:
                Sorted = False
                posIni = 0
                posFin = lt.size(SortedArtists)-1
                while not Sorted:
                    pos = (posIni + posFin)//2
                    CompYear = int(lt.getElement(SortedArtists,pos)['BeginDate'])
                    if Year == CompYear:
                        lt.insertElement(SortedArtists,Artist,pos)
                        Sorted = True
                    elif Year > CompYear:
                        posIni = pos + 1
                        if posIni > posFin:
                            lt.addLast(SortedArtists,Artist)
                            Sorted = True
                        elif posIni == posFin:
                            lt.insertElement(SortedArtists,Artist,pos)
                            Sorted = True
                    else:
                        posFin = pos - 1
                        if posFin < posIni:
                            lt.insertElement(SortedArtists,Artist,posIni)
                            Sorted = True
                        elif posIni == posFin:
                            lt.insertElement(SortedArtists,Artist,pos)
                            Sorted = True
        posList += 1
    return SortedArtists

                




# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento