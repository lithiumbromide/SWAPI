---
title: "IExtrudeFeatureData2 Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_properties.html"
---

# IExtrudeFeatureData2 Interface Properties

For a list of all members of this type, see [IExtrudeFeatureData2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AssemblyFeatureScope | Gets or sets whether to use scope for this assembly extrude feature. |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part. |
| Property | AutoSelectComponents | Gets or sets whether to auto-select all components that this assembly extrude feature affects in model. |
| Property | BothDirections | Gets or sets whether the extrusion is in both directions. |
| Property | CapEnds | Caps the ends for a thin base extrude feature. |
| Property | CapThickness | Gets or sets the end cap thickness for a thin base extrude feature. |
| Property | Contours | Gets and sets the selected contours in this extrude feature. |
| Property | FeatureScope | Gets or sets whether to use scope for the extrude feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the extrude feature affects in a multibody part. |
| Property | FlipSideToCut | Gets or sets whether to flip the side to cut. |
| Property | FromOffsetDistance | Gets or sets the offset distance if IExtrudeFeatureData2::FromType is swExtrudeFrom_Offset. |
| Property | FromOffsetReverse | Gets or sets whether the offset is reverse for this extrusion if IExtrudeFeatureData2::FromType is swExtrudeFrom_Offset. |
| Property | FromType | Gets or sets the type from which to create an extrusion. |
| Property | LinkToThickness | Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature. |
| Property | Merge | Gets or sets whether to merge the results of the extrude feature in a multibody part. |
| Property | NormalCut | Gets or sets whether the cut is created normal to the thickness of the sheet metal part. |
| Property | OptimizeGeometry | Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part. |
| Property | PropagateFeatureToParts | Gets whether to propagate this assembly extrude feature to the parts that it affects in this model. |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of the extrusion feature. |
| Property | ThinWallType | Gets or sets the thin wall type for a thin base extrude feature. |

[Top](#topBookmark)

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut2.html)
[IFeatureManager::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.html)
[IFeatureManager::FeatureExtrusion2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion2.html)
[IFeatureManager::FeatureExtrusionThin2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.html)
