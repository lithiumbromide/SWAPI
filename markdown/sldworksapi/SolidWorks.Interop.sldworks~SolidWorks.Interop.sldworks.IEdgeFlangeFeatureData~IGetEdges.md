---
title: "IGetEdges Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.html"
---

# IGetEdges Method (IEdgeFlangeFeatureData)

Gets the edges for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges( _
   ByVal EdgeCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim EdgeCount As System.Integer
Dim value As System.Object

value = instance.IGetEdges(EdgeCount)
```

### C#

```csharp
System.object IGetEdges(
   System.int EdgeCount
)
```

### C++/CLI

```cpp
System.Object^ IGetEdges(
   System.int EdgeCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCount`: Number of edges for this edge flange

### Return Value

- in-process, unmanaged C++: Pointer to an array of edges for this edge flange

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IEdgeFlangeFeatureData::GetEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~GetEdgeCount.html) before calling this method to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.html)
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
