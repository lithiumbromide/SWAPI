---
title: "CreateSketchPlane Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSketchPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchPlane.html"
---

# CreateSketchPlane Method (ISketchManager)

Creates a 3D sketch plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSketchPlane( _
   ByVal Relation1 As System.Integer, _
   ByVal Relation2 As System.Integer, _
   ByVal Relation3 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Relation1 As System.Integer
Dim Relation2 As System.Integer
Dim Relation3 As System.Integer
Dim value As System.Boolean

value = instance.CreateSketchPlane(Relation1, Relation2, Relation3)
```

### C#

```csharp
System.bool CreateSketchPlane(
   System.int Relation1,
   System.int Relation2,
   System.int Relation3
)
```

### C++/CLI

```cpp
System.bool CreateSketchPlane(
   System.int Relation1,
   System.int Relation2,
   System.int Relation3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Relation1`: Relation as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the first selection to position the 3D sketch plane
- `Relation2`: Relation as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the second selection to position the 3D sketch plane
- `Relation3`: Relation as defined in [swConstraintType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the third selection to position the 3D sketch plane

### Return Value

True if the 3D sketch plane is created, false if not

## VBA Syntax

See [SketchManager::CreateSketchPlane](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~CreateSketchPlane.html).

## Examples

[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)

## Remarks

This method gets the selected items from the selection list in the order in which they were selected and applies the specified relation to them. If fewer than three items were selected, then only the first, or first and second, values are used.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
