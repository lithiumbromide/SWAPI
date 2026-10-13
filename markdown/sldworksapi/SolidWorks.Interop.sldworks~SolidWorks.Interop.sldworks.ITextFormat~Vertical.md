---
title: "Vertical Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "Vertical"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~Vertical.html"
---

# Vertical Property (ITextFormat)

Gets or sets the individual characters as vertical.

## Syntax

### Visual Basic (Declaration)

```vb
Property Vertical As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Boolean

instance.Vertical = value

value = instance.Vertical
```

### C#

```csharp
System.bool Vertical {get; set;}
```

### C++/CLI

```cpp
property System.bool Vertical {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the characters are vertical, false if not

## VBA Syntax

See [TextFormat::Vertical](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~Vertical.html).

## Examples

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
