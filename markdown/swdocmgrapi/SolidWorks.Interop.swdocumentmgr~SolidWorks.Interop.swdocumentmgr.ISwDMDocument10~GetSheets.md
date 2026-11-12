---
title: "GetSheets Method (ISwDMDocument10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument10"
member: "GetSheets"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetSheets.html"
---

# GetSheets Method (ISwDMDocument10)

Gets the sheets in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheets() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument10
Dim value As System.Object

value = instance.GetSheets()
```

### C#

```csharp
System.object GetSheets()
```

### C++/CLI

```cpp
System.Object^ GetSheets();
```

### Return Value

Array of [sheets](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet.html)

## VBA Syntax

See [SwDMDocument10::GetSheets](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument10~GetSheets.html).

## Examples

[Get Preview Bitmaps of Drawing Sheets (C#)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm)
[Get Preview Bitmaps of Drawing Sheets (VB.NET)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm)

## Remarks

This method only supports documents saved in SOLIDWORKS 2008 and later.

## See Also

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
