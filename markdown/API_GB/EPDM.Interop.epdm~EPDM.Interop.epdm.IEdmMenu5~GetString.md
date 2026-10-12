---
title: "GetString Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "GetString"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetString.html"
---

# GetString Method (IEdmMenu5)

Gets a string for a menu item in this menu.

## Syntax

### Visual Basic

```vb
Function GetString( _
   ByVal lItemID As System.Integer, _
   ByVal eType As EdmMenuStrType _
) As System.String
```

### C#

```csharp
System.string GetString(
   System.int lItemID,
   EdmMenuStrType eType
)
```

### C++/CLI

```cpp
System.String^ GetString(
   System.int lItemID,
   EdmMenuStrType eType
)
```

### Parameters

- `lItemID`: ID of menu item for which to get a string
- `eType`: Type of string to get as defined in [EdmMenuStrType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuStrType.html)

### Return Value

String (see **Remarks**)

## Remarks

C++ programmers must free the returned string with SysFreeString.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)
[IEdmMenu6::GetItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6~GetItems.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
