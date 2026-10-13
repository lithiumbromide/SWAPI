---
title: "GetSheetPropertiesUntrimmed Method (ISwDMDocument31)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument31"
member: "GetSheetPropertiesUntrimmed"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetPropertiesUntrimmed.html"
---

# GetSheetPropertiesUntrimmed Method (ISwDMDocument31)

Gets the specified sheet's properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetPropertiesUntrimmed( _
   ByVal SheetName As System.String, _
   ByRef Properties As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument31
Dim SheetName As System.String
Dim Properties As System.Object
Dim value As System.Integer

value = instance.GetSheetPropertiesUntrimmed(SheetName, Properties)
```

### C#

```csharp
System.int GetSheetPropertiesUntrimmed(
   System.string SheetName,
   out System.object Properties
)
```

### C++/CLI

```cpp
System.int GetSheetPropertiesUntrimmed(
   System.String^ SheetName,
   [Out] System.Object^ Properties
)
```

### Parameters

- `SheetName`: Untrimmed sheet name, complete with leading and trailing whitespace characters.
- `Properties`: Array of 8 doubles (see **Remarks**)

### Return Value

Result as defined in [swSheetPropertiesResult](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swSheetPropertiesResult.html)

## VBA Syntax

See [SwDMDocument31::GetSheetPropertiesUntrimmed](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument31~GetSheetPropertiesUntrimmed.html).

## Examples

**Get Drawing Sheets' Properties (Untrimmed) (C#)**
**Get Drawing Sheets' Properties (Untrimmed) (VB.NET)**

## Remarks

This method only supports drawing documents saved in SOLIDWORKS 2005 SP02 and later. An empty string is returned for documents saved in eariler versions of SOLIDWORKS.

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html) or [ISwDMDocument31::GetSheetNamesUntrimmed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetNamesUntrimmed.html).

The output value is an array of 8 doubles:

**[**`sheetPaperSize, sheetWidth, sheetHeight, sheetScale1, sheetScale2, firstAngle, templateSize, templateVisible`**]**

where:

1. `sheetPaperSize`: long packed into a double represented by [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)
2. `sheetWidth`: sheet width
3. `sheetHeight`: sheet height
4. `sheetScale1`: sheet scale1
5. `sheetScale2`: sheet scale2
6. `firstAngle`: Boolean packed into a double; true if sheet is using first angle project, false if not
7. `templateSize`: long packed into a double represented by [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)
8. `templateVisible`: Boolean packed into a double; true if template is visible, false if not

## See Also

[ISwDMDocument31 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31.html)
[ISwDMDocument31 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31_members.html)
[GetSheetProperties Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html)
[GetSheetNames Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html)
[GetSheetNamesUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetNamesUntrimmed.html)
[GetSheetFormatPath Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)
[GetSheetFormatPathUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetFormatPathUntrimmed.html)

## Availability

SOLIDWORKS Document Manager API 2026 SP2
