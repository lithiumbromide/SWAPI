---
title: "RemoveGroup Method (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "RemoveGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~RemoveGroup.html"
---

# RemoveGroup Method (ICollisionDetectionManager)

Removes the specified collision detection group from collision detection.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveGroup( _
   ByVal GroupIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim GroupIndex As System.Integer
Dim value As System.Boolean

value = instance.RemoveGroup(GroupIndex)
```

### C#

```csharp
System.bool RemoveGroup(
   System.int GroupIndex
)
```

### C++/CLI

```cpp
System.bool RemoveGroup(
   System.int GroupIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupIndex`: Zero-based index of the collision detection group to remove from collision detection

### Return Value

True if collision detection group successfully removed, false if not

## VBA Syntax

See [CollisionDetectionManager::RemoveGroup](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager~RemoveGroup.html).

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
