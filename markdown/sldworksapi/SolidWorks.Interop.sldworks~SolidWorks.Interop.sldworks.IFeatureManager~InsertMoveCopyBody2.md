---
title: "InsertMoveCopyBody2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoveCopyBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html"
---

# InsertMoveCopyBody2 Method (IFeatureManager)

Moves or makes copies of the selected solid bodies or surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoveCopyBody2( _
   ByVal TransX As System.Double, _
   ByVal TransY As System.Double, _
   ByVal TransZ As System.Double, _
   ByVal TransDist As System.Double, _
   ByVal RotPointX As System.Double, _
   ByVal RotPointY As System.Double, _
   ByVal RotPointZ As System.Double, _
   ByVal RotAngleX As System.Double, _
   ByVal RotAngleY As System.Double, _
   ByVal RotAngleZ As System.Double, _
   ByVal BCopy As System.Boolean, _
   ByVal NumCopies As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim TransX As System.Double
Dim TransY As System.Double
Dim TransZ As System.Double
Dim TransDist As System.Double
Dim RotPointX As System.Double
Dim RotPointY As System.Double
Dim RotPointZ As System.Double
Dim RotAngleX As System.Double
Dim RotAngleY As System.Double
Dim RotAngleZ As System.Double
Dim BCopy As System.Boolean
Dim NumCopies As System.Integer
Dim value As Feature

value = instance.InsertMoveCopyBody2(TransX, TransY, TransZ, TransDist, RotPointX, RotPointY, RotPointZ, RotAngleX, RotAngleY, RotAngleZ, BCopy, NumCopies)
```

### C#

```csharp
Feature InsertMoveCopyBody2(
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
)
```

### C++/CLI

```cpp
Feature^ InsertMoveCopyBody2(
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransX`: Value for delta X; applies to translation and valid only if Rot* parameters are null or Nothing (see **Remarks**)
- `TransY`: Value for delta Y; applies to translation and valid only if Rot* parameters are null or Nothing (see **Remarks**)
- `TransZ`: Value for delta Z; applies to translation and valid only if Rot* parameters are null or Nothing (see **Remarks**)
- `TransDist`: Distance ; applies to translation and valid only if Rot* parameters are null or Nothing (see **Remarks**)
- `RotPointX`: Value for X rotation origin; applies to rotation (see **Remarks**)
- `RotPointY`: Value for Y rotation origin; applies to rotation (see **Remarks**)
- `RotPointZ`: Value for Z rotation origin; applies to rotation (see **Remarks**)
- `RotAngleX`: Value for X rotation angle; applies to rotation (see **Remarks**)
- `RotAngleY`: Value for Y rotation angle; applies to rotation (see **Remarks**)
- `RotAngleZ`: Value for Z rotation angle; applies to rotation (see **Remarks**)
- `BCopy`: True if a copy operation, false if a move operation
- `NumCopies`: Number of copies to create

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMoveCopyBody2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoveCopyBody2.html).

## Examples

[Move Bodies (C#)](Move_Bodies_Example_CSharp.htm)
[Move Bodies (VB.NET)](Move_Bodies_Example_VBNET.htm)
[Move Bodies (VBA)](Move_Bodies_Example_VB.htm)

## Remarks

Specify either translation or rotation parameters. Translation and rotation cannot both be applied by a single move/copy body feature. If you specify both translation and rotation parameters, only the rotation parameters are applied.

This method requires selecting the body, surface, edge, and vertex using these marks:

| Selection | Mark |
| --- | --- |
| Body or surface | 1 |
| Rotation edge, vertex, coordinate system | 2 |
| Translation edge, vertex, coordinate system | 4 |
| Translation vertex | 8 |

**NOTE:** To add the move/copy body as a sub-feature of a derived part, you must select the move/copy body feature first.

See [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) for details on selecting and marking bodies, surfaces, edges, vertices, and coordinate systems.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
