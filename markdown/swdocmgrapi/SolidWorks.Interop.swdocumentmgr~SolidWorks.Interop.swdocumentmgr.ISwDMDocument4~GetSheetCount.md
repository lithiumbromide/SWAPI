---
title: "GetSheetCount Method (ISwDMDocument4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument4"
member: "GetSheetCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.html"
---

# GetSheetCount Method (ISwDMDocument4)

Gets the number of sheets in the SOLIDWORKS drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument4
Dim value As System.Integer

value = instance.GetSheetCount()
```

### C#

```csharp
System.int GetSheetCount()
```

### C++/CLI

```cpp
System.int GetSheetCount();
```

### Return Value

Number of sheets

## VBA Syntax

See [SwDMDocument4::GetSheetCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument4~GetSheetCount.html).

## Examples

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

## Remarks

This method supports SOLIDWORKS drawing documents only. A -1 or NULL is returned for all other types of SOLIDWORKS documents.

## See Also

[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.html)
[ISwDMDocument4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4_members.html)
[ISwDocument6::GetSheetNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html)
[ISwDMDocument4::GetActiveSheetName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
