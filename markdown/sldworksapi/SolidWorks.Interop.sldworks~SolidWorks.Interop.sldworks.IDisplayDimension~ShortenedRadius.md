---
title: "ShortenedRadius Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ShortenedRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShortenedRadius.html"
---

# ShortenedRadius Property (IDisplayDimension)

Gets or sets whether to display this radius display dimension with a foreshortened radius.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShortenedRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ShortenedRadius = value

value = instance.ShortenedRadius
```

### C#

```csharp
System.bool ShortenedRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool ShortenedRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays a foreshortened radius, false does not display a foreshortened radius

## VBA Syntax

See [DisplayDimension::ShortenedRadius](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ShortenedRadius.html).

## Remarks

In certain instances, you might want to show a radius dimension where the leader goes towards the center of the arc, but stops just before reaching the center. This is commonly used when the center of the arc is beyond the bounds of a drawing, or interferes with another view. This method controls that display characteristic.

This property applies only to radius dimensions. It does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
