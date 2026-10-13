---
title: "LineSpacing Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "LineSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~LineSpacing.html"
---

# LineSpacing Property (ITextFormat)

Gets or sets the text line spacing.

## Syntax

### Visual Basic (Declaration)

```vb
Property LineSpacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.LineSpacing = value

value = instance.LineSpacing
```

### C#

```csharp
System.double LineSpacing {get; set;}
```

### C++/CLI

```cpp
property System.double LineSpacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line spacing

## VBA Syntax

See [TextFormat::LineSpacing](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~LineSpacing.html).

## Examples

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
