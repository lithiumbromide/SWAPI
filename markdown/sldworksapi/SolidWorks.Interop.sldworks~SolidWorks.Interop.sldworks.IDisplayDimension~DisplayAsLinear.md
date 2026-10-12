---
title: "DisplayAsLinear Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "DisplayAsLinear"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.html"
---

# DisplayAsLinear Property (IDisplayDimension)

Gets or sets whether this diameter dimension is displayed as a linear dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayAsLinear As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.DisplayAsLinear = value

value = instance.DisplayAsLinear
```

### C#

```csharp
System.bool DisplayAsLinear {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayAsLinear {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays a linear dimension, false displays a diameter dimension

## VBA Syntax

See [DisplayDimension::DisplayAsLinear](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~DisplayAsLinear.html).

## Remarks

This property applies only to diameter dimensions. It does not affect other types of dimensions.

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.html)
[IDisplayDimension::Foreshortened Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Foreshortened.html)

## Availability

SOLIDWORKS 99, datecode 1999207
