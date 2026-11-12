---
title: "IGetEdges Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetEdges.html"
---

# IGetEdges Method (IChamferFeatureData2)

Gets the edges to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetEdges(Count)
```

### C#

```csharp
Edge IGetEdges(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetEdges(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IChamferFeatureData2::GetEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~GetEdgeCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetEdges.html)
[IChamferFeatureData2::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Edges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
