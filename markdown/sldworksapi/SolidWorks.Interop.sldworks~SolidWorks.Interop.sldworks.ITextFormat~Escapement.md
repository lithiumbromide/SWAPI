---
title: "Escapement Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "Escapement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~Escapement.html"
---

# Escapement Property (ITextFormat)

Gets or sets the text angle in radians.

## Syntax

### Visual Basic (Declaration)

```vb
Property Escapement As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Double

instance.Escapement = value

value = instance.Escapement
```

### C#

```csharp
System.double Escapement {get; set;}
```

### C++/CLI

```cpp
property System.double Escapement {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text angle in radians

## VBA Syntax

See [TextFormat::Escapement](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~Escapement.html).

## Examples

[Gets All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
