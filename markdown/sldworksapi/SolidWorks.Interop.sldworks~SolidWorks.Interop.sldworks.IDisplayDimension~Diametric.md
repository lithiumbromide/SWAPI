---
title: "Diametric Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Diametric"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.html"
---

# Diametric Property (IDisplayDimension)

Gets or sets whether this display dimension is radial/single distance or diameter/doubled distance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Diametric As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Diametric = value

value = instance.Diametric
```

### C#

```csharp
System.bool Diametric {get; set;}
```

### C++/CLI

```cpp
property System.bool Diametric {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the diameter/doubled distance dimension, false to display the radial/single distance dimension

## VBA Syntax

See [DisplayDimension::Diametric](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Diametric.html).

## Examples

[Change Radial to Diametric Style (VBA)](Change_Radial_to_Diametric_Style_Example_VB.htm)
[Create Non-associative Diameter Dimension (VBA)](Create_Non-associative_Diameter_Dimension_Example_VB.htm)

## Remarks

Depending on the [type](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionType_e.html) of this display dimension, this property toggles between:

- radial and diameter display dimensions
- radial linear and diametric linear display dimensions

This property does not affect other types of dimensions.

Use [IModelDocExtension::AddSpecificDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.html) to create single or doubled distance display dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetType.html)
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.html)
[IDisplayDimension::DisplayAsLinear Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.html)

## Availability

SOLIDWORKS 99, datecode 1999207
