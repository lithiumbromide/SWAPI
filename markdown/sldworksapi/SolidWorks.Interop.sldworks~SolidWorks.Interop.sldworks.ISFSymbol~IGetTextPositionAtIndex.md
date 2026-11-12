---
title: "IGetTextPositionAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "IGetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.html"
---

# IGetTextPositionAtIndex Method (ISFSymbol)

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
Dim instance As ISFSymbol
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

- `Index`: Index of the text where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISFSymbol::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextCount.html) before calling this method to get the number of text items.

The return value is the following array of doubles :

[ textPtX, textPtY, textPtZ ]

where these text position values are offset values from the origin of this [ISFSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html) object.

Call [ISFSymbol::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextCount.html) before calling this method to get the number of text items.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.html)
[ISFSymbol::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetText.html)
[ISFSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.html)
[ISFSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAtIndex.html)
[ISFSymbol::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.html)
[ISFSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.html)
[ISFSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.html)
[ISFSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.html)
[ISFSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetText.html)
