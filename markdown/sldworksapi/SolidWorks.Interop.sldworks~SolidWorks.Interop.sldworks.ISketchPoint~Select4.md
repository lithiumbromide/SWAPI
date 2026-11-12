---
title: "Select4 Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Select4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4.html"
---

# Select4 Method (ISketchPoint)

Selects the sketch point and marks it.

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
Dim instance As ISketchPoint
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

- `Append`: True to append this selection to the selection list, false to replace the selection
  list with this selection
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the sketch point is selected, false if not

## VBA Syntax

See [SketchPoint::Select4](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Select4.html).

## Examples

[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)
[Get Sketch Points in Wizard Hole (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)
[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Get Sketch Point's Selection Mark (C#)](Get_Sketch_Points_Selection_Mark_Example_CSharp.htm)
[Get Sketch Point's Selection Mark (VB.NET)](Get_Sketch_Points_Selection_Mark_Example_VBNET.htm)
[Get Sketch Point's Selection Mark (VBA)](Get_Sketch_Points_Selection_Mark_Example_VB.htm)
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~DeSelect.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
