---
title: "SetTrackingID Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "SetTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.html"
---

# SetTrackingID Method (IEdge)

Assigns a tracking ID to this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTrackingID( _
   ByVal TrackingCookie As System.Integer, _
   ByVal TrackingID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim TrackingCookie As System.Integer
Dim TrackingID As System.Integer
Dim value As System.Integer

value = instance.SetTrackingID(TrackingCookie, TrackingID)
```

### C#

```csharp
System.int SetTrackingID(
   System.int TrackingCookie,
   System.int TrackingID
)
```

### C++/CLI

```cpp
System.int SetTrackingID(
   System.int TrackingCookie,
   System.int TrackingID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)
- `TrackingID`: Application-defined value for the tracking ID

  | Value | Action |
  | --- | --- |
  | >0 | Edge is tracked |
  | 0 | Tracking of edge is stopped |

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Edge::SetTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Edge~SetTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Edge (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Edge_Example_VB.htm)

## Remarks

You can assign tracking IDs to [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), edges, [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), and [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.html)
[IEdge::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.html)
[IEdge::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.html)
[IEdge::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
