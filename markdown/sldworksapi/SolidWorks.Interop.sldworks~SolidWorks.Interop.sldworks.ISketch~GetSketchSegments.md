---
title: "GetSketchSegments Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.html"
---

# GetSketchSegments Method (ISketch)

Gets the sketch segments in this sketch, which include line, arc, spline, parabola, and ellipse entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchSegments()
```

### C#

```csharp
System.object GetSketchSegments()
```

### C++/CLI

```cpp
System.Object^ GetSketchSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html), which include line, arc, spline, parabola, and ellipse entities, in this sketch (see **Remarks**)

## VBA Syntax

See [Sketch::GetSketchSegments](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchSegments.html).

## Examples

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)
[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

## Remarks

If the sketch has errors, this method does not return all of the sketch segments.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.html)
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.html)
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.html)

## Availability

SOLIDWORKS 99, datecode 1999207
