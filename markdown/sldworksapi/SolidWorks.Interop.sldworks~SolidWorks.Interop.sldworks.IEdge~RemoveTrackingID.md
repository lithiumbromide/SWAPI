---
title: "RemoveTrackingID Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "RemoveTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.html"
---

# RemoveTrackingID Method (IEdge)

Removes a [tracking ID assigned to this edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~SetTrackingID.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTrackingID( _
   ByVal TrackingCookie As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim TrackingCookie As System.Integer
Dim value As System.Integer

value = instance.RemoveTrackingID(TrackingCookie)
```

### C#

```csharp
System.int RemoveTrackingID(
   System.int TrackingCookie
)
```

### C++/CLI

```cpp
System.int RemoveTrackingID(
   System.int TrackingCookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Edge::RemoveTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Edge~RemoveTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Edge (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Edge_Example_VB.htm)

## Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.html)
[IEdge::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.html)
[IEdge::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.html)
[IEdge::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
