---
title: "ISetEdges Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "ISetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~ISetEdges.html"
---

# ISetEdges Method (IShutOffSurfaceFeatureData)

Sets the edges to use to form closed loops for patches.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEdges( _
   ByVal Count As System.Integer, _
   ByRef EdgeArr As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim Count As System.Integer
Dim EdgeArr As Edge

instance.ISetEdges(Count, EdgeArr)
```

### C#

```csharp
void ISetEdges(
   System.int Count,
   ref Edge EdgeArr
)
```

### C++/CLI

```cpp
void ISetEdges(
   System.int Count,
   Edge^% EdgeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges
- `EdgeArr`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetEdgeCount.html)
[IShutOffSurfaceFeatureData::GetLoopEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.html)
[IShutOffSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.html)
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.html)
[IShutOffSurfaceFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Edges.html)
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
