---
title: "Color Property (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Color.html"
---

# Color Property (ISketchPoint)

Gets or sets the color of this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Integer

instance.Color = value

value = instance.Color
```

### C#

```csharp
System.int Color {get; set;}
```

### C++/CLI

```cpp
property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

COLORREF value for this sketch point

## VBA Syntax

See [SketchPoint::Color](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Color.html).

## Remarks

Only drawing documents support layers.

Sketch points can be created on a layer that has specific visual properties. The color value specified with this property overrides the layer color.

Use the [ISketchPoint::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~LayerOverride.html) to determine if this sketch point is currently using its default layer color.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Layer.html)

## Availability

SOLIDWORKS 99, datecode 1999207
