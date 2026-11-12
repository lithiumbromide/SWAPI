---
title: "IGetTextPositionAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "IGetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTextPositionAtIndex.html"
---

# IGetTextPositionAtIndex Method (IWeldSymbol)

Gets the text item's offset relative to note's text point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetTextPositionAtIndex(Index)
```

### C#

```csharp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the piece of text where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles:

[ textPtX, textPtY, textPtZ ]

where these text position values are offset values from the origin of this weld symbol.

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
[IWeldSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextRefPositionAtIndex.html)
