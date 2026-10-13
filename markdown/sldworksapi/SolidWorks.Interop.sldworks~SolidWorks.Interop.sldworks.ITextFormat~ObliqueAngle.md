---
title: "ObliqueAngle Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "ObliqueAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~ObliqueAngle.html"
---

# ObliqueAngle Property (ITextFormat)

Gets or sets the text slant.

## Syntax

### Visual Basic (Declaration)

```vb
Property ObliqueAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.ObliqueAngle = value

value = instance.ObliqueAngle
```

### C#

```csharp
System.double ObliqueAngle {get; set;}
```

### C++/CLI

```cpp
property System.double ObliqueAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text slant

## VBA Syntax

See [TextFormat::ObliqueAngle](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~ObliqueAngle.html).

## Examples

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
