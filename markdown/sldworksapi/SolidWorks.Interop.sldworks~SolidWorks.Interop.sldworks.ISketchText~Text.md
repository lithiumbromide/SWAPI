---
title: "Text Property (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.html"
---

# Text Property (ISketchText)

Gets or sets the text that makes up this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim value As System.String

instance.Text = value

value = instance.Text
```

### C#

```csharp
System.string Text {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text that makes up this sketch text

## VBA Syntax

See [SketchText::Text](ms-its:sldworksapivb6.chm::/sldworks~SketchText~Text.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)

## Remarks

To set the text format, you must be editing the sketch. See [IModelDoc2::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditSketch.html) or [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html). You can only change text in visible documents.

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)
[ISketchText::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.html)
[ISketchText::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.html)
[ISketchText::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.html)
[ISketchText::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.html)
[ISketchText::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
