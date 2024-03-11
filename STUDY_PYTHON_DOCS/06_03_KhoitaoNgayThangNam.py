#thuc hanh
class Date:
    day = 0
    month = 0
    year = 0
    def __init__(sefl,day:int,month:int,year:int):
        sefl.day = day
        sefl.month = month
        sefl.year = year
    def getDay(sefl):
        return sefl.day
 
    def getMonth(sefl):
        return sefl.month

    def getYear(sefl):
        return sefl.year

    def setDay(sefl,day):
        sefl.day = day
 
    def setMonth(sefl,month):
        sefl.month = month

    def setYear(sefl,year):
        sefl.year = year

    def setDate(sefl,day,month,year):
        sefl.day = day
        sefl.month = month
        sefl.year = year

    def toString(sefl):
        return str(sefl.day) + '/' + str(sefl.month) + '/' + str(sefl.year)

d = Date(8,3,2024)
print(d.toString())

d.setDay(9)
print(d.toString())