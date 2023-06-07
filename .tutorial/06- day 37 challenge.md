# 👉 Day 37 Challenge

This _is_ the challenge you're looking for.  This program will generate your Star Wars Name.

1. Ask the user to input their first & last names.
2. Slice the first 3 letters of the first name.
3. Slice the first 3 letters of the last name (surname).
4. Join them together. Ideally change the case so that it looks good - think fStrings or `.upper()/.lower()`.  This is the user's Star Wars first name.
5. Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.) 
6. Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name.  Remember, fStrings and `.upper()/.lower()`.
7. Finally, `print` them both as part of a sentence.

🥳 Extra points for getting all the inputs with just one `input` command and the `split` function.

Example:

```
🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff
```

<details> <summary> 💡 Hints </summary>
  
- To get charaters from the beginning of a string, leave the first argument blank. ex: [:3] gets the first 3 characters.
- To get charaters from the end of a string, make the first argument a negative number for how many charaters to get. Leave the last argument blank.  ex: [-5:] gets the last 5 characters.
- fString formatting uses `.title` for first character capitalization and `.lower` for all lower case.
- Use fStrings to join the sliced characters to a new variable as you get the correct characters from each string.
- For extra points, get the user to input all info at once separated by spaces. 




</details>