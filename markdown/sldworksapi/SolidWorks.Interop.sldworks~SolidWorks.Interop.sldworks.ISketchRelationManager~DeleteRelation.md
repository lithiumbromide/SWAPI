---
title: "DeleteRelation Method (ISketchRelationManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchRelationManager"
member: "DeleteRelation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteRelation.html"
---

# DeleteRelation Method (ISketchRelationManager)

Deletes the specified logical sketch relation in sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRelation( _
   ByVal ThisRelation As SketchRelation _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRelationManager
Dim ThisRelation As SketchRelation
Dim value As System.Boolean

value = instance.DeleteRelation(ThisRelation)
```

### C#

```csharp
System.bool DeleteRelation(
   SketchRelation ThisRelation
)
```

### C++/CLI

```cpp
System.bool DeleteRelation(
   SketchRelation^ ThisRelation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThisRelation`: [Sketch relation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

### Return Value

True if the sketch relation is deleted, false if not

## VBA Syntax

See [SketchRelationManager::DeleteRelation](ms-its:sldworksapivb6.chm::/sldworks~SketchRelationManager~DeleteRelation.html).

## See Also

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html)
[ISketchRelationManager::DeleteAllRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteAllRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
