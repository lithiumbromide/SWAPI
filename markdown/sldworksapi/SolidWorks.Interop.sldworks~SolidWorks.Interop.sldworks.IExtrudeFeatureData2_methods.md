---
title: "IExtrudeFeatureData2 Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_methods.html"
---

# IExtrudeFeatureData2 Interface Methods

For a list of all members of this type, see [IExtrudeFeatureData2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define the extrusion feature. |
| Method | GetAutoFilletCorners | Gets whether the corners of this thin feature are automatically filleted. |
| Method | GetAutoFilletRadius | Gets the automatic corner fillet radius for this thin feature. |
| Method | GetContoursCount | Gets the number of selected contours for this extrude feature. |
| Method | GetDepth | Gets the depth of the extrusion feature in the forward or reverse direction. |
| Method | GetDirectionReference | Gets the direction of the extrusion. |
| Method | GetDraftAngle | Gets the draft angle of the extrusion in the forward or reverse direction. |
| Method | GetDraftOutward | Gets whether the extrusion feature is drafted outward in the forward or reverse direction. |
| Method | GetDraftWhileExtruding | Gets whether the feature is drafted while extruding in the forward or reverse direction. |
| Method | GetEndCondition | Gets the type of end condition of this extrusion feature for forward or reverse direction. |
| Method | GetEndConditionReference | Gets the reference entity defining the end condition in the forward or reverse direction. |
| Method | GetFace | Obsolete. Superseded by IExtrudeFeatureData2::GetEndConditionReference . |
| Method | GetFeatureScopeBodiesCount | Gets the number of solid bodies affected by the extrude feature in a multibody part. |
| Method | GetFromEntity | Gets the entity and its type from which the extrusion was created. |
| Method | GetReverseOffset | Gets the offset direction for this extrude feature. |
| Method | GetTranslateSurface | Gets the translate surface setting for this extrude feature. |
| Method | GetVertex | Obsolete. Superseded by IExtrudeFeatureData2::GetEndConditionReference . |
| Method | GetWallThickness | Gets the wall thickness of the thin extrusion feature in forward or reverse direction. |
| Method | IAccessSelections | Gains access to the selections used to define the extrusion feature. |
| Method | IGetContours | Gets the selected contours for this extrude feature. |
| Method | IGetFace | Obsolete. Superseded by IExtrudeFeatureData2::GetEndConditionReference . |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the extrude feature affects in a multibody part. |
| Method | IGetVertex | Obsolete. Superseded by IExtrudeFeatureData2::GetEndConditionReference . |
| Method | IsBaseExtrude | Obsolete. Superseded by IFeature::IsBase2 . |
| Method | IsBossFeature | Gets whether the extrusion is a boss feature. |
| Method | ISetChangeToConfigurations | Applies changes made to this extrude feature to the specified configurations. |
| Method | ISetContours | Sets the selected contours for this extrude feature. |
| Method | ISetFace | Obsolete. Superseded by IExtrudeFeatureData2::SetEndConditionReference . |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that the extrude feature affects in the multibody part. |
| Method | ISetVertex | Obsolete. Superseded by IExtrudeFeatureData2::SetEndConditionReference . |
| Method | IsThinFeature | Gets whether the extrusion is a thin feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the extrude feature. |
| Method | SetAutoFillet | Sets the automatic corner fillet properties of this thin feature. |
| Method | SetChangeToConfigurations | Applies changes made to this extrude feature to the specified configurations. |
| Method | SetDepth | Sets the depth of the feature in the forward or reverse direction. |
| Method | SetDirectionReference | Sets the direction of the extrusion. |
| Method | SetDraftAngle | Sets the draft angle of the extrusion in the forward or reverse direction. |
| Method | SetDraftOutward | Sets whether the extrusion feature should draft outward in the forward or reverse direction. |
| Method | SetDraftWhileExtruding | Sets whether the feature is drafted while extruding in the forward or reverse direction. |
| Method | SetEndCondition | Sets the end condition type of the extrusion feature for the forward or reverse direction. |
| Method | SetEndConditionReference | Sets the reference entity that defines the end condition in a forward or reverse direction. |
| Method | SetFace | Obsolete. Superseded by IExtrudeFeatureData2::SetEndConditionReference . |
| Method | SetFromEntity | Sets the entity from which to create an extrusion. |
| Method | SetReverseOffset | Sets the offset direction for this extrude feature. |
| Method | SetTranslateSurface | Sets the translate surface setting for this extrude feature. |
| Method | SetVertex | Obsolete. Superseded by IExtrudeFeatureData2::SetEndConditionReference . |
| Method | SetWallThickness | Sets the wall thickness of the thin extrusion feature in a forward or reverse direction. |

[Top](#topBookmark)

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2.html)
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.html)
[IFeatureManager::FeatureExtrusion2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion2.html)
[IFeatureManager::FeatureExtrusionThin2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.html)
