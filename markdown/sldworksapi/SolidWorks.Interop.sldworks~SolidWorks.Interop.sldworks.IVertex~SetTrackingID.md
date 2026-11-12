---
title: "SetTrackingID Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "SetTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.html"
---

# SetTrackingID Method (IVertex)

Assigns a tracking ID to this vertex.

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
Dim instance As IVertex
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
  | >0 | Vertex is tracked |
  | 0 | Tracking of vertex is stopped |

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Vertex::SetTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Vertex~SetTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Vertex (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Vertex_Example_VB.htm)

## Remarks

You can assign tracking IDs to [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), and vertices in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.html)
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.html)
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.html)
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
