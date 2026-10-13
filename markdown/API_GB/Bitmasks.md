---
title: "Bitmasks"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/Bitmasks.htm"
---

# Bitmasks

Bitmasks are essentially bitwise comparisons. Understanding how bitmasks work might make more sense if you think of their binary representation.

The binary representation of the decimal number 1 is 0001, 2 is 0010, 4 is 0100, etc.

Think of each bit as a switch. For example, the decimal number 5 in binary is 0101. The third bit (0100) is on and the first bit (0001) is on. So, 0101 = 0100 + 0001.

If a SOLIDWORKS PDM Professional enumerator has a bitmask like the following:

| Decimal | Option | Binary |
| --- | --- | --- |
| 1 | OptionA | 0001 |
| 2 | OptionB | 0010 |
| 4 | OptionC | 0100 |
| 8 | OptionD | 1000 |

and you want OptionA and OptionC on, then add their two values together:

| Decimal | Option | Binary |
| --- | --- | --- |
| 1 | OptionA | 0001 |
| + 4 | OptionC | 0100 |
| = 5 |  | 0101 |
