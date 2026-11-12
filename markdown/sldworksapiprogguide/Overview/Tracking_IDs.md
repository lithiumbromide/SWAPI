---
title: "Tracking IDs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Tracking_IDs.htm"
---

# Tracking IDs

### Overview

Tracking IDs allow you to assign IDs to the following topological entities in order to track them across modeling operations such as split, merge, copy, delete, etc.:

- bodies ([IBody2::GetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.html), [IBody2::IGetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.html), [IBody2::GetTrackingIDsCount](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.html), [IBody2::RemoveTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.html), [IBody2::SetTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.html))
- edges ([IEdge::GetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDs.html), [IEdge::IGetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTrackingIDs.html), I[Edge::GetTrackingIDsCount](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTrackingIDsCount.html), [IEdge::RemoveTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveTrackingID.html), [IEdge::SetTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetTrackingID.html))
- faces ([IFace2::GetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.html), [IFace2::IGetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.html), [IFace2::GetTrackingIDsCount](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.html), [IFace2::RemoveTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.html), [IFace2::SetTrackingID)](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.html)
- loops [ILoop2::GetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDs.html), [ILoop2::IGetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetTrackingIDs.html), [ILoop2::GetTrackingIDsCount](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetTrackingIDsCount.html), [ILoop2::RemoveTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RemoveTrackingID.html), [ILoop2::SetTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SetTrackingID.html))
- vertices ([IVertex::GetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDs.html), [IVertex::IGetTrackingIDs](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetTrackingIDs.html), [IVertex::GetTrackingIDsCount,](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetTrackingIDsCount.html) [IVertex::RemoveTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~RemoveTrackingID.html), and [IVertex::SetTrackingID](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~SetTrackingID.html))

Your application can define tracking IDs that are specific to that application to avoid interference with other applications using [ISldWorks::RegisterTrackingDefinition](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterTrackingDefinition.html). Because tracking IDs are intended for use by application developers, there are no visual clues that entities have been assigned tracking IDs. You can find the entities assigned tracking IDs in a document using [IModelDocExtension::FindTrackedObjects](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FindTrackedObjects.html).

### Usage

Tracking IDs are supported within a single model document only and are limited to part and assembly documents. Tracking IDs propagate across modeling operations (e.g., splitting a face in two — both faces inherit the tracking ID of the original face) while attributes, persistent IDs, and safe entities do not.

The lifetime of a tracking ID is from the time of its creation until a rebuild of the model. Attributes, persistent IDs, and safe entities have longer lifetimes. Persistent IDs exist across SOLIDWORKS sessions, and safe entities continue to exist after a rebuild. Attributes behave like features.

By default, tracking IDs are not persistent across SOLIDWORKS sessions. However, you can create a macro feature to assign tracking IDs, which would then allow you to retrieve tracking IDs across SOLIDWORKS sessions.

You can assign a tracking ID to the result body of a macro feature. You assign the tracking ID as the last step, just before the result body is returned by the rebuild function of the macro feature to avoid modifying the body and losing the tracking ID. You assign the tracking ID to the entire body using IBody2::SetTrackingID or to individual entities using, for example, IFace2::SetTrackingID. The latter allows you to reuse the logic required for [IMacroFeatureData::SetFaceUserId](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.html) (for SOLIDWORKS purposes) for assigning a tracking ID (for your purposes).

### Guidelines

You assign a tracking ID before modifying an entity.

You can:

- obtain bodies to which to assign tracking IDs using [IPartDoc::GetBodies2](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.html).
- obtain bodies, belonging to components in assembly documents, to which to assign tracking IDs using [IComponent2::GetBodies](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.html).
- propagate tracking IDs from a part document to component instances of that part in an assembly context. Your application can obtain the corresponding face using [IModelDocExtension::GetCorrespondingEntity](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html). The same tracking ID used in the part document can be assigned to the corresponding face in the component context.
- assign:

You cannot assign tracking IDs:

### Implementation

| Object | Modeling Operation |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| IBody2 | S | M | D | R | C | P |
| IEdge | S | M | D | R | C | N/A |
| IFace2 | S | M | D | R | C | P |
| ILoop2 | S | M | D | R | C | N/A |
| IVertex | S | M | D | R | C | N/A |

S = Assign ID to the new object resulting from the split operation. The number of objects to which the ID is assigned is incremented by 1.

M = Remove ID from the object being merged into another object. The number of objects to which the ID is assigned is decremented by 1.

D = Remove ID from object being deleted. The number of objects to which the ID is assigned is decremented with 1.

R = Remove ID from object and assign it to the object that replaces it. The number of objects to which the ID is assigned remains the same.

C = Assign ID to the new objects resulting from the copy operation. The number of objects to which the ID is assigned is incremented by the number of new copies.

P = Assign ID to new objects corresponding to the source object being patterned. The number of objects to which the ID is assigned is incremented by the number of new pattern instances. Similar implementation for mirror operations.

N/A = Not applicable.
