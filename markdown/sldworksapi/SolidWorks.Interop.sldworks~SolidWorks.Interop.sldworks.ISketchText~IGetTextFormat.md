---
title: "IGetTextFormat Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "IGetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.html"
---

# IGetTextFormat Method (ISketchText)

Gets the text format for this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextFormat() As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As TextFormat

value = instance.IGetTextFormat()
```

### C#

```csharp
TextFormat IGetTextFormat()
```

### C++/CLI

```cpp
TextFormat^ IGetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [SketchText::IGetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~SketchText~IGetTextFormat.html).

## Remarks

To change the text format of an existing sketch text, get the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object using this method, next use its APIs to set the text format properties to what you want the sketch text to look like. Then use [ISketchText::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~SetTextFormat.html) or [ISketchText::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~ISetTextFormat.html) to change how the sketch text looks. To make the sketch text use the default model text format, use ISketchText:SetTextFormat and ISketchText::ISetTextFormat with the UseDoc argument set to True.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.html)
[ISketchText::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.html)
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
