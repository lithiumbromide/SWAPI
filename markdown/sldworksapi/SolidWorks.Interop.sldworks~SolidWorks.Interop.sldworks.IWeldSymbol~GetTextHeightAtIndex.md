---
title: "GetTextHeightAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetTextHeightAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextHeightAtIndex.html"
---

# GetTextHeightAtIndex Method (IWeldSymbol)

Gets the text height for the specified piece of text in this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetTextHeightAtIndex(Index)
```

### C#

```csharp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired piece of text where the index begins at 0

### Return Value

Text height for the specified piece of text in meters

## VBA Syntax

See [WeldSymbol::GetTextHeightAtIndex](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetTextHeightAtIndex.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.html)
[IWeldSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAngleAtIndex.html)
[IWeldSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAtIndex.html)
[IWeldSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextCount.html)
[IWeldSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextInvertAtIndex.html)
[IWeldSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextPositionAtIndex.html)
[IWeldSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextRefPositionAtIndex.html)
[IWeldSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTextPositionAtIndex.html)
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html)
