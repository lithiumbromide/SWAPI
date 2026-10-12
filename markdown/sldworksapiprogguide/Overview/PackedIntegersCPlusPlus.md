---
title: "Unpacking Double Arrays into Integer Pairs in C++"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/PackedIntegersCPlusPlus.htm"
---

# Unpacking Double Arrays into Integer Pairs in C++

Some API functions return integer information packed into arrays of double values.

To extract the pair of integers from a double in C++, SOLIDWORKS suggests using a union:

```vb
union PackedData_
{
```

```vb
double doubleValue;
int intValues[2];
```

```vb
} PackedData;

int iValue1, iValue2;
```

To access the data, assign doubleValue to the array element containing the data, then use intValues to access the integers:

```vb
PackedData.doubleValue = dArray[0];

iValue1 = PackedData.intValues[0];
iValue2 = PackedData.intValues[1];
```
