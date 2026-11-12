---
title: "Select4 Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Select4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.html"
---

# Select4 Method (ISketchSegment)

Selects this sketch segment and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select4(Append, Data)
```

### C#

```csharp
System.bool Select4(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select4(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True to append this selection to the selection list, false to replace the selection list with this selection
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the sketch segment is selected, false if not

## VBA Syntax

See [SketchSegment::Select4](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Select4.html).

## Examples

[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)
[Get Axis of Revolve Feature (VBA)](Get_Axis_of_Revolve_Feature_Example_VB.htm)
[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Create Sketch Path (C#)](Create_Sketch_Path_Example_CSharp.htm)
[Create Sketch Path (VB.NET)](Create_Sketch_Path_Example_VBNET.htm)
[Create Sketch Path (VBA)](Create_Sketch_Path_Example_VB.htm)
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
