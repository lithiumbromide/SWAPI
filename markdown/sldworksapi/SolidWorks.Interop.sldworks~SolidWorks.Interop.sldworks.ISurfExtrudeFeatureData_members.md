---
title: "ISurfExtrudeFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html"
---

# ISurfExtrudeFeatureData Interface Members

The following tables list the members exposed by [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BothDirections | Gets or sets whether this surface is extruded in both directions. |
| Property | D1CapEnd | Gets or sets whether to cap the end of the extruded surface in Direction 1. |
| Property | D1DraftAngle | Gets or sets the angle of the draft of this extruded surface in Direction 1. |
| Property | D1DraftOn | Gets or sets whether to draft the extruded surface in Direction 1. |
| Property | D1DraftOutward | Gets or sets whether to draft the extruded surface outward or inward in Direction 1. |
| Property | D2CapEnd | Gets or sets whether to cap the end of the extruded surface in Direction 2. |
| Property | D2DraftAngle | Gets or sets the angle of the draft of this extruded surface in Direction 2. |
| Property | D2DraftOn | Gets or sets whether to draft the extruded surface in Direction 2. |
| Property | D2DraftOutward | Gets or sets whether to draft the extruded surface outward or inward in Direction 2. |
| Property | DeleteOriginalFace | Gets or sets whether to delete the original faces of this extruded surface. |
| Property | KnitResult | Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface. |
| Property | ReverseDirection | Gets or sets whether the direction of this extruded surface is reversed. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections that define this extruded surface. |
| Method | GetDepth | Gets the depth of the feature in the forward or reverse direction. |
| Method | GetEndCondition | Gets the end condition of this extruded surface for the forward or reverse direction. |
| Method | GetFace | Gets the end condition face for this extruded surface in the forward or reverse direction. |
| Method | GetReverseOffset | Gets the reverse offset direction setting for the end condition of this extruded surface. |
| Method | GetTranslateSurface | Gets the translate surface setting for this extruded surface. |
| Method | GetVertex | Gets the end condition vertex in the forward or reverse direction for this extruded surface. |
| Method | IAccessSelections | Accesses the selections that define this extruded surface. |
| Method | IGetFace | Gets the end condition face for this extruded surface in the forward or reverse direction. |
| Method | IGetVertex | Gets the end condition vertex in the forward or reverse direction for this extruded surface. |
| Method | ISetFace | Sets the end condition face for this extruded surface in the forward or reverse direction. |
| Method | ISetVertex | Sets the end condition vertex in the forward or reverse direction for this extruded surface. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this extruded surface. |
| Method | SetDepth | Sets the depth of this extruded surface in the forward or reverse direction. |
| Method | SetEndCondition | Sets the end condition of this extruded surface in the forward or reverse direction. |
| Method | SetFace | Sets the end condition face for this extruded surface in the forward or reverse direction. |
| Method | SetReverseOffset | Sets the reverse offset direction setting for the end condition of this extruded surface. |
| Method | SetTranslateSurface | Sets the translate surface setting for this extruded surface. |
| Method | SetVertex | Sets the end condition vertex in the forward or reverse direction for this extruded surface. |

[Top](#topBookmark)

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.html)
[IFeatureManager::FeatureExtruRefSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtruRefSurface2.html)
