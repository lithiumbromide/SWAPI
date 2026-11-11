---
title: "InsertBlock Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertBlock"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertBlock.html"
---

# InsertBlock Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::InsertBlock2](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertBlock2.html).

## Syntax

### Visual Basic

```vb
Function InsertBlock( _
   ByVal BlockName As System.String, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Rotation As System.Double _
) As BlockInstance
```

### C#

```csharp
BlockInstance InsertBlock(
   System.string BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### JScript

```
function InsertBlock(
   BlockName : System.String,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   Scale : System.double,
   Rotation : System.double
) : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* InsertBlock(
   System.string* BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### C++/CLI

```cpp
BlockInstance^ InsertBlock(
   System.String^ BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### Parameters

- `BlockName`: Name for the Block instance
- `InsertX`: x coordinate where to insert the Block instance
- `InsertY`: y coordinate where to insert the Block instance
- `InsertZ`: z coordinate where to insert the Block instance
- `Scale`: Scale factor for each axis
- `Rotation`: Angle by which to rotate the Block instance; in radians (see **Remarks**)

### Return Value

[Block instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Remarks

Use a positive value for Rotation to rotate the Block instance counterclockwise and a negative value to rotate the Block instance clockwise.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1
