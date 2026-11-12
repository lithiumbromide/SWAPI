---
title: "DeleteAllRelations Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "DeleteAllRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteAllRelations.html"
---

# DeleteAllRelations Method (ISketchRelationManager)

Deletes all of the logical sketch relations in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteAllRelations() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim value As System.Boolean

value = instance.DeleteAllRelations()
```

### C#

```csharp
System.bool DeleteAllRelations()
```

### C++/CLI

```cpp
System.bool DeleteAllRelations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all of the logical sketch relations are deleted, false if not

## VBA Syntax

See [SketchRelationManager::DeleteAllRelations](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~DeleteAllRelations.html).

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::DeleteRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteRelation.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
