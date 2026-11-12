---
title: "FindTrackedObjects Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "FindTrackedObjects"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html"
---

# FindTrackedObjects Method (IModelDocExtension)

Finds the tracking IDs assigned to entities in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindTrackedObjects( _
   ByVal TrackingCookie As System.Integer, _
   ByVal SearchObject As System.Object, _
   ByVal TypesFilter As System.Object, _
   ByVal TrackingIDs As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TrackingCookie As System.Integer
Dim SearchObject As System.Object
Dim TypesFilter As System.Object
Dim TrackingIDs As System.Object
Dim value As System.Object

value = instance.FindTrackedObjects(TrackingCookie, SearchObject, TypesFilter, TrackingIDs)
```

### C#

```csharp
System.object FindTrackedObjects(
   System.int TrackingCookie,
   System.object SearchObject,
   System.object TypesFilter,
   System.object TrackingIDs
)
```

### C++/CLI

```cpp
System.Object^ FindTrackedObjects(
   System.int TrackingCookie,
   System.Object^ SearchObject,
   System.Object^ TypesFilter,
   System.Object^ TrackingIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrackingCookie`: Cookie obtained from [ISldWorks::RegisterTrackingDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html)
- `SearchObject`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) or [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to search for tracking IDs; if empty, then all bodies in the document are searched
- `TypesFilter`: Array of the type of entities for which to search as defined by [swTopoEntity_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopoEntity_e.html); valid values are swTopoVertex, swTopoEdge, swTopoLoop, swTopoFace, and swTopoBody; if empty or set to 0, then all types are searched
- `TrackingIDs`: Array of tracking IDs for which to search; if empty, then search for all tracking IDs

### Return Value

Array of objects found that match the specified tracking cookie, types, and tracking IDs; this list can be empty if no matches are found

## VBA Syntax

See [ModelDocExtension::FindTrackedObjects](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~FindTrackedObjects.html)

## Remarks

You can set tracking IDs on [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), and [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in parts and assemblies only; you cannot set tracking IDs on these entities in drawings. See [Tracking IDs](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IBody2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.html)
[IBody2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.html)
[IBody2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.html)
[IBody2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.html)
[IEdge::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.html)
[IEdge::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.html)
[IEdge::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.html)
[IEdge::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.html)
[IFace2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.html)
[IFace2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.html)
[IFace2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.html)
[IFace2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.html)
[ILoop2::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDs.html)
[ILoop2::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDsCount.html)
[ILoop2::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RemoveTrackingID.html)
[ILoop2::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SetTrackingID.html)
[IVertex::GetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.html)
[IVertex::GetTrackingIDsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.html)
[IVertex::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.html)
[IVertex::RemoveTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.html)
[IVertex::SetTrackingID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.html)
[ILoop2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetTrackingIDs.html)
[IFace2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.html)
[IEdge::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.html)
[IBody2::IGetTrackingIDs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
