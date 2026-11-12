---
title: "ISimpleFilletFeatureData2 Interface Properties"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_properties.html"
---

# ISimpleFilletFeatureData2 Interface Properties

For a list of all members of this type, see [ISimpleFilletFeatureData2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AsymmetricFillet | Gets or sets whether this simple fillet/chamfer is asymmetric. |
| Property | ConicTypeForCrossSectionProfile | Gets or sets the cross-sectional profile for this simple fillet. |
| Property | ConstantWidth | Gets or sets whether this simple fillet has a constant width. |
| Property | CurvatureContinuous | Gets or sets whether to create a smoother curvature between adjacent surfaces for this simple fillet feature. |
| Property | DefaultConicRhoOrRadius | Gets or sets the default conic rho or radius. |
| Property | DefaultDistance | Gets or sets the default Distance 2 radius of this asymmetric fillet. |
| Property | DefaultRadius | Gets or sets the default radius of this simple fillet. |
| Property | Edges | Gets or sets the edges for this simple radius fillet. |
| Property | EnablePartialEdgeParameters | Gets or sets whether to enable partial edge properties for all edges of this fillet. |
| Property | Features | Gets or sets the features for this simple fillet radius. |
| Property | FilletItemsCount | Gets the number of fillets for this simple fillet feature. |
| Property | HelpPoint | Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature. |
| Property | HoldLines | Gets or sets the hold lines (boundaries) for a face blend fillet feature. |
| Property | IsMultipleRadius | Gets or sets whether this symmetric fillet or chamfer feature is a multiple radius fillet. |
| Property | KeepFeatures | Gets or sets whether to keep existing features on the entities selected for the fillet. |
| Property | Loops | Gets or sets the loops on which to create a simple radius fillet. |
| Property | OmitAttachedEdges | Gets whether the simple fillet feature is not applied to the attachment edges of the feature. |
| Property | OverflowType | Gets or sets the overflow type of the simple fillet feature. |
| Property | PropagateFeatureToParts | Gets or sets whether to extend the assembly simple fillet feature to all affected parts. |
| Property | PropagateToTangentFaces | Gets or sets whether to extend fillet to all faces tangent to the selected face or edge. |
| Property | ReverseFaceNormal | Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies. |
| Property | RoundCorners | Gets or sets whether to round the corners of this simple fillet feature. |
| Property | TrimAndAttachSurfaces | Gets or sets the Trim surfaces option for surface face fillets. |
| Property | Type | Gets the type of simple fillet feature. |

[Top](#topBookmark)

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.html)
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
