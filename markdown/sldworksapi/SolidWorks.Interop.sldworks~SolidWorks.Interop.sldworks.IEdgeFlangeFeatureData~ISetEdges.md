---
title: "ISetEdges Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ISetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html"
---

# ISetEdges Method (IEdgeFlangeFeatureData)

Sets the edges for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEdges( _
   ByVal EdgeCount As System.Integer, _
   ByRef EdgeArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim EdgeCount As System.Integer
Dim EdgeArray As System.Object

instance.ISetEdges(EdgeCount, EdgeArray)
```

### C#

```csharp
void ISetEdges(
   System.int EdgeCount,
   ref System.object EdgeArray
)
```

### C++/CLI

```cpp
void ISetEdges(
   System.int EdgeCount,
   System.Object^% EdgeArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCount`: Number of edges for this edge flange
- `EdgeArray`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) for this edge flange

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeaturData::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetEdgeCount.html)
[IEdgeFlangeFeaturData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html)
[IEdgeFlangeFeaturData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
