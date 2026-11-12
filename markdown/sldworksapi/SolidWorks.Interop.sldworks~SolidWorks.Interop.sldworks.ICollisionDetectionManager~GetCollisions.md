---
title: "GetCollisions Method (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "GetCollisions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetCollisions.html"
---

# GetCollisions Method (ICollisionDetectionManager)

Gets the collisions detected.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCollisions( _
   ByVal TreatContactAsCollision As System.Boolean, _
   ByRef Collisions As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim TreatContactAsCollision As System.Boolean
Dim Collisions As System.Object
Dim value As System.Integer

value = instance.GetCollisions(TreatContactAsCollision, Collisions)
```

### C#

```csharp
System.int GetCollisions(
   System.bool TreatContactAsCollision,
   out System.object Collisions
)
```

### C++/CLI

```cpp
System.int GetCollisions(
   System.bool TreatContactAsCollision,
   [Out] System.Object^ Collisions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TreatContactAsCollision`: True to treat touching faces/edges/vertices as colliding, false to require solid bodies to overlap in a finite volume
- `Collisions`: Array of [ICollision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.html)s

### Return Value

Number of collisions found

## VBA Syntax

See [CollisionDetectionManager::GetCollisions](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager~GetCollisions.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## Remarks

Use [ICollisionDetectionManager::IsCollisionPresent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~IsCollisionPresent.html) to determine whether to run this method.

This method can take significantly longer to execute than ICollisionDetectionManager::IsCollisionPresent, because this method might perform the collision detection calculation repeatedly.

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
