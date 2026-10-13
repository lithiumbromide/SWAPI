---
title: "Compare Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "Compare"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~Compare.html"
---

# Compare Method (IEdmMenu5)

Compares this IEdmMenu5 menu with another menu to see if they contain the same menu items.

## Syntax

### Visual Basic

```vb
Function Compare( _
   ByVal poMenu As IEdmMenu5 _
) As System.Boolean
```

### C#

```csharp
System.bool Compare(
   IEdmMenu5 poMenu
)
```

### C++/CLI

```cpp
System.bool Compare(
   IEdmMenu5^ poMenu
)
```

### Parameters

- `poMenu`: [Menu](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)

### Return Value

True if the objects are equal, false if not

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: Success, but the objects are different (pbEqual returned false).

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
