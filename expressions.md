# Anatomy of a call expressions
```python
add(1+1, 3)
```
In the code above ```add``` is an operator. The value inside parenthesis is the arguments, in this case they act as operands. Evaluate the operator and then the operand of sub-expressions. In the above case, ```add``` will be evaluated first, after that ```1 + 1```, then ```3```. After all sub-expressions are evaluated, they then applied to the ```add``` operator (function). Finaly, the result of this expression is ```5```. 

## Nested procedure
Consider the following:
```python
mul(add(4, mul(4, 6)), add(3, 5))
```
In the above code, we use simple expression to solve a complex operation by combining them.  The procedure of evaluation is similar to the previous expression. 

## Type of expressions
1) Primitive Expression
    * 2     : numeral
    * add   : name
    * 'Hello'   : string
2) Call Expression
    ```python
    max(2, 3)
    ```
    * max   : operator
    * 2, 3  : operands. 

## Assignment 
```python
f = min
f = max 
g, h = min, max
max = g

max(f(2, g(h(1, 5), 3)), 4)
```
