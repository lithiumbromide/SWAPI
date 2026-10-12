---
title: "GetSize Method (IEdmCard5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard5"
member: "GetSize"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetSize.html"
---

# GetSize Method (IEdmCard5)

Gets the size of this data card.

## Syntax

### Visual Basic

```vb
Sub GetSize( _
   ByRef plWidth As System.Integer, _
   ByRef plHeight As System.Integer _
)
```

### C#

```csharp
void GetSize(
   out System.int plWidth,
   out System.int plHeight
)
```

### C++/CLI

```cpp
void GetSize(
   [Out] System.int plWidth,
   [Out] System.int plHeight
)
```

### Parameters

- `plWidth`: Width in pixels of this data card
- `plHeight`: Height in pixels of this data card

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCard5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)
[IEdmCard5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
