---
title: "SetTrackingID Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "SetTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.html"
---

# SetTrackingID Method (IFace2)

Assigns a tracking ID to this face.

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
Dim instance As IFace2
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
  | >0 | Face is tracked |
  | 0 | Tracking of face is stopped |

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Face2::SetTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Face2~SetTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Face (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Face_Example_VB.htm)

## Remarks

You can assign tracking IDs to [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), faces, [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), and [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.html)
[IFace2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.html)
[IFace2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.html)
[IFace2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
