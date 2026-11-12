---
title: "GetTrackingIDsCount Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetTrackingIDsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.html"
---

# GetTrackingIDsCount Method (IEdge)

Gets the number of tracking IDs on this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrackingIDsCount( _
   ByVal TrackingCookie As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim TrackingCookie As System.Integer
Dim value As System.Integer

value = instance.GetTrackingIDsCount(TrackingCookie)
```

### C#

```csharp
System.int GetTrackingIDsCount(
   System.int TrackingCookie
)
```

### C++/CLI

```cpp
System.int GetTrackingIDsCount(
   System.int TrackingCookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)

### Return Value

NUmber of tracking IDs on this edge

## VBA Syntax

See [Edge::GetTrackingIDsCount](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetTrackingIDsCount.html).

## Examples

[Get, Set, and Remove Tracking IDs on Edge (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Edge_Example_VB.htm)

## Remarks

Call this method before calling [IEdge::IGetTrackingIDs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetTrackingIDs.html) to determine the size for that array.

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.html)
[IEdge::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.html)
[IEdge::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.html)
[IEdge::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
