---
title: "GetUseDocTextFormat Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (ISketchText)

Gets whether default model text format is in use in this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.Boolean

value = instance.GetUseDocTextFormat()
```

### C#

```csharp
System.bool GetUseDocTextFormat()
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the default model text format is used, false if not

## VBA Syntax

See [SketchText::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~SketchText~GetUseDocTextFormat.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## Remarks

To change the text format of an existing sketch text, get the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object using [ISketchText::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~GetTextFormat.html) or [ISketchText::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~IGetTextFormat.html), next use the ITextFormat APIs to set the text format properties to what you want the sketch text to look like. Then, use [ISketchText::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~SetTextFormat.html) or [ISketchText::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~ISetTextFormat.html) to change how the sketch text looks. To make the sketch text use the default model text format, use ISketchText::SetTextFormat and ISketchText::ISetTextFormat with the UseDoc argument set to True.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
