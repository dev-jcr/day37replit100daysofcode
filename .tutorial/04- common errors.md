# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## It stops printing too early

👉 Why is it printing 'Hell' instead of 'Hello'?


```python
myString = "Hello there my friend."
print(myString[0:4])
```

<details> <summary> 👀 Answer </summary>

- The second argument should always be **one more** than the index of the final character.

```python
myString = "Hello there my friend."
print(myString[0:5])
```

</details>

## It won't stop printing the same character

👉 What is the problem here?
```python
myString = "Hello there my friend."
print(myString[0:4:0])
```

<details> <summary> 👀 Answer </summary>

The 0 in the third argument means 'move on 0 characters in the string each time'.  You've told it to print the same character again and again and again....

The third argument should be **at least 1**.
```python
myString = "Hello there my friend."
print(myString[0:4:1])
```


</details>

