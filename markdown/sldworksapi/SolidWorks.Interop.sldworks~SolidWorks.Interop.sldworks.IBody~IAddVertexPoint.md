---
title: "IAddVertexPoint Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddVertexPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddVertexPoint.html"
---

# IAddVertexPoint Method (IBody)

Obsolete. Superseded by [IBody2::IAddVertextPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddVertexPoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddVertexPoint( _
   ByRef Point As System.Double _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
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

- `Point`:

## VBA Syntax

See [Body::IAddVertexPoint](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddVertexPoint.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
