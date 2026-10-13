---
title: "GetTextFormat Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "GetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.html"
---

# GetTextFormat Method (ISketchText)

Gets the text format for this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormat() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.Object

value = instance.GetTextFormat()
```

### C#

```csharp
System.object GetTextFormat()
```

### C++/CLI

```cpp
System.Object^ GetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [SketchText::GetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~SketchText~GetTextFormat.html).

## Examples

[Get All Elements (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## Remarks

To change the text format of an existing sketch text, get the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object using this method, next use its APIs to set the text format properties to what you want the sketch text to look like. Then use [ISketchText::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~SetTextFormat.html) or [ISketchText::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~ISetTextFormat.html) to change how the sketch text looks. To make the sketch text use the default model text format, use ISketchText:SetTextFormat and ISketchText::ISetTextFormat with the UseDoc argument set to True.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.html)
[ISketchText::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.html)
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
