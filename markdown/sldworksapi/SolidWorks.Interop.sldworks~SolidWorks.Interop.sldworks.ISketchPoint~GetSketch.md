---
title: "GetSketch Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetSketch.html"
---

# GetSketch Method (ISketchPoint)

Gets the sketch for the current sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As Sketch

value = instance.GetSketch()
```

### C#

```csharp
Sketch GetSketch()
```

### C++/CLI

```cpp
Sketch^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchPoint::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetSketch.html).

## Examples

[Get Sketch Point's View (VBA)](Get_Sketch_Point_s_View_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)

## Remarks

You can use the [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) interface for extracting information about geometry in the sketch.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
