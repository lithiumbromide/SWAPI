---
title: "SetText Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "SetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetText.html"
---

# SetText Method (ISFSymbol)

Sets a text string in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetText( _
   ByVal WhichOne As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim WhichOne As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.SetText(WhichOne, Text)
```

### C#

```csharp
System.bool SetText(
   System.int WhichOne,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool SetText(
   System.int WhichOne,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Text item to set as defined in [swSurfaceFinishSymbolText_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceFinishSymbolText_e.html)
- `Text`: Text string

### Return Value

True if the text string is successfully set, false if not

## VBA Syntax

See [SFSymbol::SetText](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~SetText.html).

## Remarks

If an invalid text item is specified, the symbol is not changed, and false is returned.

To see the model or drawing changes caused by running this method, you must redraw your window. See [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) for details.

To get the text strings, use [ISFSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetText.html).

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
