---
title: "IGetIntersectionEdges Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetIntersectionEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdges.html"
---

# IGetIntersectionEdges Method (IBody2)

Obsolete. Superseded by [IBody2::GetIntersectionEdges2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetIntersectionEdges( _
   ByVal ToolBodyIn As Body2 _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ToolBodyIn As Body2
Dim value As Edge

value = instance.IGetIntersectionEdges(ToolBodyIn)
```

### C#

```csharp
Edge IGetIntersectionEdges(
   Body2 ToolBodyIn
)
```

### C++/CLI

```cpp
Edge^ IGetIntersectionEdges(
   Body2^ ToolBodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToolBodyIn`: Temporary [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) used to perform the intersection

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method imprints a set of edges on both of these temporary bodies and returns the edges in an unordered list as shown below. The total number of edges in this array is twice the value returned from
[IBody2::IGetIntersectionEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.html).

**[** `Edge1imprintedOnTarget, Edge1imprintedOnTool, Edge2imprintedOnTarget, Edge2imprintedOnTool` **]**

where the target body is the IBody2 object used to call this method and the tool body is passed into this method as the first argument.

If the two bodies are in an assembly, then IBody2::GetIntersectionEdges generates a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is positioned the same with respect to the first body as it is in assembly space.

To align the two bodies before calling IBody2::GetIntersectionEdges or IBody2::IGetIntersectionEdgeCount, calculate the transformation from the first body to the second body and set this as the transform for the second body using [IBody2::ApplyTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ApplyTransform.html).

In the case of a tangency condition (for example, a planar face contacting the cylindrical face of a cylinder), this method returns a single edge along the tangency.

You might also find that [IBody2::IOperations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html) provides an adequate solution. This method intersects a sheet body with a target body.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetIntersectionEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
