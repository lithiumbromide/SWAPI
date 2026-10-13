---
title: "GetSheetFormatPath Method (ISwDMDocument13)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument13"
member: "GetSheetFormatPath"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html"
---

# GetSheetFormatPath Method (ISwDMDocument13)

Gets the path and filename of the sheet format used for the specified sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetFormatPath( _
   ByVal SheetName As System.String, _
   ByRef FormatPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument13
Dim SheetName As System.String
Dim FormatPath As System.String
Dim value As System.Integer

value = instance.GetSheetFormatPath(SheetName, FormatPath)
```

### C#

```csharp
System.int GetSheetFormatPath(
   System.string SheetName,
   out System.string FormatPath
)
```

### C++/CLI

```cpp
System.int GetSheetFormatPath(
   System.String^ SheetName,
   [Out] System.String^ FormatPath
)
```

### Parameters

- `SheetName`: Sheet name
- `FormatPath`: Path and filename of the sheet format

### Return Value

Result as defined in [swSheetFormatPathResult](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swSheetFormatPathResult.html)

## VBA Syntax

See [SwDMDocument13::GetSheetFormatPath](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument13~GetSheetFormatPath.html).

## Examples

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later. An empty string is returned for documents saved in earlier versions of SOLIDWORKS.

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html) or [ISwDMDocument6::GetSheetNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html).

## See Also

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.html)
[ISwDMDocument13::GetSheetProperties Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html)

## Availability

SOLIDWORKS Document Manager 2009 SP0
