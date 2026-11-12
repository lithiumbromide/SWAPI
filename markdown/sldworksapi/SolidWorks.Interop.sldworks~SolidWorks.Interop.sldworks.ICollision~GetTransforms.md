---
title: "GetTransforms Method (ICollision)"
project: "SOLIDWORKS API Help"
interface: "ICollision"
member: "GetTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~GetTransforms.html"
---

# GetTransforms Method (ICollision)

Gets the current transforms of the components involved in this collision.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransforms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICollision
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

See [Collision::GetTransforms](ms-its:sldworksapivb6.chm::/sldworks~Collision~GetTransforms.html).

## See Also

[ICollision Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.html)
[ICollision Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
