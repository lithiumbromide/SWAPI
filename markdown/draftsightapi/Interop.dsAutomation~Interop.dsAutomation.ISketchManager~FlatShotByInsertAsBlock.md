---
title: "FlatShotByInsertAsBlock Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "FlatShotByInsertAsBlock"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByInsertAsBlock.html"
---

# FlatShotByInsertAsBlock Method (ISketchManager)

Inserts a 2D flattened representation of the current view's 3D solid objects and Regions to the specified Block in the graphics area.

## Syntax

### Visual Basic

```vb
Function FlatShotByInsertAsBlock( _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal ScaleX As System.Double, _
   ByVal ScaleY As System.Double, _
   ByVal ScaleZ As System.Double, _
   ByVal Rotation As System.Double _
) As BlockInstance
```

### C#

```csharp
BlockInstance FlatShotByInsertAsBlock(
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### JScript

```
function FlatShotByInsertAsBlock(
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   ScaleX : System.double,
   ScaleY : System.double,
   ScaleZ : System.double,
   Rotation : System.double
) : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* FlatShotByInsertAsBlock(
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### C++/CLI

```cpp
BlockInstance^ FlatShotByInsertAsBlock(
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### Parameters

- `InsertX`: X-coordinate of Block's insertion point
- `InsertY`: Y-coordinate of Block's insertion point
- `InsertZ`: Z-coordinate of Block's insertion point
- `ScaleX`: Scale in x-direction
- `ScaleY`: Scale in y-direction
- `ScaleZ`: Scale in z-direction
- `Rotation`: Angle of rotation in radians

### Return Value

[IBlockInstance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Examples

[Creating Flat Representations of 3D Entities (C#)](Creating_Flat_Representations_of_3D_Entities_Example_CSharp.htm)
[Creating Flat Representations of 3D Entities (VB.NET)](Creating_Flat_Representations_of_3D_Entities_Example_VBNET.htm)
[Creating Flat Representations of 3D Entities (VBA)](Creating_Flat_Representations_of_3D_Entities_Example_VBA.htm)
[Creating Flat Representations of 3D Entities (JS)](Creating_Flat_Representations_of_3D_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Modifying Solids > Creating Flat Representations of 3D Solid Objects** in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::FlatShotByExportToFile Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByExportToFile.html)
[ISketchManager::FlatShotByReplaceExistingBlock Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByReplaceExistingBlock.html)

## Availability

DraftSight 2020 SP0
