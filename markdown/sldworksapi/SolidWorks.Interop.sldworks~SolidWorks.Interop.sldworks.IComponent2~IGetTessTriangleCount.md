---
title: "IGetTessTriangleCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessTriangleCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriangleCount.html"
---

# IGetTessTriangleCount Method (IComponent2)

Gets the number of triangles that make up the shaded picture tessellation for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriangleCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IGetTessTriangleCount()
```

### C#

```csharp
System.int IGetTessTriangleCount()
```

### C++/CLI

```cpp
System.int IGetTessTriangleCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of triangles that make up the shaded picture tessellation for this component

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
