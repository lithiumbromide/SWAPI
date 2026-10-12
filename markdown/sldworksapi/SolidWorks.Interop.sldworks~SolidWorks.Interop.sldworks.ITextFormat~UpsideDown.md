---
title: "UpsideDown Property (ITextFormat)"
project: "SOLIDWORKS API Help"
interface: "ITextFormat"
member: "UpsideDown"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~UpsideDown.html"
---

# UpsideDown Property (ITextFormat)

Gets or sets whether the whole text string is upside down.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpsideDown As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextFormat
Dim value As System.Boolean

instance.UpsideDown = value

value = instance.UpsideDown
```

### C#

```csharp
System.bool UpsideDown {get; set;}
```

### C++/CLI

```cpp
property System.bool UpsideDown {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the string is upside down, false if not

## VBA Syntax

See [TextFormat::UpsideDown](ms-its:sldworksapivb6.chm::/sldworks~TextFormat~UpsideDown.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html)
