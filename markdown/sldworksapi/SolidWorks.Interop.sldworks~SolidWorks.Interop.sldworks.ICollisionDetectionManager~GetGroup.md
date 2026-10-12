---
title: "GetGroup Method (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "GetGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetGroup.html"
---

# GetGroup Method (ICollisionDetectionManager)

Gets the specified collision detection group.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroup( _
   ByVal GroupIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim GroupIndex As System.Integer
Dim value As System.Object

value = instance.GetGroup(GroupIndex)
```

### C#

```csharp
System.object GetGroup(
   System.int GroupIndex
)
```

### C++/CLI

```cpp
System.Object^ GetGroup(
   System.int GroupIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupIndex`: Zero-based index of collision detection group

### Return Value

[ICollisionDetectionGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html)

## VBA Syntax

See [CollisionDetectionManager::GetGroup](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager~GetGroup.html).

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
