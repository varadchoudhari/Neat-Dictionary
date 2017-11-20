'''
neat_printer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: Width between the titles

example:
d = {"egg":["Qty. 1",1],
     "bread":["Qty. 2",2]}

neat_printer(d,["Item","Quantity","Price"],[6,10,10])

OUTPUT:
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2
'''

def neat_printer(dictionary,titles,width):
    formatting = ""
    for number in width:
        formatting += "{:<"+str(number)+"}"
    print formatting.format(*titles)
    for key,value in dictionary.iteritems():
        sv = []
        for subvalue in value:
            sv.append(subvalue)
        print formatting.format(key,*sv)

'''
neat_writer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: Width between the titles
file: File you want to write dictionary to

example:
d = {"egg":["Qty. 1",1],
     "bread":["Qty. 2",2]}

file = open("neat_writer.txt", "w")

neat_writer(d,["Item","Quantity","Price"],[6,10,10],file)

OUTPUT FILE:
Item  Quantity  Price     
egg   Qty. 1    1         
bread Qty. 2    2   
'''

def neat_writer(dictionary,titles,width,file):
    formatting = ""
    for number in width:
        formatting += "{:<" + str(number) + "}"
    file.write(formatting.format(*titles))
    file.write("\n")
    for key, value in dictionary.iteritems():
        sv = []
        for subvalue in value:
            sv.append(subvalue)
        file.write(formatting.format(key, *sv))
        file.write("\n")