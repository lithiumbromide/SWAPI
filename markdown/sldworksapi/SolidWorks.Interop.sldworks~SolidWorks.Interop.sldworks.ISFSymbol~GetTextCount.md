---
title: "GetTextCount Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetTextCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextCount.html"
---

# GetTextCount Method (ISFSymbol)

Gets the number of text items in the surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetTextCount()
```

### C#

```csharp
System.int GetTextCount()
```

### C++/CLI

```cpp
System.int GetTextCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text items

## VBA Syntax

See [SFSymbol::GetTextCount](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetTextCount.html).

## Remarks

Call this method before calling the following methods to get the number of text items in this surface finish symbol:

- [ISFSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetText.html)
- [ISFSymbol::GetTextAngleAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.html)
- [ISFSymbol::GetTextFontAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.html)
- [ISFSymbol::GetTextHeightAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.html)
- [ISFSymbol::GetTextInvertAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.html)
- [ISFSymbol::GetTextPositionAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.html) and [ISFSymbol::IGetTextPositionAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.html)
- [ISFSymbol::GetTextRefPositioinAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.html)

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
