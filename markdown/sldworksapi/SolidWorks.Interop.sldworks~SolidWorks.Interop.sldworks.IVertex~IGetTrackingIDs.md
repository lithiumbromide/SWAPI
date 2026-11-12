---
title: "IGetTrackingIDs Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IGetTrackingIDs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.html"
---

# IGetTrackingIDs Method (IVertex)

Gets the [tracking IDs assigned to this vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~SetTrackingID.html).

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
Dim instance As IVertex
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
- `Count`: Number of tracking IDs on this vertex
- `TrackingIDs`: - in-process, unmanaged C++: Pointer to an array of tracking IDs on this vertex

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Status as defined by [swTrackingIDError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTrackingIDError_e.html)

## Remarks

Before calling this method, call [IVertex::GetTrackingIDsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~GetTrackingIDsCount.html) to get Count.

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.html)
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.html)
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
