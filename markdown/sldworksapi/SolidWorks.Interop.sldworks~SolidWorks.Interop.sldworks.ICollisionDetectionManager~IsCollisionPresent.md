---
title: "IsCollisionPresent Method (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "IsCollisionPresent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~IsCollisionPresent.html"
---

# IsCollisionPresent Method (ICollisionDetectionManager)

Performs collision detection analysis between all groups of components.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCollisionPresent( _
   ByVal TreatContactAsCollision As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim TreatContactAsCollision As System.Boolean
Dim value As System.Integer

value = instance.IsCollisionPresent(TreatContactAsCollision)
```

### C#

```csharp
System.int IsCollisionPresent(
   System.bool TreatContactAsCollision
)
```

### C++/CLI

```cpp
System.int IsCollisionPresent(
   System.bool TreatContactAsCollision
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TreatContactAsCollision`: True to treat touching faces/edges/vertices as colliding, false to require solid bodies to overlap in a finite volume

### Return Value

Return code as defined in [swCollisionDetectionResults_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionDetectionResults_e.html)

## VBA Syntax

See [CollisionDetectionManager::IsCollisionPresent](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager~IsCollisionPresent.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## Remarks

This method takes less time to run than [ICollisionDetectionManager::GetCollisions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetCollisions.html).

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
