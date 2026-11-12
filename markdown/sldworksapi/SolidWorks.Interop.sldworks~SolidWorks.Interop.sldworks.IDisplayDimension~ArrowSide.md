---
title: "ArrowSide Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ArrowSide"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide.html"
---

# ArrowSide Property (IDisplayDimension)

Gets or sets the position of the dimension arrows.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArrowSide As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.ArrowSide = value

value = instance.ArrowSide
```

### C#

```csharp
System.int ArrowSide {get; set;}
```

### C++/CLI

```cpp
property System.int ArrowSide {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dimension arrow side state as defined in [swDimensionArrowsSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionArrowsSide_e.html)

## VBA Syntax

See [DisplayDimension::ArrowSide](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ArrowSide.html).

## Examples

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

## Remarks

By specifying one of the following values in the Dimension Arrow Side state, the location of the dimension arrow with respect to the extension lines can be controlled. Valid values are listed in the [swDimensionArrowsSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionArrowsSide_e.html) enumeration.

The graphics of the drawing change when you change this property. After you finish changing the drawing, use [IModelDoc2::WindowRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~WindowRedraw.html) to regenerate the drawing and display your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow.html)
[IDisplayDimension::GetUseDocSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.html)
[IDisplayDimension::SetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow.html)
