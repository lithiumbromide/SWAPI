---
title: "GetTransforms Method (ICollisionDetectionGroup)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionGroup"
member: "GetTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~GetTransforms.html"
---

# GetTransforms Method (ICollisionDetectionGroup)

Gets the current transforms of the components in this collision detection group.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransforms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionGroup
Dim value As System.Object

value = instance.GetTransforms()
```

### C#

```csharp
System.object GetTransforms()
```

### C++/CLI

```cpp
System.Object^ GetTransforms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [CollisionDetectionGroup::GetTransforms](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionGroup~GetTransforms.html).

## See Also

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html)
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
