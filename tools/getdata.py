from config.configuration import db, collection

def get_char():
    """
    Function that returns all distint characters from the database
    """
    query = {}
    quotes = list(collection.distinct("Character"))
    return quotes

def get_char_script(char):
    """
    Función que devuelve todas las frases de alguno de los personajes de la película
    """ 
    query= {"Character":f"{char}"}
    frases=list(collection.find(query,{"_id":0, "Time":0, "Place":0,"Word count":0,"Character":0, "Line number":0}))
    return frases

def get_time():
    """
    Function that returns all distint times from the database
    """
    query = {}
    quotes = list(collection.distinct("Time"))
    return quotes

def get_time_script(time):
    """
    Función que devuelve todas las frases de la película en función del momento del día en el que se hayan dicho
    """ 
    query= {"Time":f"{time}"}
    frases=list(collection.find(query,{"_id":0, "Place":0,"Word count":0,"Character":0,"Line number":0,"Time":0}))
    return frases

def get_place():
    """
    Function that returns all distint places from the database
    """
    query = {}
    quotes = list(collection.distinct("Place"))
    return quotes

def get_place_script(place):
    """
    Función que devuelve todas las frases de la película en función del momento del día en el que se hayan dicho
    """ 
    query= {"Place":f"{place}"}
    frases=list(collection.find(query,{"_id":0, "Place":0,"Word count":0,"Character":0,"Line number":0,"Time":0,}))
    return frases   

