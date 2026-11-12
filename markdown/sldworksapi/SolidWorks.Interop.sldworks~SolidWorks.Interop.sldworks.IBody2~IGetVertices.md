---
title: "IGetVertices Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetVertices.html"
---

# IGetVertices Method (IBody2)

Gets the vertices in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertices( _
   ByVal Count As System.Integer _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Count As System.Integer
Dim value As Vertex

value = instance.IGetVertices(Count)
```

### C#

```csharp
Vertex IGetVertices(
   System.int Count
)
```

### C++/CLI

```cpp
Vertex^ IGetVertices(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of vertices in this body

### Return Value

- in-process, unmanaged C++: Pointer to an array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in this body

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBody2::GetVertexCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetVertexCount.html) to determine the size of the array.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[GetVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertices.html)
