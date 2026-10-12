---
title: "IGetIntersectionEdgeCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetIntersectionEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.html"
---

# IGetIntersectionEdgeCount Method (IBody2)

Gets the number of intersecting edges between this body and the specified tool body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetIntersectionEdgeCount( _
   ByVal ToolBodyIn As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ToolBodyIn As Body2
Dim value As System.Integer

value = instance.IGetIntersectionEdgeCount(ToolBodyIn)
```

### C#

```csharp
System.int IGetIntersectionEdgeCount(
   Body2 ToolBodyIn
)
```

### C++/CLI

```cpp
System.int IGetIntersectionEdgeCount(
   Body2^ ToolBodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToolBodyIn`: Pointer to the temporary body used to perform the intersection

### Return Value

Number of intersection edges

## VBA Syntax

See [Body2::IGetIntersectionEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetIntersectionEdgeCount.html).

## Remarks

Use the return value from this method to determine the size of the array returned by [IBody2::IGetIntersectionEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetIntersectionEdges.html).

If the two bodies are in an assembly, then IBody2::GetIntersectionEdges and IBody2::IGetIntersectionEdges generate a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is positioned the same with respect to the first body as it is in assembly space.

To align the two bodies before calling IBody2::GetIntersectionEdges, IBody2::IGetIntersectionEdges, or Body2::IGetIntersectionEdgeCount, calculate the transformation from the first body to the second body and apply the transform to the second body using [IBody2::ApplyTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ApplyTransform.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
