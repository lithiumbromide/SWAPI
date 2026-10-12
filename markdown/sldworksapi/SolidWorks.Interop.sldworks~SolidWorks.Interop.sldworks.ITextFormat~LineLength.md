---
title: "LineLength Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "LineLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~LineLength.html"
---

# LineLength Property (ITextFormat)

Gets or sets the text line length in meters.

## Syntax

### Visual Basic (Declaration)

```vb
Property LineLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.LineLength = value

value = instance.LineLength
```

### C#

```csharp
System.double LineLength {get; set;}
```

### C++/CLI

```cpp
property System.double LineLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line length

## VBA Syntax

See [TextFormat::LineLength](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~LineLength.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
