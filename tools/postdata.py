from config.configuration import collection

def insert_line(linenumber, character, place, 
time, line, wordcount, message):
    dict_insert = {"Line number": linenumber,
    "Character": character,
    "Place": place,
    "Time": time,
    "Line": line,
    "Word count": wordcount,
    "Message": message, 
    }
    collection.insert_one(dict_insert)