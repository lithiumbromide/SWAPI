---
title: "ApplyTransforms Method (ICollisionDetectionGroup)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionGroup"
member: "ApplyTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~ApplyTransforms.html"
---

# ApplyTransforms Method (ICollisionDetectionGroup)

Applies the specified transforms to the components in this collision detection group.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyTransforms( _
   ByVal ComponentTransforms As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionGroup
Dim ComponentTransforms As System.Object
Dim value As System.Integer

value = instance.ApplyTransforms(ComponentTransforms)
```

### C#

```csharp
System.int ApplyTransforms(
   System.object ComponentTransforms
)
```

### C++/CLI

```cpp
System.int ApplyTransforms(
   System.Object^ ComponentTransforms
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentTransforms`: Array of [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

### Return Value

Result code as defined in [swCollisionGroupApplyTransformErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupApplyTransformErrors_e.html)

## VBA Syntax

See [CollisionDetectionGroup::ApplyTransforms](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionGroup~ApplyTransforms.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## See Also

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html)
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
