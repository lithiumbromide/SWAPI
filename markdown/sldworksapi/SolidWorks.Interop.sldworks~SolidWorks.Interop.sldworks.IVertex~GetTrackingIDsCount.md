---
title: "GetTrackingIDsCount Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetTrackingIDsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.html"
---

# GetTrackingIDsCount Method (IVertex)

Gets the number of tracking IDs assigned to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrackingIDsCount( _
   ByVal TrackingCookie As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
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

Number of tracking IDs on this vertex

## VBA Syntax

See [Vertex::GetTrackingIDsCount](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetTrackingIDsCount.html).

## Examples

[Get, Set, and Remove Tracking IDs on Vertex (VBA)](Get_Set_And_Remove_Tracking_IDs_On_Vertex_Example_VB.htm)

## Remarks

Call this method before calling [IVertex::IGetTrackingIDs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~IGetTrackingIDs.html) to determine the size of the array for that method.

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
