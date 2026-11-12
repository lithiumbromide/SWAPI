---
title: "GetTextRefPositionAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetTextRefPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextRefPositionAtIndex.html"
---

# GetTextRefPositionAtIndex Method (IWeldSymbol)

Gets the specified text's reference position in this weld symbol (that is, upper left, lower left, center).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextRefPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextRefPositionAtIndex(Index)
```

### C#

```csharp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the piece of text where the index begins at 0

### Return Value

Reference position of the specified text item as defined in [swTextPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextPosition_e.html)

## VBA Syntax

See [WeldSymbol::GetTextRefPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetTextRefPositionAtIndex.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.html)
[IWeldSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAngleAtIndex.html)
[IWeldSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAtIndex.html)
[IWeldSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextCount.html)
[IWeldSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextHeightAtIndex.html)
[IWeldSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextInvertAtIndex.html)
[IWeldSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextPositionAtIndex.html)
[IWeldSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTextPositionAtIndex.html)
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html)
