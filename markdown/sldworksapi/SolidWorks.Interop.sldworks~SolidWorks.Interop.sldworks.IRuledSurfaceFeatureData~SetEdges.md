---
title: "SetEdges Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "SetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges.html"
---

# SetEdges Method (IRuledSurfaceFeatureData)

Sets the edge to use as the base for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEdges( _
   ByVal Edges As System.Object, _
   ByVal SideFlags As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim Edges As System.Object
Dim SideFlags As System.Object

instance.SetEdges(Edges, SideFlags)
```

### C#

```csharp
void SetEdges(
   System.object Edges,
   System.object SideFlags
)
```

### C++/CLI

```cpp
void SetEdges(
   System.Object^ Edges,
   System.Object^ SideFlags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edges`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `SideFlags`: Array of flags indicating which side of each edge to create the ruled-surface feature

## VBA Syntax

See [RuledSurfaceFeatureData::SetEdges](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~SetEdges.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges.html)
[IRuledSurfaceFeatureData::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.html)
[IRuledSurfaceFeatureData::GetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.html)
[IRuledSurfaceFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
