# Hands-on Python Problems

This repository contains a collection of hands-on Python problems that cover various topics, including strings, lists, tuples, and dictionaries. 

## List of Problems:

### Dictionary translator

This Python program reads an integer 'n' on the first line, which represents the total number of words in the dictionary. The following 'n' lines each contain two words, indicating that the second word is the translation of the first word. The next line consists of a sentence containing multiple words separated by spaces. The goal is to write a translator program that reads the dictionary and the corresponding sentence as input, and translates the sentence accordingly. During the translation process, if a word is not found in the dictionary, the word itself should be printed in the output.

#### Sample Input:
```
5
hello salam
goodbye khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight
```
#### Sample Output:
```
ma goftan khodafez to shoma tonight
```
Please refer to the sample input and output for further clarification.

### Palindrome
This program determines whether a word is a palindrome by checking if it reads the same forwards and backwards, and outputs the result accordingly.

### Vote Counting System

This program is a vote counting system that counts the total number of votes for each country. The input consists of several lines, where the first line represents the total number of votes, denoted by `n`. The following `n` lines contain the names of the countries. The country names are composed of lowercase English letters.

The program outputs `m` lines, each line displaying the number of votes for a specific country. The country names are written in alphabetical order. 

#### Sample Input:

```
5
spain
hungary
argentina 
spain
spain
```

#### Sample Output:

```
argentina 1
hungary 1
spain 3
```
### Find the Largest(Second-Largest)

This is a program that reads ages from input and prints the largest (and second-largest) age(ages). The program continues reading from the input until -1 is entered. 

### Guess The Number
In this game:

1. The user thinks of a number between 1 and 99 without telling the computer.

2. The program guesses a number and displays it.

3. Based on the displayed number, the user responds with one of the following inputs:

   - Typing 'k' if the user's number is smaller.
   - Typing 'b' if the user's number is larger.
   - Typing 'd' if the guess is correct.

4. If the user types 'k', the program makes a smaller guess.
   If the user types 'b', the program makes a larger guess.
   If the user types 'd', the game ends.

The program continues making guesses until the correct number is guessed with the 'd' input.


### Number with Maximum Divisors

This project aims to find the number with the highest number of divisors among 20 input numbers.The program then prints the number with the maximum divisors and its count as the output.

### Print Equation in Order

This Python program takes an input equation and rearranges the numbers in the equation to ensure they are in non-descending order. The numbers involved in the equation are limited to 1, 2, and 3 for simplicity.
