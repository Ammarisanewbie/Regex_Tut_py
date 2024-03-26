# Regex_Tut_py
This is a Python Regular Expression Tutorial that can help in filtering and automation of log files in Cybersecurity 
Check out the Regex.py file when you're done reading through for a concise application example.

## Introduction
Learning regular expressions(Regex) in Python equips you with a powerful tool for text processing, data validation, and manipulation tasks, allowing you to efficiently work with textual data.

## Software Used
- Vscode

## Learning Objectives
1.Importing Regex library
2. Symbols for Character types
3. Symbols to Quantify Occurrences
4. Basic Regex Functions
5. Constructing Regex Patterns

## 1. Installation
To use Regex and its functions, we need to import the `re` library

``` python
import re
```

## 2.Symbols for Character types
1. '\w' : matches with any alphanumeric char only. (includes '_',underscore) 
    eg: user1@email1.com = \w+@\w+\.\w+ ->typical email Regex

2. '.' : matches all char including symbols

3. '\d' : matches to all single digits (0-9)

4. '\s' : matches to all single spaces

5. '\.' : matches to the period char (.)

## 3.Symbols to Quantify Occurrences
1. '+' : matches one or more of the following character
    eg ("\d+", "h32rb17") > ['32', '17']

2. '*' : matches 0, 1 or more occurances of specific char
    eg ("\d*", "h32rb17") > ['', '32', '', '', '17', '']
    
3. '{ }' :specific number of repetitions to allow is placed in the '{}'
   - specify a range within the {} brackets by separating two numbers(1st: min reps, max reps) with a comma
    eg ("\d{2}", "h32rb17 k825t0m c2994eh") > ['32', '17', '82', '29', '94']

4. {x,y}: range
  - x: min number, y: max number of repetitions 
  - `("\d{1,3}", "h32rb17 k825t0m c2994eh")` : ['32', '17', '825', '0', '299', '4']

## 4.Basic Regex Functions
`re.findall(1st, 2nd)`
 - returns a list of matches to a regex
 - takes in 2 parameters (1st: string containing the regex pattern, 2nd: string that you're searching through)
 - *include `r` or `\` to bypass the escape sequence eg:`(r"\w")`

## 5.Constructing Regex Patterns
- Break down the pattern searching for into smaller chunks
- represent chunks using regex symbols

#### Example 1: Extract username and login attempts, without ID or department
```python
employee_logins = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"*
pattern = "\w+:\s\d+"

re.findall(patternm employee_logins)
```

#### Example 2: Find devices beginning with 'r15'
```python
devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253e78b ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"
pattern = "r15\w+"

re.findall(pattern,devices)
```

## Key Notes
- Match what you wish to search for with the position too, it's like matching or looking out for the pattern game.
- Noticed in [Example 2](#Example 2: Find devices beginning with 'r15')



