# AZH, a fully letered mathematic language

Welcome to the AZH Project, where you can simple math operation with only letters at your disposition. From A to Z, by passing to H.

We've all been told in school that mathematic operation doesn't only use number or operationnal symbols, letters are used too. And between you and me letters are superior.

So why not do math operations with only letters? This is AZH!


## The Project Itself
Made with Python, AZH is a troll language I have created. Why you may ask...

Because why not.


## Use AZH
- AZH have some contrains, to create an AZH project you have to have a local copy of the repository on your system. You also need [uv](https://github.com/astral-sh/uv) installed ([uv](https://github.com/astral-sh/uv) is better than pip)
- All your project files should be stored in the [project_files](project_files) folder (for a better organisation)
- Use [main.py](main.py) to run you project
- To create a new AZH project, you need a new fresh copy of the repository
- Wanted to upgrade your AZH project to the latest version of AZH? You need a new fresh copy of the repository too
- AZH will tell you when you made a mistake when he want to
- You have to fill the AZH stack everytime you want to test your code, normal AZH behavoir


## The Official Documentation
AZH can manage numbers, while they don't have any decimal. To tell AZH what number you want it to use you have to write it as a bit, with letters only.

How can you do? It's very easy :)

```
Typing "a" adds a octet.
When AZH start interpreting your code, the base octet added is 1.
AZH register a bit when 8 octet are added.
```
```
You can change the octet added by typing "b".
So 1 becomes 0, and 0 becomes 1.
```
Here is an example to help you understand AZH's logic:
```
Input "aabaabaaaaba", and AZH will interpret, and outputt "11001111"

AZH read the input character by character from the left, to the right.
```
|Character readed|Action                 |Output   |
|----------------|-----------------------|---------|
|NONE            |NONE                   |NONE     |
|a               |Octet 1 added          |1        |
|a               |Octet 1 added          |11       |
|b               |Octet added is set to 0|11       |
|a               |Octet 0 add            |110      |
|a               |Octet 0 add            |1100     |
|b               |Octet added is set to 1|1100     |
|a               |Octet 1 add            |11001    |
|a               |Octet 1 add            |110011   |
|a               |Octet 1 add            |1100111  |
|a               |Octet 1 add            |11001111 |
|NONE            |Bit register           |NONE     |
|b               |Octet added is set to 0|NONE     |
|a               |Octet 0 add            |0        |

```
To fill the stack, you can type in main.py this: azh_interpretor.add_data_to_stack("your code")
For example:

def main():
    azh_interpretor.add_data_to_stack("aabaabaaaaba")
    azh_interpretor.add_data_to_stack("abaababaa")
    azh_interpretor.add_data_to_stack("aaabaabaabaaba")

    azh_interpretor.interpret_stack()

azh_interpretor.interpret_stack() will tell the interpreter to interpret the stack
```
## Upcoming Features
- The AZH official file format, to write AZH code without filling manually the stack every time you want to test your AZH script
