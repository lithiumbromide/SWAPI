---
title: "DimensionToInside Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "DimensionToInside"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DimensionToInside.html"
---

# DimensionToInside Property (IDisplayDimension)

Gets or sets whether dimensions to arcs are always to the inside of the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionToInside As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.DimensionToInside = value

value = instance.DimensionToInside
```

### C#

```csharp
System.bool DimensionToInside {get; set;}
```

### C++/CLI

```cpp
property System.bool DimensionToInside {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True dimension to the inside of arc, false does not dimension to the inside of the arc

## VBA Syntax

See [DisplayDimension::DimensionToInside](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~DimensionToInside.html).

## Remarks

This property applies only to radius dimensions. This property does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
