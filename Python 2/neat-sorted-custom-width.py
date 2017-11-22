'''
neat_printer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: List of width between the titles

example:
d = {"egg":["Qty. 1",1],
     "bread":["Qty. 2",2]}

neat_printer(d,["Item","Quantity","Price"],[6,10,10],"Item")

OUTPUT:
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2

neat_printer(d,["Item","Quantity","Price"],[6,10,10],"Price")

OUTPUT:
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2
'''

def neat_printer(dictionary,titles,width,sort_by):
    sortIndex = titles.index(sort_by)
    formatting = ""
    for number in width:
        formatting += "{:<"+str(number)+"}"
    print formatting.format(*titles)
    if sortIndex is not 0:
        for key,value in sorted(dictionary.iteritems(),key=lambda value: value[1][sortIndex-1]):
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            print formatting.format(key,*sv)
    else:
        for key, value in sorted(dictionary.iteritems(), key=lambda value: value[0]):
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            print formatting.format(key, *sv)

'''
neat_writer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: List of width between the titles
file: File you want to write dictionary to

example:
d = {"egg":["Qty. 1",1],
     "bread":["Qty. 2",2]}

file = open("neat_writer.txt", "w")

neat_writer(d,["Item","Quantity","Price"],[6,10,10],file,"Item")

OUTPUT FILE:
Item  Quantity  Price     
egg   Qty. 1    1         
bread Qty. 2    2   
'''

def neat_writer(dictionary,titles,width,file,sort_by):
    sortIndex = titles.index(sort_by)
    formatting = ""
    for number in width:
        formatting += "{:<" + str(number) + "}"
    file.write(formatting.format(*titles))
    file.write("\n")
    if sortIndex is not 0:
        for key,value in sorted(dictionary.iteritems(),key=lambda value: value[1][sortIndex-1]):
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            file.write(formatting.format(key, *sv))
            file.write("\n")
    else:
        for key, value in sorted(dictionary.iteritems(), key=lambda value: value[0]):
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            file.write(formatting.format(key, *sv))
            file.write("\n")
