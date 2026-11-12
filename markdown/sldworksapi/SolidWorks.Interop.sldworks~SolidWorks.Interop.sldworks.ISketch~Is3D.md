---
title: "Is3D Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "Is3D"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~Is3D.html"
---

# Is3D Method (ISketch)

Gets whether this sketch is 2D or 3D.

## Syntax

### Visual Basic (Declaration)

```vb
Function Is3D() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.Is3D()
```

### C#

```csharp
System.bool Is3D()
```

### C++/CLI

```cpp
System.bool Is3D();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this sketch is 3D, false if it is 2D

## VBA Syntax

See [Sketch::Is3D](ms-its:sldworksapivb6.chm::/sldworks~Sketch~Is3D.html).

## Examples

[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)
[Get Whether Sketch Segment is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Transform Coordinates from Sketch to Model Space (VBA)](Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[Insert3DSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Insert3DSketch2.html)

## Availability

SOLIDWORKS 99, datecode 1999207
