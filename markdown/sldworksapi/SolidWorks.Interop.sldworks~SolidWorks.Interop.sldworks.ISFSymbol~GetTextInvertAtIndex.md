---
title: "GetTextInvertAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetTextInvertAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.html"
---

# GetTextInvertAtIndex Method (ISFSymbol)

Gets the specified text item's invert flag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextInvertAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextInvertAtIndex(Index)
```

### C#

```csharp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text where the index begins at 0

### Return Value

Text item's invert flag

## VBA Syntax

See [SFSymbol::GetTextInvertAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetTextInvertAtIndex.html).

## Remarks

The invert flag specifies whether the text has been mirrored (reflected) about the X axis. Any reflection is applied after text rotation.

Call [ISFSymbol::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextCount.html) before calling this method to get the number of text items.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetText.html)
[ISFSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.html)
[ISFSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAtIndex.html)
[ISFSymbol::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.html)
[ISFSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.html)
[ISFSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.html)
[ISFSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.html)
[ISFSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.html)
[ISFSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetText.html)
