---
title: "GetContour Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetContour"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetContour.html"
---

# GetContour Method (IWeldSymbol)

Gets the contour settings for this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContour( _
   ByVal Top As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Top As System.Boolean
Dim value As System.Integer

value = instance.GetContour(Top)
```

### C#

```csharp
System.int GetContour(
   System.bool Top
)
```

### C++/CLI

```cpp
System.int GetContour(
   System.bool Top
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Top`: If true, then get the contour setting for the portion of the symbol above the horizontal line; if false, then get the contour setting for the portion of the symbol below the horizontal line

### Return Value

Contour setting as defined by [swWeldSymbolContourTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolContourTypes_e.html)

## VBA Syntax

See [WeldSymbol::GetContour](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetContour.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To set the contour settings for a weld symbol, use [IWeldSymbol::SetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetText.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
