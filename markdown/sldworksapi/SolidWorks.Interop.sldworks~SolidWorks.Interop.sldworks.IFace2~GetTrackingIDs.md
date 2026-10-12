---
title: "GetTrackingIDs Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTrackingIDs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.html"
---

# GetTrackingIDs Method (IFace2)

Gets the [tracking IDs assigned to this face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~SetTrackingID.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrackingIDs( _
   ByVal TrackingCookie As System.Integer, _
   ByRef TrackingIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim TrackingCookie As System.Integer
Dim TrackingIDs As System.Object
Dim value As System.Integer

value = instance.GetTrackingIDs(TrackingCookie, TrackingIDs)
```

### C#

```csharp
System.int GetTrackingIDs(
   System.int TrackingCookie,
   out System.object TrackingIDs
)
```

### C++/CLI

```cpp
System.int GetTrackingIDs(
   System.int TrackingCookie,
   [Out] System.Object^ TrackingIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)
- `TrackingIDs`: Array of tracking IDs on this face

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## VBA Syntax

See [Face2::GetTrackingIDs](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTrackingIDs.html).

## Examples

[Get, Set, and Remove Tracking IDs on Face (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Face_Example_VB.htm)

## Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.html)
[IFace2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.html)
[IFace2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.html)
[IFace2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
