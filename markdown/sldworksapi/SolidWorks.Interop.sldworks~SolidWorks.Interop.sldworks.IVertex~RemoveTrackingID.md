---
title: "RemoveTrackingID Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "RemoveTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.html"
---

# RemoveTrackingID Method (IVertex)

Removes a [tracking ID assigned to this vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~SetTrackingID.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTrackingID( _
   ByVal TrackingCookie As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
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

See [Vertex::RemoveTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Vertex~RemoveTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Vertex (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Vertex_Example_VB.htm)

## Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.html)
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.html)
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.html)
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
