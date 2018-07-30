import re

#Class for the folder movie
class Movie:
    __folder = ""
    __movieName = ""
    __releaseYear = ""
    __movieType = ""
    __Sound = ""
    __video = ""
    
    #Constructor for the class 
    def __init__(self, folder):
        m = re.search("([a-zA-Z0-9\.]+)\.(\d{4})\.([0-9]+p)\.([a-zA-Z0-9\.-]+)\.([a-zA-Z0-9]+)", folder)
        self.__movieName = m.group(1).replace(".", "-").lower()
        self.__folder = folder
        self.__releaseYear = m.group(2)

    def getMovieName(self):
        return self.__movieName

    def getFolder(self):
        return self.__folder

    def getReleaseYear(self):
        return self.__releaseYear
