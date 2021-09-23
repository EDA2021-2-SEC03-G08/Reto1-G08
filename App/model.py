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
import time
import math
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import insertionsort as ins
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

def addArtists(catalog, artists_file, list_type):
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

#Requirement 2
def findArtist(artists,artist_IDs):
    artists_artworks = []
    for artist_ID in (artist_IDs.replace('[','')).replace(']','').split(','):
        pos = 0
        while pos < lt.size(artists):
            artist = lt.getElement(artists,pos)
            if artist['ConstituentID'] == artist_ID:
                artists_artworks.append(artist['DisplayName'])
            pos += 1
    return artists_artworks

def ArtworksInRange(Artworks,StartYear,EndYear,list_type,sample_size):
    artworksInRange = lt.newList(datastructure=list_type)
    sub_list = lt.subList(artworksInRange, 1, sample_size)
    sub_list = sub_list.copy()
    posList = 0
    while posList < lt.size(Artworks):
        Artwork = lt.getElement(Artworks,posList)
        Year = Artwork['DateAcquired']
        if Year >= StartYear and Year <= EndYear:
            lt.addLast(artworksInRange,Artwork)
        posList += 1
    return artworksInRange

def SortArtworks(artworksInRange,sort_type):
    start_time = time.process_time()
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworksInRange,cmpArtworkByDateAcquired)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworksInRange,cmpArtworkByDateAcquired)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworksInRange,cmpArtworkByDateAcquired)
    else:
        sortedList = ms.sort(artworksInRange,cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sortedList

#Requirement 3
def encounterArtist(artists,artist_name):
    for artist in lt.iterator(artists):
        if artist['DisplayName'] == artist_name:
            return artist['ConstituentID']
    return 'NotFound'

def artistMediumInfo(artworks,artist_ID,list_type):
    mediums = {}
    maxIteUses = 0
    artist_mediums = 0
    artist_artworks = 0
    for artwork in lt.iterator(artworks):
        if artwork['ConstituentID'] == '[' + artist_ID + ']':
            artist_artworks += 1
            medium = artwork['Medium']
            if medium not in mediums:
                artist_mediums += 1
                mediums[medium] = lt.newList(datastructure=list_type)
                lt.addLast(mediums[medium],artwork)
                if maxIteUses == 0:
                    maxIteUses = 1
                    mostUsed = medium
            else:
                lt.addLast(mediums[medium],artwork)
                IteUses = lt.size(mediums[medium])
                if IteUses > maxIteUses:
                    maxIteUses = IteUses
                    mostUsed = medium
    return artist_artworks, artist_mediums, mostUsed, mediums[mostUsed]

#Requirement 5
def estimatePrice(artwork):
    measurements = ['Diameter (cm)','Height (cm)','Length (cm)','Weight (kg)','Width (cm)']
    enc_info = {}
    weight = 0
    radius = 0
    for measurement in measurements:
        if artwork[measurement] != '':
            if measurement == 'Weight (kg)':
                weight = artwork[measurement]
            elif measurement == 'Diameter (cm)':
                radius = artwork[measurement]/200
            else:
                amount = float(artwork[measurement])
                enc_info[measurement] = amount/100
    
    max_price = 0.0

    #Weight
    if weight != 0:
        if weight * 72 > max_price:
            max_price = weight * 72
    
    #Areas and Volumes with Radius
    if radius > 0:
        if len(list(enc_info.keys())) > 0:
            price = 0
            for measure in list(enc_info.keys()):
                price = (enc_info[measure]*radius*math.pi*2 + math.pi*radius**2)*72
                if price > max_price:
                    max_price = price
                price = (enc_info[measure]*math.pi*radius**2)*72
                if price > max_price:
                    max_price = price
        else:
            price = 4*math.pi*radius**2
            if price > max_price:
                    max_price = price
            price = (4*math.pi*radius**3)/3
            if price > max_price:
                    max_price = price
    #Areas
    elif len(list(enc_info.keys())) > 1:
        i = 0
        while i < len(list(enc_info.keys())) - 1:
            j = i + 1
            while j < len(list(enc_info.keys())): 
                M1 = enc_info[list(enc_info.keys())[i]]
                M2 = enc_info[list(enc_info.keys())[j]]
                price = M1*M2*72
                if price > max_price:
                    max_price = price
                j += 1
            i += 1
    #Volumes
    elif len(list(enc_info.keys())) > 2:
        i = 0
        while i < len(list(enc_info.keys())) - 2:
            j = i + 1
            while j < len(list(enc_info.keys()))-1: 
                k = j +1 
                while k < len(list(enc_info.keys())): 
                    M1 = enc_info[list(enc_info.keys())[i]]
                    M2 = enc_info[list(enc_info.keys())[j]]
                    M3 = enc_info[list(enc_info.keys())[k]]
                    price = M1*M2*M3*72
                    if price > max_price:
                        max_price = price
                    k += 1
                j += 1
            i += 1
    
    if max_price == 0.0:
        max_price = 48.0
    
    return max_price

def checkDeparment(artworks,department):
    encountered = False
    pos = 0
    while not encountered and pos < lt.size(artworks):
        artwork = lt.getElement(artworks,pos)
        if artwork['Department'] == department:
            encountered = True
        pos += 1
    return encountered

def moveDepartment(artworks,department,list_type):
    art2trans = 0
    est_price = 0
    est_weight = 0
    artworks_dep = lt.newList(datastructure=list_type)

    pos = 0
    while pos < lt.size(artworks):
        artwork = lt.getElement(artworks,pos)
        if artwork['Department'] == department:
            price = estimatePrice(artwork)
            if artwork['Weight (kg)'] != '':
                est_weight += float(artwork['Weight (kg)'])
            est_price += price
            art2trans += 1
            artwork['EstPrice'] = price
            lt.addLast(artworks_dep,artwork)
        pos += 1
    return est_price, art2trans, est_weight, artworks_dep

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    return artwork1["DateAcquired"] < artwork2['DateAcquired']

def cmpArtworkByDate(artwork1, artwork2): 
    return artwork1["Date"] < artwork2['Date']

def cmpArtworkByEstPrice(artwork1, artwork2): 
    return artwork1["EstPrice"] > artwork2['EstPrice']

def artworksWithDate(artworks_dep,list_type):
    artworksWithDate = lt.newList(datastructure=list_type)
    for artwork in lt.iterator(artworks_dep):
        if artwork['Date'] != '':
            lt.addLast(artworksWithDate,artwork)
    return artworksWithDate
 
def SortArtworksByDate(artworks_dep,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworks_dep,cmpArtworkByDate)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworks_dep,cmpArtworkByDate)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworks_dep,cmpArtworkByDate)
    else:
        sortedList = ms.sort(artworks_dep,cmpArtworkByDate)
    return sortedList

def SortArtworksByPrice(artworks_dep,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworks_dep,cmpArtworkByEstPrice)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworks_dep,cmpArtworkByEstPrice)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworks_dep,cmpArtworkByEstPrice)
    else:
        sortedList = ms.sort(artworks_dep,cmpArtworkByEstPrice)
    return sortedList


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento