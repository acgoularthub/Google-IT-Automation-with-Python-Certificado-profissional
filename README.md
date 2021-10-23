## Google IT Automation with Python Certificado profissional

### Methods

* .lower()
  
  usage:
  ```python
  >>>"You".lower()
  you
  >>>
  ```
* .upper()
    
  usage:
  ```python
  >>>"You".upper()
  YOU
  >>>
  ```
* .strip()
    
  usage:
  ```python
  >>>"In case of".strip()
  Incaseof
  >>>
  ```

  also can be used like `.lstrip()` to wipe all spaces on left of the word and `.rstrip()` to do the same in the right of the word.

* .count()
    
  usage:
  ```python
  >>>"You are amazing".count("a")
  3
  >>>
  ```

* .endswith()
    
  usage:
  ```python
  >>>"You".endswith("ou")
  True
  >>>
  ```

  * .isnumeric()
    
  usage:
  ```python
  >>>"You".isnumeric()
  False
  >>>
  ```

  * .join()
    
  usage:
  ```python
  >>>" ".join(['This', 'is', 'a', 'phrase', 'joined', 'by', 'spaces'])
  'This is a phrase joined by spaces'
  >>>
  ```

  * .split()
  
  ```python
  >>>"You are awesome".split()
  ['You', 'are', 'awesome']
  >>>
  ```

### Notes

- we can use "{ }" as masks to interact with a text like in the following example:

```python
name = "Elliot"
number = len(name) * 3
print("Hello {}, your lucky number is {}!".format(name, number))
```
and, as the result, we have this:

`Hello Elliot, your lucky number is 18!`

and we also can use like this:

```python

name = "Elliot"
number = len(name) * 3
print("Hello {name}, your lucky number is {number}!".format(name=name, number=number))
```

in this way in not needed to put the function `.format()` in the same order that of the masks, 'cause we are using declared placeholders.

