---
title: "RotateOrCopy Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RotateOrCopy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy.html"
---

# RotateOrCopy Method (IModelDocExtension)

Rotates and optionally copies the selected sketch entities or annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RotateOrCopy( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal DestX As System.Double, _
   ByVal DestY As System.Double, _
   ByVal DestZ As System.Double, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Copy As System.Boolean
Dim NumCopies As System.Integer
Dim KeepRelations As System.Boolean
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim BaseZ As System.Double
Dim DestX As System.Double
Dim DestY As System.Double
Dim DestZ As System.Double
Dim Angle As System.Double

instance.RotateOrCopy(Copy, NumCopies, KeepRelations, BaseX, BaseY, BaseZ, DestX, DestY, DestZ, Angle)
```

### C#

```csharp
void RotateOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ,
   System.double Angle
)
```

### C++/CLI

```cpp
void RotateOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Copy`: True to copy sketch entities or annotations, false to not
- `NumCopies`: Number of copies
- `KeepRelations`: True to keep sketch relations, false to not
- `BaseX`: X coordinate of the base point from which to rotate the sketch entities or annotations
- `BaseY`: Y coordinate of the base point from which to rotate the sketch entities or annotations
- `BaseZ`: Z coordinate of the base point from which to rotate the sketch entities or annotations
- `DestX`: X vector component of the axis of rotation parallel to the base point
- `DestY`: Y vector component of the axis of rotation parallel to the base point
- `DestZ`: Z vector component of the axis of rotation parallel to the base point
- `Angle`: Angle at which to rotate or move the sketch entities or annotations

## VBA Syntax

See [ModelDocExtension::RotateOrCopy](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RotateOrCopy.html).

## Examples

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

## Remarks

Typically a user will specify 0, 0, 1 for the x, y, z destination point coordinates and 0 for the baseZ argument. The baseX and baseY arguments should specify the center of rotation for the sketch entity.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::MoveOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveOrCopy.html)
[IModelDocExtension::ScaleOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ScaleOrCopy.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
