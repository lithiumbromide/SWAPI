---
title: "IGetTrackingIDs Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetTrackingIDs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetTrackingIDs.html"
---

# IGetTrackingIDs Method (ILoop2)

Gets the [tracking IDs assigned to this loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~SetTrackingID.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrackingIDs( _
   ByVal TrackingCookie As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef TrackingIDs As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim TrackingCookie As System.Integer
Dim Count As System.Integer
Dim TrackingIDs As System.Integer
Dim value As System.Integer

value = instance.IGetTrackingIDs(TrackingCookie, Count, TrackingIDs)
```

### C#

```csharp
System.int IGetTrackingIDs(
   System.int TrackingCookie,
   System.int Count,
   out System.int TrackingIDs
)
```

### C++/CLI

```cpp
System.int IGetTrackingIDs(
   System.int TrackingCookie,
   System.int Count,
   [Out] System.int TrackingIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)
- `Count`: Number of tracking IDs on this loop
- `TrackingIDs`: - in-process, unmanaged C++: Pointer to an array of tracking IDs on this loop

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## Remarks

Before calling this method, call [ILoop2::GetTrackingIDsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetTrackingIDsCount.html) to get Count.

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDs.html)
[ILoop2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RemoveTrackingID.html)
[ILoop2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SetTrackingID.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
