---
title: "IAddVertexPoint Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddVertexPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddVertexPoint.html"
---

# IAddVertexPoint Method (IBody2)

Adds a vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddVertexPoint( _
   ByRef Point As System.Double _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Point As System.Double
Dim value As Vertex

value = instance.IAddVertexPoint(Point)
```

### C#

```csharp
Vertex IAddVertexPoint(
   ref System.double Point
)
```

### C++/CLI

```cpp
Vertex^ IAddVertexPoint(
   System.double% Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Vertex to add

### Return Value

[IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [Body2::IAddVertexPoint](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddVertexPoint.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::AddVertexPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddVertexPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
