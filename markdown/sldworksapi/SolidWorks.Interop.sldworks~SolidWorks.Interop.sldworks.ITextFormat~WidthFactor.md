---
title: "WidthFactor Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "WidthFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~WidthFactor.html"
---

# WidthFactor Property (ITextFormat)

Stretches the text by the specified factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property WidthFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.WidthFactor = value

value = instance.WidthFactor
```

### C#

```csharp
System.double WidthFactor {get; set;}
```

### C++/CLI

```cpp
property System.double WidthFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Stretch factor

## VBA Syntax

See [TextFormat::WidthFactor](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~WidthFactor.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Increase Width of Text (VBA)](Increase_Width_of_Text_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
