# 🫧 BubbleLan Programming Language

A simple toy programming language written in Python with its own syntax, REPL and file execution system. Supports variables, lists, arithmetic operations, conditionals, and loops.

### Run a BubbleLan file:
```bash
python bubblelan.py hello.bub
```

### Start interactive REPL:
```bash
bubblelan 
```

## Language Features

### Variables & Data Types
```python
# Numbers
x = 10
age = 25

# Strings (double quotes)
name = "Alice"
message = "Hello World"

# Lists
nums = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 42]
```

### Arithmetic Operations
```python
x = 10 + 5      # Addition
x = 10 - 3      # Subtraction
x = 4 * 5       # Multiplication
x = 20 / 4      # Division
x = 2 + 3 * 4   # Respects precedence
```

### String Operations
```python
greeting = "Hello " + "World"
message = "Hi " + name
```

### List Operations
```python
l = [10, 20, 30, 40]
say l[0]        # prints 10
say l[2]        # prints 30
x = l[1]        # x = 20
```

### Comparisons
```python
x == 5          # Equal to
x != 5          # Not equal to
x < 10          # Less than
x > 10          # Greater than
```

### Conditionals
```python
if x > 0 then say "positive" else say "negative"

if age == 18 then say "Adult" else say "Minor"
```

#### For loop
```python
nums = [1, 2, 3, 4, 5]
for n in nums: say n

names = ["Alice", "Bob"]
for name in names: say name

for i from 1 to 5: say i          # prints 1, 2, 3, 4, 5
for i from 0 to 10: say i * i     # prints squares
```

### Output
```
say 42
say "Hello"
say x
say l[0]
```

## File Structure

```
bubbleLan/
├── bubblelan.py       # Main runner 
├── lexer.py           # Tokenizer
├── new_parser.py      # Parser
├── interpreter.py     # Interpreter
├── my_ast.py          # AST node definitions
└── README.md
```

