---
title: "Bitmasks"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Bitmasks.htm"
---

# Bitmasks

A Bitmask is a set of binary representations of decimal numbers. Some SOLIDWORKS enumerators are bitmasks that enable you to turn on multiple options simultaneously. Two or more options in a bitmask are enabled by simply adding their values together.

For example, if a SOLIDWORKS enumerator has a bitmask like the following:

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
