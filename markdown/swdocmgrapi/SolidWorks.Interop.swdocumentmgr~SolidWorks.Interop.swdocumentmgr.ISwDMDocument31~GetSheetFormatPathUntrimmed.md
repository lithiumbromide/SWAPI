---
title: "GetSheetFormatPathUntrimmed Method (ISwDMDocument31)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument31"
member: "GetSheetFormatPathUntrimmed"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetFormatPathUntrimmed.html"
---

# GetSheetFormatPathUntrimmed Method (ISwDMDocument31)

Gets the path and filename of the sheet format used for the specified sheet without removing leading or trailing whitespace characters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetFormatPathUntrimmed( _
   ByVal SheetName As System.String, _
   ByRef FormatPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument31
Dim SheetName As System.String
Dim FormatPath As System.String
Dim value As System.Integer

value = instance.GetSheetFormatPathUntrimmed(SheetName, FormatPath)
```

### C#

```csharp
System.int GetSheetFormatPathUntrimmed(
   System.string SheetName,
   out System.string FormatPath
)
```

### C++/CLI

```cpp
System.int GetSheetFormatPathUntrimmed(
   System.String^ SheetName,
   [Out] System.String^ FormatPath
)
```

### Parameters

- `SheetName`: Untrimmed sheet name, complete with leading and trailing whitespace characters.
- `FormatPath`: Path and filename of the sheet format.

### Return Value

Result as defined in [swSheetFormatPathResult](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swSheetFormatPathResult.html).

## VBA Syntax

See [SwDMDocument31::GetSheetFormatPathUntrimmed](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument31~GetSheetFormatPathUntrimmed.html).

## Examples

**Get Drawing Sheets' Properties (Untrimmed) (C#)**
**Get Drawing Sheets' Properties (Untrimmed) (VB.NET)**

## Remarks

This method only supports drawing documents saved in SOLIDWORKS 2005 SP02 and later. An empty string is returned for documents saved in eariler versions of SOLIDWORKS.

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html) or [ISwDMDocument31::GetSheetNamesUntrimmed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetNamesUntrimmed.html).

## See Also

[ISwDMDocument31 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31.html)
[ISwDMDocument31 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31_members.html)
[GetSheetFormatPath Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)
[GetSheetProperties Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html)
[GetSheetPropertiesUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetPropertiesUntrimmed.html)
[getsheetnames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html)
[GetSheetNamesUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetNamesUntrimmed.html)

## Availability

SOLIDWORKS Document Manager API 2026 SP2.
