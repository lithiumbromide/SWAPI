---
title: "GetCard Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetCard"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetCard.html"
---

# GetCard Method (IEdmFolder5)

Gets the interface to a data card of a file of the specified file type or the interface to the data card of this folder.

## Syntax

### Visual Basic

```vb
Function GetCard( _
   ByVal bsExtension As System.String _
) As IEdmCard5
```

### C#

```csharp
IEdmCard5 GetCard(
   System.string bsExtension
)
```

### C++/CLI

```cpp
IEdmCard5^ GetCard(
   System.String^ bsExtension
)
```

### Parameters

- `bsExtension`: Extension of file for which to get a data card; for example, "DWG" or "DOC" or "." to get the data card for this folder

### Return Value

[IEdmCard5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)

## Examples

[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)
[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

If you only need the card ID, it is faster to call [IEdmfolder5::GetCardID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetCardID.html) than to call this method.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmCard5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_NAME: There is no data card matching the specified extension.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
