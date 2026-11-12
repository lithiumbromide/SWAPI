---
title: "GetSketchPoints2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.html"
---

# GetSketchPoints2 Method (ISketch)

Gets the sketch points in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPoints2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchPoints2()
```

### C#

```csharp
System.object GetSketchPoints2()
```

### C++/CLI

```cpp
System.Object^ GetSketchPoints2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) in this sketch

## VBA Syntax

See [Sketch::GetSketchPoints2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchPoints2.html).

## Examples

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)
[Get Sketch Points and Their Persistent IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)
[Get Sketch Points (VBA)](Get_Sketch_Points_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

## Remarks

The difference between this method and the now obsolete method [ISketch::GetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchPoints.html) is that this method does not return sketch points intended for internal SOLIDWORKS use only.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.html)
[ISketch::IEnumSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.html)
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.html)
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.html)
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html)
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
