---
title: "ISetEdges Method (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "ISetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~ISetEdges.html"
---

# ISetEdges Method (IRipFeatureData)

Sets the edges for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEdges( _
   ByVal EdgeCount As System.Integer, _
   ByRef EdgeArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim EdgeCount As System.Integer
Dim EdgeArr As System.Object

instance.ISetEdges(EdgeCount, EdgeArr)
```

### C#

```csharp
void ISetEdges(
   System.int EdgeCount,
   ref System.object EdgeArr
)
```

### C++/CLI

```cpp
void ISetEdges(
   System.int EdgeCount,
   System.Object^% EdgeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCount`: Number of edges
- `EdgeArr`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size EdgeCount
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetEdgesCount.html)
[IRipFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~IGetEdges.html)
[IRipFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Edges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
