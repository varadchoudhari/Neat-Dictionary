# Neat-Dictionary
A simple Python implementation to pretty print dictionaries

Works with Python 2

What's inside
---
* neat_printer
* neat_writer

...and more are coming!

How to use
---
**neat-dictionary-fixed-column-width.py**

neat_printer
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
neat_writer
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
file = open("neat_writing.txt", "w")
neat_writer(dictionary, ["Item","Quantity","Price"], 10, file)
```
OUTPUT neat_writing.txt
```
Item      Quantity  Price
egg       Qty. 1    1
bread     Qty. 2    2
```

**neat-dictionary-custom-column-width.py**

neat_printer
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

neat_writer
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}
```
```python
file = open("neat_writing.txt", "w")
neat_writer(dictionary, ["Item","Quantity","Price"], [6,10,10], file)
```
OUTPUT neat_writing.txt
```
Item  Quantity  Price
egg   Qty. 1    1
bread Qty. 2    2
```
