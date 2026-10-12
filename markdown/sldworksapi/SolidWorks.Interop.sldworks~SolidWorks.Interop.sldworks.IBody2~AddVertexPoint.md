---
title: "AddVertexPoint Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddVertexPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddVertexPoint.html"
---

# AddVertexPoint Method (IBody2)

Adds a vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVertexPoint( _
   ByVal Point As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Point As System.Object
Dim value As System.Object

value = instance.AddVertexPoint(Point)
```

### C#

```csharp
System.object AddVertexPoint(
   System.object Point
)
```

### C++/CLI

```cpp
System.Object^ AddVertexPoint(
   System.Object^ Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Vertex to add

### Return Value

[IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [Body2::AddVertexPoint](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddVertexPoint.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IAddVertexPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddVertexPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
