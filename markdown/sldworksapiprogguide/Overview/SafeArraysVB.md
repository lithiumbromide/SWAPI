---
title: "Passing SafeArrays in VB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SafeArraysVB.htm"
---

# Passing SafeArrays in VB

## Passing SafeArrays in Visual Basic for Applications

Passing array data to SOLIDWORKS in Visual Basic for Applications (VBA) requires the use of a VARIANT variable to hold the data. Put the data into an array and assign a VARIANT to the array. Pass the VARIANT enclosed in parentheses to the API function.

```vb
Dim varArray As Variant
Dim DataArray(9) As double

' Assign values
DataArray(0) = 0.1
...

' Pass the data in a VARIANT to a SOLIDWORKS method
varArray = DataArray
Result = Object.Method( (varArray) )  ' The extra parentheses are required
```
