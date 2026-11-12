---
title: "SetTrackingID Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "SetTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SetTrackingID.html"
---

# SetTrackingID Method (ILoop2)

Assigns a tracking ID to this loop.

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
Dim instance As ILoop2
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
  | >0 | Loop is tracked |
  | 0 | Tracking of loop is stopped |

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Loop2::SetTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Loop2~SetTrackingID.html).

## Remarks

You can assign tracking IDs to [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), loops, and [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in parts and assemblies only; you cannot assign tracking IDs to these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDs.html)
[ILoop2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RemoveTrackingID.html)
[ILoop2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDsCount.html)
[ILoop2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetTrackingIDs.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
