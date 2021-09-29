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
    filename = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    if(list_type == 1):
        list_type = "ARRAY_LIST"
    else:
        list_type = "SINGLE_LINKED"
    return model.addArtists(catalog, filename, list_type)

def loadArtworks(catalog,list_type):
    filename = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    if(list_type == 1):
        list_type = "ARRAY_LIST"
    else:
        list_type = "SINGLE_LINKED"
    return model.addArtworks(catalog, filename, list_type)

#Requirement 1
def ArtistsInRange(Artists,StartYear,EndYear,list_type):
    return model.ArtistsInRange(Artists,StartYear,EndYear,list_type)

def SortChronologically(artistsInRange):
    return model.SortChronologically(artistsInRange)

#Requirement 2
def findArtist(artists,artist_IDs):
    return model.findArtist(artists,artist_IDs)

def ArtworksInRange(Artworks,StartYear,EndYear,list_type):
    return model.ArtworksInRange(Artworks,StartYear,EndYear,list_type)

def SortArtworks(artworks,sort_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworks(artworks,sort_type)

#Requirement 3
def encounterArtist(artists,artist_name):
    return model.encounterArtist(artists,artist_name)

def artistMediumInfo(artworks,artist_ID,list_type):
    return model.artistMediumInfo(artworks,artist_ID,list_type)

#Requirement 4
def nationalityArtworks(artworks,artists,list_type):
    return model.nationalityArtworks(artworks,artists,list_type)

def sortNations(artworksNationality,nation,sort_type):
    return model.sortNations(artworksNationality,nation,sort_type)

#Requirement 5
def checkDepartment(artworks,department):
    return model.checkDeparment(artworks,department)

def moveDepartment(artworks,department,list_type):
    return model.moveDepartment(artworks,department,list_type)

def artworksWithDate(artworks_dep,list_type):
    return model.artworksWithDate(artworks_dep,list_type)

def SortArtworksByDate(artworks_dep,sort_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworksByDate(artworks_dep,sort_type)

def SortArtworksByPrice(artworks_dep,sort_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworksByPrice(artworks_dep,sort_type)

#Performance & Efficiency
def createSample(listArt,sample_size):
    return model.createSample(listArt,sample_size)

def createPercSample(artlist,percentage):
    return model.createPercSample(artlist,percentage)

def start_endPerfTest():
    return model.start_endPerfTest()