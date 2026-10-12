---
title: "RemoveTrackingID Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "RemoveTrackingID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.html"
---

# RemoveTrackingID Method (IBody2)

Removes a [tracking ID assigned to this body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~SetTrackingID.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTrackingID( _
   ByVal TrackingCookie As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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

See [Body2::RemoveTrackingID](ms-its:sldworksapivb6.chm::/sldworks~Body2~RemoveTrackingID.html).

## Examples

[Get, Set, and Remove Tracking IDs on Body (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Body_Example_VB.htm)

## Remarks

See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.html)
[IBody2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.html)
[IBody2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.html)
[IBody2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.html)
[IModelDocExtension::FindTrackedObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
