---
title: "ISetEdges Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.html"
---

# ISetEdges Method (ISimpleFilletFeatureData2)

Sets the edges on which to create a simple radius fillet.

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
Dim instance As ISimpleFilletFeatureData2
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

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.html)
[ISimpleFilletFeatureData2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount.html)
[ISimpleFilletFeatureData2::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
