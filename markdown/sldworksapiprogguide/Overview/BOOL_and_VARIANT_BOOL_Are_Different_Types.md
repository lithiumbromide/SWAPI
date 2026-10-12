---
title: "BOOL and VARIANT_BOOL Are Different Types"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/BOOL_and_VARIANT_BOOL_Are_Different_Types.htm"
---

# BOOL and VARIANT_BOOL Are Different Types

This topic describes:

- [BOOL and VARIANT_BOOL differences](#BOOL)
- [S_OK and S_FALSE values](#S_OK)

### BOOL and VARIANT BOOL Differences

BOOL and VARIANT_BOOL use different number values for TRUE:

### BOOL

### VARIANT_BOOL

However, many of the SOLIDWORKS COM APIs methods with VARIANT_BOOL return values return False or True (0 or 1). To ensure a correct comparison, always compare the return value to 0. For example:

```vb
Dim bRetVal    As Boolean
Dim lRetVal    As Long

' Invoke method
bRetVal = swSomeObject.SomeMethod

' Inspect the numeric value
lRetVal = bRetVal
Debug.Print "Numeric value = & " lRetVal

' Inspect the logical value
If  (Not (bRetVal = False)) Then   'If bRetVal Then will give incorrect results
Debug.Print "Return value is True"
Else
Debug.Print "Return value is False"
End if

' Negate value
bRetVal = (bRetVal = False)   ' bRetVal = Not bRetVal will give incorrect results
```

### S_OK and S_FALSE Values

The numeric values for S_OK and S_FALSE are:

- S_OK = 0
- S_FALSE = 1

These values should be type long in Visual Basic.
