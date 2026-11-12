---
title: "GetText Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetText.html"
---

# GetText Method (ISFSymbol)

Gets the specified text string in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal WhichOne As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim WhichOne As System.Integer
Dim value As System.String

value = instance.GetText(WhichOne)
```

### C#

```csharp
System.string GetText(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Text item to get as defined in [swSurfaceFinishSymbolText_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceFinishSymbolText_e.html)

### Return Value

Text string

## VBA Syntax

See [SFSymbol::GetText](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetText.html).

## Remarks

Call [ISFSymbol::GetTextCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTextCount.html) before calling this method to get the number of text items.

To set the text strings, use [ISFSymbol::SetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~SetText.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.html)
[ISFSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAtIndex.html)
[ISFSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextCount.html)
[ISFSymbol::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.html)
[ISFSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.html)
[ISFSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.html)
[ISFSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.html)
[ISFSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.html)
[ISFSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
