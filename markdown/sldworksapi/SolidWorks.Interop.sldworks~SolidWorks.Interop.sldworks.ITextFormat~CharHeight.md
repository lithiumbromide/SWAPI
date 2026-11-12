---
title: "CharHeight Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "CharHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeight.html"
---

# CharHeight Property (ITextFormat)

Gets or sets the height of the font in meters.

## Syntax

### Visual Basic (Declaration)

```vb
Property CharHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.CharHeight = value

value = instance.CharHeight
```

### C#

```csharp
System.double CharHeight {get; set;}
```

### C++/CLI

```cpp
property System.double CharHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Font height in meters

## VBA Syntax

See [TextFormat::CharHeight](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~CharHeight.html).

## Examples

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
[ITextFormat::CharHeightInPts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeightInPts.html)
[ITextFormat::IsHeightSpecifiedInPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~IsHeightSpecifiedInPts.html)
