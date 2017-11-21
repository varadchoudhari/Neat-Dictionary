# Neat-Dictionary
A simple Python implementation to pretty print dictionaries

Works with Python 2

What's inside
---
1. neat-dictionary-fixed-column-width.py
   * neat_printer
   * neat_writer
2. neat-dictionary-custom-column-width.py
   * neat_printer
   * neat_writer
3. neat-multiline-custom-width.py
   * multiline_printer
   * multiline_writer
4. neat-multiline-fixed-width.py
   * multiline_printer
   * multiline_writer

...and more are coming!

How to use
---
#### neat-dictionary-fixed-column-width.py

_neat_printer(dictionary_variable,[list_of_titles],column_width)_
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
neat_printer(dictionary,["Item","Quantity","Price"],10)
```
OUTPUT
```
Item      Quantity  Price
egg       Qty. 1    1
bread     Qty. 2    2
```
```python
neat_printer(dictionary,["Item","Quantity","Price"],20)
```
OUTPUT when width == 20:
```
Item                Quantity            Price               
egg                 Qty. 1              1                   
bread               Qty. 2              2                   
```
_neat_writer(dictionary_variable,[list_of_titles],column_width,output_file)_
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
file = open("neat_writing.txt", "w")
neat_writer(dictionary, ["Item","Quantity","Price"], 10, file)
```
OUTPUT FILE:
```
Item      Quantity  Price
egg       Qty. 1    1
bread     Qty. 2    2
```

#### neat-dictionary-custom-column-width.py

_neat_printer(dictionary_variable,[list_of_titles],[list_of_column_width])_
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
neat_printer(dictionary,["Item","Quantity","Price"],[6,10,10])
```
OUTPUT
```
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2
```

_neat_writer(dictionary_variable,[list_of_titles],[list_of_column_width],file)_
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
file = open("neat_writing.txt", "w")
neat_writer(dictionary, ["Item","Quantity","Price"], [6,10,10], file)
```
OUTPUT FILE:
```
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2
```

#### neat-multiline-custom-width.py

_multiline_printer(dictionary_variable,[list_of_titles],[list_of_column_width])_
```python
dictionary = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
              "bread":[["Qty. 2",2], ["Qty. 3",3]]}
```
```python
multiline_printer(dictionary,["Item","Quantity","Price"],[6,10,10])
```
OUTPUT
```
Item  Quantity  Price
egg   Qty. 1    1
egg   Qty. 2    2
egg   Qty. 4    3
bread Qty. 2    2
bread Qty. 3    3
```

_multiline_writer(dictionary_variable,[list_of_titles],[list_of_column_width],output_file)_
```python
dictionary = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
              "bread":[["Qty. 2",2], ["Qty. 3",3]]}
```
```python
file = open("multiline_writing.txt", "w")
multiline_writer(dictionary,["Item","Quantity","Price"],[6,10,10],file)
```
OUTPUT FILE
```
Item  Quantity  Price
egg   Qty. 1    1
egg   Qty. 2    2
egg   Qty. 4    3
bread Qty. 2    2
bread Qty. 3    3
```
#### neat-multiline-fixed-width.py

_multiline_printer(dictionary_variable,[list_of_titles],column_width)_
```python
dictionary = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
              "bread":[["Qty. 2",2], ["Qty. 3",3]]}
```
```python
multiline_printer(dictionary,["Item","Quantity","Price"],10)
```
OUTPUT
```
Item      Quantity  Price
egg       Qty. 1    1
egg       Qty. 2    2
egg       Qty. 4    3
bread     Qty. 2    2
bread     Qty. 3    3
```

_multiline_writer(dictionary_variable,[list_of_titles],column_width,output_file)_
```python
dictionary = {"egg":[["Qty. 1",1], ["Qty. 2",2], ["Qty. 4",3]],
              "bread":[["Qty. 2",2], ["Qty. 3",3]]}
```
```python
file = open("multiline_writing.txt", "w")
multiline_writer(dictionary,["Item","Quantity","Price"],10,file)
```
OUTPUT
```
Item      Quantity  Price
egg       Qty. 1    1
egg       Qty. 2    2
egg       Qty. 4    3
bread     Qty. 2    2
bread     Qty. 3    3
```
