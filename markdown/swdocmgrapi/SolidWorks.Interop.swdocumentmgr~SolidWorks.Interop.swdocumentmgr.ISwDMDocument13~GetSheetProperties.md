---
title: "GetSheetProperties Method (ISwDMDocument13)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument13"
member: "GetSheetProperties"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html"
---

# GetSheetProperties Method (ISwDMDocument13)

Gets the specified sheet's properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetProperties( _
   ByVal SheetName As System.String, _
   ByRef Properties As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument13
Dim SheetName As System.String
Dim Properties As System.Object
Dim value As System.Integer

value = instance.GetSheetProperties(SheetName, Properties)
```

### C#

```csharp
System.int GetSheetProperties(
   System.string SheetName,
   out System.object Properties
)
```

### C++/CLI

```cpp
System.int GetSheetProperties(
   System.String^ SheetName,
   [Out] System.Object^ Properties
)
```

### Parameters

- `SheetName`: Sheet name
- `Properties`: Array of 8 doubles (see **Remarks**)

### Return Value

Result as defined in [swSheetPropertiesResult](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swSheetPropertiesResult.html)

## VBA Syntax

See [SwDMDocument13::GetSheetProperties](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument13~GetSheetProperties.html).

## Examples

[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

## Remarks

Before calling this method, call [ISwDMDocument4::GetActiveSheetName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html) or [ISwDMDocument6::GetSheetNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html).

The return value is an array of 8 doubles:

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

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.html)
[ISwDMDocument13::GetSheetFormatPath](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
