# Neat-Dictionary
A simple Python implementation to pretty print dictionaries

Works with Python 2

What's inside
---
* neat_printer

...and more are coming!

How to use
---
```python
dictionary = {egg: ["Qty. 1", 1],
              bread: ["Qty. 2", 2]}

```
```python
neat_printer(dictionary,["Item","Quantity","Price"],10)
```
OUTPUT when width == 10:
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
