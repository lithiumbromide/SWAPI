---
title: "EnumEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "EnumEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumEdges.html"
---

# EnumEdges Method (ILoop2)

Enumerates the edges in a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumEdges() As EnumEdges
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As EnumEdges

value = instance.EnumEdges()
```

### C#

```csharp
EnumEdges EnumEdges()
```

### C++/CLI

```cpp
EnumEdges^ EnumEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Edges enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html)

## VBA Syntax

See [Loop2::EnumEdges](ms-its:sldworksapivb6.chm::/sldworks~Loop2~EnumEdges.html).

## Remarks

The edge objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

Because an edge is shared by multiple loops, the edge direction may be opposite to the direction of the ILoop2. To check this, use [IEdge::EdgeInFaceSense](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~EdgeInFaceSense.html).

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdgeCount.html)
[ILoop2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetEdges.html)
[ILoop2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
