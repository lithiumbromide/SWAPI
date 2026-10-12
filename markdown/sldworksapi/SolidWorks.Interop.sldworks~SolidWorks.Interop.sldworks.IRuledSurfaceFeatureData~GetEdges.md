---
title: "GetEdges Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.html"
---

# GetEdges Method (IRuledSurfaceFeatureData)

Gets the edges to used as the base for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEdges( _
   ByRef Edges As System.Object, _
   ByRef SideFlags As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim Edges As System.Object
Dim SideFlags As System.Object

instance.GetEdges(Edges, SideFlags)
```

### C#

```csharp
void GetEdges(
   out System.object Edges,
   out System.object SideFlags
)
```

### C++/CLI

```cpp
void GetEdges(
   [Out] System.Object^ Edges,
   [Out] System.Object^ SideFlags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edges`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `SideFlags`: Array of flags indicating which side of each edge to create the ruled-surface feature

## VBA Syntax

See [RuledSurfaceFeatureData::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~GetEdges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.html)
[IRuledSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.html)
[IRuledSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges.html)
[IRuledSurfaceFeatureData::SetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
