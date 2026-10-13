---
title: "GetComponents Method (ICollision)"
project: "SOLIDWORKS API Help"
interface: "ICollision"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision~GetComponents.html"
---

# GetComponents Method (ICollision)

Gets the components involved in this collision.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICollision
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

See [Collision::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~Collision~GetComponents.html).

## See Also

[ICollision Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.html)
[ICollision Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
