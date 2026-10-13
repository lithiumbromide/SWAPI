---
title: "CharHeightInPts Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "CharHeightInPts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeightInPts.html"
---

# CharHeightInPts Property (ITextFormat)

Gets or sets the height of the font in points.

## Syntax

### Visual Basic (Declaration)

```vb
Property CharHeightInPts As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Integer

instance.CharHeightInPts = value

value = instance.CharHeightInPts
```

### C#

```csharp
System.int CharHeightInPts {get; set;}
```

### C++/CLI

```cpp
property System.int CharHeightInPts {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Font height in points

## VBA Syntax

See [TextFormat::CharHeightInPts](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~CharHeightInPts.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
[ITextFormat::CharHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeight.html)
[ITextFormat::IsHeightSpecifiedInPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~IsHeightSpecifiedInPts.html)
