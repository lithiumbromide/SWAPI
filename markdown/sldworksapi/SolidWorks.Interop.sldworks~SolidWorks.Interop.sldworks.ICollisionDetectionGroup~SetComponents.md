---
title: "SetComponents Method (ICollisionDetectionGroup)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionGroup"
member: "SetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~SetComponents.html"
---

# SetComponents Method (ICollisionDetectionGroup)

Sets the specified components in this collision detection group.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponents( _
   ByVal Components As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionGroup
Dim Components As System.Object
Dim value As System.Integer

value = instance.SetComponents(Components)
```

### C#

```csharp
System.int SetComponents(
   System.object Components
)
```

### C++/CLI

```cpp
System.int SetComponents(
   System.Object^ Components
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Components`: Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

### Return Value

Return code as defined in [swCollisionGroupSetComponentsErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupSetComponentsErrors_e.html)

## VBA Syntax

See [CollisionDetectionGroup::SetComponents](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionGroup~SetComponents.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## See Also

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html)
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
