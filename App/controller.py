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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadArtists(catalog,list_type):
    filename = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    if(list_type == 1):
        list_type = "ARRAY_LIST"
    else:
        list_type = "SINGLE_LINKED"
    return model.addArtists(catalog, filename, list_type)

def loadArtworks(catalog,list_type):
    filename = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    return model.addArtworks(catalog, filename, list_type)

# Funciones de ordenamiento
def ArtistsInRange(Artists,StartYear,EndYear):
    return model.ArtistsInRange(Artists,StartYear,EndYear)

def SortChronologically(artistsInRange,sort_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    else:
        sort_type = "MERGE"
    return model.SortChronologically(artistsInRange, sort_type)


# Funciones de consulta sobre el catálogo
