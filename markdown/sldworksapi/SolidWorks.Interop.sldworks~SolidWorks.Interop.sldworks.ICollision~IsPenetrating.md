---
title: "IsPenetrating Method (ICollision)"
project: "SOLIDWORKS API Help"
interface: "ICollision"
member: "IsPenetrating"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~IsPenetrating.html"
---

# IsPenetrating Method (ICollision)

Gets whether the components involved in this collision penetrate one another.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsPenetrating() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICollision
Dim value As System.Boolean

value = instance.IsPenetrating()
```

### C#

```csharp
System.bool IsPenetrating()
```

### C++/CLI

```cpp
System.bool IsPenetrating();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if components penetrate one another, false if they are only in contact

## VBA Syntax

See [Collision::IsPenetrating](ms-its:sldworksapivb6.chm::/sldworks~Collision~IsPenetrating.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) example.

## See Also

[ICollision Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.html)
[ICollision Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
