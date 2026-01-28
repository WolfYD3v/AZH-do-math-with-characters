# The Official AAZH's Documentation!!!!!!§!§!§§§!!!!§

## How AZH manage numbers (it's important)
AZH can manage numbers, while they don't have decimals. To tell AZH what number you want it to use you have to write it as a bit, with letters only.
Here is an example of a bit:
```
01100101
```
But how can you do this very simple thing?

## The syntax of AZH
A bit is composed of 8 octets, to add one octet typing "a" is the solution. AZH register a bit when 8 octet are added, or when the aded octet is reversed. \
Important note: When AZH start interpreting your code, the base octet added is 1.

To invert the added octet, "b" is here.
1 becomes 0, and 0 becomes 1.

Here is an example to help you understand AZH's logic:
```
Input: aabaabaaaaba -> Output: 11001111

AZH read the input character by character from the left, to the right.
The following table shows how the interpretation work:
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

"c" tells to AZH to make an addition in the math process, because yes, AZH do math!

"d" tells to AZH to make an soustraction in the math process

## The stack of AZH
AZH work with a stack, that is empty.
To fill the stack, typing the following line in the main() function of the (main.py file)[main.py]
``` python
azh_interpretor.add_data_to_stack("your AZH great and amazing code")
```
Here is an example to help:
``` py
def main():
    azh_interpretor.add_data_to_stack("aabababbabc")
    azh_interpretor.add_data_to_stack("abbaac")
    azh_interpretor.add_data_to_stack("dbbaaabaa")

    azh_interpretor.interpret_stack()

# "azh_interpretor.interpret_stack()" will tell the interpreter to interpret the stack
```

## Testing
To test/run your AZH code, you can type in your terminal one of the following commands:
``` bash
./run.sh
```
``` bash
uv run main.py
```

The estimated output in your terminal is:
```
STACK | Current state -> ['aabababbabc']
STACK | Current state -> ['aabababbabc', 'abbaac']
STACK | Current state -> ['aabababbabc', 'abbaac', 'dbbaaabaa']

BINARY OUTPUTS BEFORE VALIDATION -> ['11011', '000', '0001']
Validating binary outputs...
Binary outputs validated! -> ['11111011', '11111000', '11110001']
Operators listed: ['+', '+', '-']

Decrypting binary outputs...
251
248
241

Doing some math...
258
```
