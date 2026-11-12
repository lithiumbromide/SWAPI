---
title: "FlatShotByReplaceExistingBlock Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "FlatShotByReplaceExistingBlock"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByReplaceExistingBlock.html"
---

# FlatShotByReplaceExistingBlock Method (ISketchManager)

Replaces an existing Block in the drawing with a new Block containing the 2D flattened representation of the current view's 3D solid objects and Regions.

## Syntax

### Visual Basic

```vb
Function FlatShotByReplaceExistingBlock( _
   ByVal BlockName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool FlatShotByReplaceExistingBlock(
   System.string BlockName
)
```

### JScript

```
function FlatShotByReplaceExistingBlock(
   BlockName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool FlatShotByReplaceExistingBlock(
   System.string* BlockName
)
```

### C++/CLI

```cpp
System.bool FlatShotByReplaceExistingBlock(
   System.String^ BlockName
)
```

### Parameters

- `BlockName`: Name of existing Block to replace

### Return Value

True if successful, false if not

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
[ISketchManager::FlatShotByInsertAsBlock Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByInsertAsBlock.html)

## Availability

DraftSight 2020 SP0
