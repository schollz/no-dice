# no-dice

Using a pen and paper to generate random numbers, in cases you don't have dice.

![Image](https://user-images.githubusercontent.com/6550035/29104256-a93dc2b0-7c81-11e7-9a72-3063d3191d01.jpg)

## Step to generate a dice "roll" from a squiggle

1. Draw a squiggle.
2. (optional, if your friend believes you are rain man) Have a friend draw a squiggle on top of yours.
3. Count the number of times lines intersect in your squiggle
4. Take that number and divide by the dice size (e.g. 6 for 6-sided dice).
5. Take the remainder and add 1. That is your roll!

## Pseudo-validation using computation

Generate random squiggles using bezier curves (which are kind like real squiggles).

```
$ python3 -W ignore bezier.py
```

Check if it passes the tests

## Validation using actual squiggles (TBD)
