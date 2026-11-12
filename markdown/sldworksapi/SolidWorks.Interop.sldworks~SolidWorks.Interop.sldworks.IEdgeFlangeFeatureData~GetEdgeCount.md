---
title: "GetEdgeCount Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "GetEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetEdgeCount.html"
---

# GetEdgeCount Method (IEdgeFlangeFeatureData)

Gets the number of edges for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer

value = instance.GetEdgeCount()
```

### C#

```csharp
System.int GetEdgeCount()
```

### C++/CLI

```cpp
System.int GetEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges for this edge flange

## VBA Syntax

See [EdgeFlangeFeatureData::GetEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~GetEdgeCount.html).

## Remarks

Call this method before calling [IEdgeFlangeFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html) to determine the size of the array.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html)
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
