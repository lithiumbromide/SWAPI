---
title: "SetText Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "SetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.html"
---

# SetText Method (IWeldSymbol)

Sets the text and symbols in the upper or lower portion of the weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetText( _
   ByVal Top As System.Boolean, _
   ByVal Left As System.String, _
   ByVal Symbol As System.String, _
   ByVal Right As System.String, _
   ByVal Stagger As System.String, _
   ByVal Contour As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Top As System.Boolean
Dim Left As System.String
Dim Symbol As System.String
Dim Right As System.String
Dim Stagger As System.String
Dim Contour As System.Integer
Dim value As System.Boolean

value = instance.SetText(Top, Left, Symbol, Right, Stagger, Contour)
```

### C#

```csharp
System.bool SetText(
   System.bool Top,
   System.string Left,
   System.string Symbol,
   System.string Right,
   System.string Stagger,
   System.int Contour
)
```

### C++/CLI

```cpp
System.bool SetText(
   System.bool Top,
   System.String^ Left,
   System.String^ Symbol,
   System.String^ Right,
   System.String^ Stagger,
   System.int Contour
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Top`: True to set the text in the portion of the symbol above the horizontal line, false to set the text in the portion of the symbol below the horizontal line
- `Left`: Text to the left of the weld symbol
- `Symbol`: Text representing the weld symbol (see **Remarks**)
- `Right`: Text to the right of the weld symbol
- `Stagger`: Text to the right of the stagger symbol (see **Remarks**)
- `Contour`: Contour setting as defined in [swWeldSymbolContourTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolContourTypes_e.html) (see **Remarks**)

### Return Value

True if the text and symbols are set, false if not

## VBA Syntax

See [WeldSymbol::SetText](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~SetText.html).

## Examples

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html) examples.

## Remarks

To get the individual pieces of text for a weld symbol, use [IWeldSymbol::GetText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetText.html). To get the contour setting for a weld symbol, use [IWeldSymbol::GetContour](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetContour.html).

The stagger text that is specified is only visible if this option is enabled. See [IWeldSymbol::GetStagger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetStagger.html) to see the current setting and [IWeldSymbol::SetStagger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~SetStagger.html) to enable or disable that option.

A list of weld symbol names can be found in the text file [**gtol.sym**,](sldworksAPIProgGuide.chm::/Miscellaneous/Geometric_Tolerance_Symbol_Libraries.htm), typically installed at **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english**. Specify Symbol with one of the currently supported ISO weld symbols:

- BUTT
- BUSQ
- BUSV
- BUSB
- BUSVBR
- BUSBR
- BUSU
- BUSJ
- BACK
- FILL
- PLUG
- SPOT
- SEAM
- SEAMC
- JSPT
- JSM

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
