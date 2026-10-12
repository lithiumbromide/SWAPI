---
title: "GetComponents Method (ICollisionDetectionGroup)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionGroup"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~GetComponents.html"
---

# GetComponents Method (ICollisionDetectionGroup)

Gets the components in this collision detection group.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionGroup
Dim value As System.Object

value = instance.GetComponents()
```

### C#

```csharp
System.object GetComponents()
```

### C++/CLI

```cpp
System.Object^ GetComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [CollisionDetectionGroup::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionGroup~GetComponents.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## See Also

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html)
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
