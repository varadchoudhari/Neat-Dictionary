'''
multiline_printer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: Width between the titles

example:
d = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
     "bread":[["Qty. 2",2], ["Qty. 3",3]]}

multiline_printer(d,["Item","Quantity","Price"], 10)

OUTPUT:
Item      Quantity  Price
egg       Qty. 1    1
egg       Qty. 2    2
egg       Qty. 4    3
bread     Qty. 2    2
bread     Qty. 3    3
'''

def multiline_printer(dictionary,titles,width):
    formatting = ""
    for i in range(0,len(titles)):
        formatting += "{:<" + str(width) + "}"
    print formatting.format(*titles)
    for key, value in dictionary.iteritems():
        if isinstance(value[0],list):
            for sublist in value:
                sv = []
                for subvalue in sublist:
                    sv.append(subvalue)
                print (formatting.format(key,*sv))
        else:
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            print (formatting.format(key, *sv))
'''
multiline_writer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: Width between the titles
file: File you want to write dictionary to

example:
d = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
     "bread":[["Qty. 2",2], ["Qty. 3",3]]}

file = open("multiline_writer.txt", "w")

multiline_writer(d,["Item","Quantity","Price"], 10, file)

OUTPUT FILE:
Item      Quantity  Price     
egg       Qty. 1    1         
egg       Qty. 2    2         
egg       Qty. 4    3         
bread     Qty. 2    2         
bread     Qty. 3    3  
'''

def multiline_writer(dictionary, titles, width, file):
    formatting = ""
    for i in range(titles):
        formatting += "{:<" + str(width) + "}"
    file.write(formatting.format(*titles))
    file.write("\n")
    for key, value in dictionary.iteritems():
        if isinstance(value[0],list):
            for sublist in value:
                sv = []
                for subvalue in sublist:
                    sv.append(subvalue)
                file.write(formatting.format(key,*sv))
                file.write("\n")
        else:
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            file.write(formatting.format(key, *sv))
            file.write("\n")
