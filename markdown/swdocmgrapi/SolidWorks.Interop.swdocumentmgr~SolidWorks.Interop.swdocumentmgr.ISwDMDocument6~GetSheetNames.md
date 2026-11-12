---
title: "GetSheetNames Method (ISwDMDocument6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument6"
member: "GetSheetNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html"
---

# GetSheetNames Method (ISwDMDocument6)

Gets the names of the sheets in the drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument6
Dim value As System.Object

value = instance.GetSheetNames()
```

### C#

```csharp
System.object GetSheetNames()
```

### C++/CLI

```cpp
System.Object^ GetSheetNames();
```

### Return Value

Array of sheet name strings.

## VBA Syntax

See [SwDMDocument6::GetSheetNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument6~GetSheetNames.html).

## Examples

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

## Remarks

This method only supports drawing documents saved in SOLIDWORKS 2005 SP02 and later. An empty array is returned if the names of the sheets are not found.

## See Also

[ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.html)
[ISwDMDocument6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6_members.html)
[ISwDMDocument4::GetActiveSheetName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html)
[ISwDMDocument4::GetSheetCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.html)
[ISwDMDocument13::GetSheetFormatPath Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)

## Availability

SOLIDWORKS Document Manager API 2005 SP2
