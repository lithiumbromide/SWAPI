---
title: "BackWards Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "BackWards"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~BackWards.html"
---

# BackWards Property (ITextFormat)

Gets or sets whether the text is displayed backwards.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackWards As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Boolean

instance.BackWards = value

value = instance.BackWards
```

### C#

```csharp
System.bool BackWards {get; set;}
```

### C++/CLI

```cpp
property System.bool BackWards {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the text is displayed backwards, false if not

## VBA Syntax

See [TextFormat::BackWards](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~BackWards.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
