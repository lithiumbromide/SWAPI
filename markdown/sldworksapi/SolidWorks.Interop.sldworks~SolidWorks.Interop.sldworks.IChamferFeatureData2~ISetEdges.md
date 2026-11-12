---
title: "ISetEdges Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "ISetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetEdges.html"
---

# ISetEdges Method (IChamferFeatureData2)

Sets the edges to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEdges( _
   ByVal Count As System.Integer, _
   ByRef EdgeList As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim EdgeList As Edge

instance.ISetEdges(Count, EdgeList)
```

### C#

```csharp
void ISetEdges(
   System.int Count,
   ref Edge EdgeList
)
```

### C++/CLI

```cpp
void ISetEdges(
   System.int Count,
   Edge^% EdgeList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges
- `EdgeList`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetEdges.html)
[IChamferFeatureData2::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Edges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
