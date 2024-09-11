# Element of Programming
Programming language must have the following features:
* **primitive expressions and statements**, represent the simplest buildin block of the language.
* **means of combination**, combinining elements or expressions or simple to complex.
* **means of abstraction**, compound elements are named and manipulated as units.

## Expressions
```python
>>> 45
45
>>> 10
10
```
The code above are called expressions, they are specifically called _primitive expression_.

## Call Expressions
This means we apply a function to arguments. As an example, the operator or function ```add``` below map its input to a single output. 
```python
add(1+1, 3)
```
In the code above ```add``` is an operator. The value inside parenthesis is the arguments, in this case they act as operands. Evaluate the operator and then the operand of sub-expressions. In the above case, ```add``` will be evaluated first, after that ```1 + 1```, then ```3```. After all sub-expressions are evaluated, they then applied to the ```add``` operator (function). Finaly, the result of this expression is ```5```. 

## Names and the Environment
Consider the following code:
```python
f = min
f = max
g, h = min, max
max = g

max(f(2, g(h(1, 5), 3)), 4)
```
In the code above, we assign or bind a value to a name. In the first line, we bind the function `min` to a name (`f`). So now, `f` equals to `min` which means that whenever we call `f`, the function of `min` is applied to it. 

## Nested procedure
To really understand about _nested procedure_, we need to procedurally. 
Consider the following:
```python
mul(add(4, mul(4, 6)), add(3, 5))
```
In the above code, we use simple expression to solve a complex operation by combining them.  The procedure of evaluation is similar to the previous expression in *call expression* part. 

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
