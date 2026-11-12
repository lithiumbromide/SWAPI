---
title: "FlatShotByExportToFile Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "FlatShotByExportToFile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByExportToFile.html"
---

# FlatShotByExportToFile Method (ISketchManager)

Saves a 2D flattened representation of the current view's 3D solid objects and Regions to an external drawing file.

## Syntax

### Visual Basic

```vb
Function FlatShotByExportToFile( _
   ByVal FilePath As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool FlatShotByExportToFile(
   System.string FilePath
)
```

### JScript

```
function FlatShotByExportToFile(
   FilePath : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool FlatShotByExportToFile(
   System.string* FilePath
)
```

### C++/CLI

```cpp
System.bool FlatShotByExportToFile(
   System.String^ FilePath
)
```

### Parameters

- `FilePath`: Full path name to which to export the 2D flattened representation

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
[ISketchManager::FlatShotByInsertAsBlock Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByInsertAsBlock.html)
[ISketchManager::FlatShotByReplaceExistingBlock Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FlatShotByReplaceExistingBlock.html)

## Availability

DraftSight 2020 SP0
