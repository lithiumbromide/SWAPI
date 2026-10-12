---
title: "IGetSilhoutteEdges Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetSilhoutteEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.html"
---

# IGetSilhoutteEdges Method (IFace2)

Gets the silhouette edges for this face with the specified root point and in the specified direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Root As System.Double
Dim Normal As System.Double
Dim value As Edge

value = instance.IGetSilhoutteEdges(Root, Normal)
```

### C#

```csharp
Edge IGetSilhoutteEdges(
   ref System.double Root,
   ref System.double Normal
)
```

### C++/CLI

```cpp
Edge^ IGetSilhoutteEdges(
   System.double% Root,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Root`: Array of doubles defining the root point
- `Normal`: Array of doubles defining the direction vector

### Return Value

- in-process, unmanaged C++: Pointer to an array to hold the edge pointers

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

These edges are not added to the face and cannot be found using [IFace2::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetEdges.html). They are created and handed back to the caller as an array of edges packed with edges.

The vector root point (root) and a vector direction (normal) define the orientation for the silhouette edge creation.

The return array has two elements for each edge: the first is the silhouette edge and the second is not used. To iterate through the edges, an application needs to step through every second element.

Before calling this method, call [IFace2::IGetSilhoutteEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.html) to get the size of array required to hold the edges.

The returned edges are transient and cannot be selected.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetSilhoutteEdgesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
