---
title: "RemoveEdges Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "RemoveEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges.html"
---

# RemoveEdges Method (IEdgeFlangeFeatureData)

Removes edges from this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveEdges( _
   ByVal EdgeArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim EdgeArray As System.Object
Dim value As System.Integer

value = instance.RemoveEdges(EdgeArray)
```

### C#

```csharp
System.int RemoveEdges(
   System.object EdgeArray
)
```

### C++/CLI

```cpp
System.int RemoveEdges(
   System.Object^ EdgeArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeArray`: Array of [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)s to remove

### Return Value

Error code as defined by [swEdgeFlangeError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeFlangeError_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::RemoveEdges](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~RemoveEdges.html).

## Examples

[Remove Edge from Edge Flange Feature (C#)](Remove_Edge_from_Edge_Flange_Feature_Example_CSharp.htm)
[Remove Edge from Edge Flange Feature (VB.NET)](Remove_Edge_from_Edge_Flange_Feature_Example_VBNET.htm)
[Remove Edge from Edge Flange Feature (VBA)](Remove_Edge_from_Edge_Flange_Feature_Example_VB.htm)

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html)
[IEdgeFlangeFeatureData::AddEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges.html)
[IEdgeFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html)
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
