---
title: "MoveOrCopy Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "MoveOrCopy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveOrCopy.html"
---

# MoveOrCopy Method (IModelDocExtension)

Moves and optionally copies the selected sketch entities or annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MoveOrCopy( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal DestX As System.Double, _
   ByVal DestY As System.Double, _
   ByVal DestZ As System.Double _
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

instance.MoveOrCopy(Copy, NumCopies, KeepRelations, BaseX, BaseY, BaseZ, DestX, DestY, DestZ)
```

### C#

```csharp
void MoveOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ
)
```

### C++/CLI

```cpp
void MoveOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Copy`: True to copy the sketch entities or annotations, false to not
- `NumCopies`: Number of copies
- `KeepRelations`: True to keep sketch relations, false to not
- `BaseX`: X coordinate of the base point from which to move the sketch entities or annotations
- `BaseY`: Y coordinate of the base point from which to move the sketch entities or annotations
- `BaseZ`: Z coordinate of the base point from which to move the sketch entities or annotations
- `DestX`: X coordinate of the destination point to which to move the sketch entities or annotations
- `DestY`: Y coordinate of the destination point to which to move the sketch entities or annotations
- `DestZ`: Z coordinate of the destination point to which to move the sketch entities or annotations

## VBA Syntax

See [ModelDocExtension::MoveOrCopy](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~MoveOrCopy.html).

## Examples

[Move Copy Sketch Entities (C#)](Move_Copy_Sketch_Entities_Example_CSharp.htm)
[Move Copy Sketch Entities (VB.NET)](Move_Copy_Sketch_Entities_Example_VBNET.htm)
[Move Copy Sketch Entities (VBA)](Move_Copy_Sketch_Entities_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::RotateOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy.html)
[IModelDocExtension::ScaleOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ScaleOrCopy.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
