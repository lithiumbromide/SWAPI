---
title: "Style Property (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.html"
---

# Style Property (IBreakLine)

Gets or sets the style of the break line in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Break line style as defined in [swBreakLineStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html)

## VBA Syntax

See [BreakLine::Style](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~Style.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## Remarks

This property might automatically load the model in the view.

To get or set the shape intensity of a jagged cut break line, call [IBreakLine::ShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~ShapeIntensity.html).

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
