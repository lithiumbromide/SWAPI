---
title: "IGetEdges Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.html"
---

# IGetEdges Method (IRuledSurfaceFeatureData)

Gets the edges to used as the base for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetEdges( _
   ByVal Count As System.Integer, _
   ByRef Entities As System.Object, _
   ByRef SideFlags As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim Count As System.Integer
Dim Entities As System.Object
Dim SideFlags As System.Integer

instance.IGetEdges(Count, Entities, SideFlags)
```

### C#

```csharp
void IGetEdges(
   System.int Count,
   out System.object Entities,
   out System.int SideFlags
)
```

### C++/CLI

```cpp
void IGetEdges(
   System.int Count,
   [Out] System.Object^ Entities,
   [Out] System.int SideFlags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges
- `Entities`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `SideFlags`: - in-process, unmanaged C++: Pointer to an array of flags indicating which side of each edge to create the ruled-surface feature

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRuledSurfaceFeatureData::GetEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.html)
[IRuledSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges.html)
[IRuledSurfaceFeatureData::SetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
