---
title: "X Property (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "X"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~X.html"
---

# X Property (ISketchPoint)

Gets or sets the x coordinate of the sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Property X As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Double

instance.X = value

value = instance.X
```

### C#

```csharp
System.double X {get; set;}
```

### C++/CLI

```cpp
property System.double X {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate of the sketch point location

## VBA Syntax

See [SketchPoint::X](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~X.html).

## Examples

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Sketch Points (VBA)](Get_Sketch_Points_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spine's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Y.html)
[ISketchPoint::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Z.html)
[ISketchPoint::SetCoords Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~SetCoords.html)
[ISketchPoint::GetCoords Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetCoords.html)

## Availability

SOLIDWORKS 99, datecode 1999207
