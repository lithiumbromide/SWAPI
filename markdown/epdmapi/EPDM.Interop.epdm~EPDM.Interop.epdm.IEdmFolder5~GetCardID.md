---
title: "GetCardID Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetCardID"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetCardID.html"
---

# GetCardID Method (IEdmFolder5)

Gets the ID of the data card of a file with the specified extension or the ID of the data card of this folder.

## Syntax

### Visual Basic

```vb
Function GetCardID( _
   ByVal bsExtension As System.String _
) As System.Integer
```

### C#

```csharp
System.int GetCardID(
   System.string bsExtension
)
```

### C++/CLI

```cpp
System.int GetCardID(
   System.String^ bsExtension
)
```

### Parameters

- `bsExtension`: Extension of file for which to get a data card ID; for example, "DWG" or "DOC" or "." to get the ID of the data card for this folder

### Return Value

ID of the data card; 0 if not found

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)

[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

If you need to access the entire card, call[IEdmFolder5::GetCard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetCard.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The card is not found.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
