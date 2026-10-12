---
title: "IGetPoint Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IGetPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetPoint.html"
---

# IGetPoint Method (IVertex)

Gets the point corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPoint() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Double

value = instance.IGetPoint()
```

### C#

```csharp
System.double IGetPoint()
```

### C++/CLI

```cpp
System.double IGetPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of three doubles representing the x, y, and z coordinates of the point

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetPoint.html)
