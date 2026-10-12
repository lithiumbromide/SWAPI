---
title: "GetText Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.html"
---

# GetText Method (IWeldSymbol)

Gets individual pieces of text from the weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal WhichText As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim WhichText As System.Integer
Dim value As System.String

value = instance.GetText(WhichText)
```

### C#

```csharp
System.string GetText(
   System.int WhichText
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int WhichText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Text to retrieve as defined in [swWeldSymbolTextTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolTextTypes_e.html)

### Return Value

Text

## VBA Syntax

See [WeldSymbol::GetText](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetText.html).

## Remarks

To set the individual pieces of text for a weld symbol, use [IWeldSymbol::SetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetText.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAngleAtIndex.html)
[IWeldSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAtIndex.html)
[IWeldSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextCount.html)
[IWeldSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextHeightAtIndex.html)
[IWeldSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextInvertAtIndex.html)
[IWeldSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextPositionAtIndex.html)
[IWeldSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextRefPositionAtIndex.html)
[IWeldSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTextPositionAtIndex.html)

## Availability

SOLIDWORKS 99, datecode 1999207
