---
title: "IGetEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetEdges.html"
---

# IGetEdges Method (ILoop2)

Gets all the edges in the loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges() As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As Edge

value = instance.IGetEdges()
```

### C#

```csharp
Edge IGetEdges()
```

### C++/CLI

```cpp
Edge^ IGetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) that make up the loop

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, use [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

Because an edge is shared by multiple loops, the edge direction might be opposite to the direction of the ILoop2. To check this, use [IEdge::IEdgeInFaceSense2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IEdgeInFaceSense2.html).

If the loop is a singular loop, use [ILoop2::IGetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetVertices.html) to get its position (a single vertex). LIoop2::GetEdges returns an empty array if the loop is singular.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdgeCount.html)
[ILoop2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdges.html)
[ILoop2::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
