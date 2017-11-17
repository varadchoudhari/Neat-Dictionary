'''
neat_printer
params dictionary: The dictionary you want to print
titles: Titles you want to give for the table
width: Width between the titles

example:
d = {"egg":["Qty. 1",1],
     "bread":["Qty. 2",2]}

neat_printer(d,["Item","Quantity","Price"],10)

OUTPUT:
Item      Quantity  Price
egg       Qty. 1    1
bread     Qty. 2    2
'''

def neat_printer(dictionary,titles,width):
    formatting = ""
    for i in range(0,len(titles)):
        formatting += "{:<"+str(width)+"}"
    print formatting.format(*titles)
    for key,value in dictionary.iteritems():
        sv = []
        for subvalue in value:
            sv.append(subvalue)
        print formatting.format(key,*sv)
