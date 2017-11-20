'''
multiline_printer
params dictionary: Dictionary that you want to print
titles: Titles you want to give for the table
width: Width between the titles

example:
d = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
     "bread":[["Qty. 2",2], ["Qty. 3",3]]}

multiline_printer(d,["Item","Quantity","Price"],[6,10,10])

OUTPUT:
Item  Quantity  Price
egg   Qty. 1    1
egg   Qty. 2    2
egg   Qty. 4    3
bread Qty. 2    2
bread Qty. 3    3
'''

def multiline_printer(dictionary,titles,width):
    formatting = ""
    for number in width:
        formatting += "{:<" + str(number) + "}"
    print formatting.format(*titles)
    for key, value in dictionary.iteritems():
        if isinstance(value[0],list):
            for sublist in value:
                sv = []
                for subvalue in sublist:
                    sv.append(subvalue)
                print formatting.format(key,*sv)
        else:
            sv = []
            for subvalue in value:
                sv.append(subvalue)
            print formatting.format(key, *sv)
