---
title: "ISimpleFilletFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html"
---

# ISimpleFilletFeatureData2 Interface Members

The following tables list the members exposed by [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html).

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

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define a simple fillet feature. |
| Method | GetConicRhoOrRadius | Gets the conic rho or radius of this fillet/chamfer. |
| Method | GetDistance | Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer. |
| Method | GetEdgeCount | Gets the number of edges on which to create a simple radius fillet. |
| Method | GetFaceCount | Gets the number of faces on which to create a simple radius fillet. |
| Method | GetFaces | Gets the faces on which to create a simple fillet. |
| Method | GetFeatureCount | Gets the number of features on which to create a simple radius fillet. |
| Method | GetFilletItemAtIndex | Gets the fillet item at the specified index. |
| Method | GetHoldLineCount | Gets the number of hold lines (boundaries) for a face blend fillet feature. |
| Method | GetLoopCount | Gets the number of loops on which to create a single radius fillet. |
| Method | GetPartialEdgeFilletData | Gets the partial edge fillet data for the specified edge. |
| Method | GetRadius | Gets the radius at the specified fillet/chamfer item. |
| Method | GetSetbackDistanceCount | Gets the number of setback distances for the specified vertex on this simple fillet feature. |
| Method | GetSetbackVertexDistance | Gets the setback distance for the specified vertex on this simple fillet feature. |
| Method | GetSetbackVertices | Gets the setback vertices for this simple fillet feature. |
| Method | GetSetbackVerticesCount | Gets the number of setback vertices for this simple fillet feature. |
| Method | IAccessSelections | Gains access to the selections used to define a simple fillet feature. |
| Method | IGetConicRhoOrRadius | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | IGetEdges | Gets the edges on which to put a simple radius fillet. |
| Method | IGetFaces | Gets the faces on which to create a simple radius fillet. |
| Method | IGetFeatures | Gets the features on which to create a simple radius fillet. |
| Method | IGetFilletItemAtIndex | Gets the fillet item at the specified index. |
| Method | IGetHoldLines | Gets the hold lines (boundaries) for a face blend fillet feature. |
| Method | IGetLoops | Gets the loops on which to create a simple radius fillet. |
| Method | IGetRadius | Gets the radius value for specified fillet item. |
| Method | IGetSetbackVertexDistance | Gets the setback distance for the specified vertex on this simple fillet feature. |
| Method | IGetSetbackVertices | Gets the setback vertices for this simple fillet feature. |
| Method | Initialize | Initializes this simple fillet feature to the specified type. |
| Method | ISetConicRhoOrRadius | Sets the conic rho, conic radius, or circular radius of this fillet. |
| Method | ISetEdges | Sets the edges on which to create a simple radius fillet. |
| Method | ISetFaces | Sets the faces on which to create a simple radius fillet. |
| Method | ISetFeatures | Sets the features on which to create a simple radius fillet. |
| Method | ISetHoldLines | Sets the hold lines (boundaries) for this face blend fillet feature. |
| Method | ISetLoops | Sets the loops on which to put a simple radius fillet. |
| Method | ISetRadius | Sets the radius value for specified fillet item. |
| Method | ISetSetbackVertexDistance | Sets the setback distance for the specified vertex and its edges on this simple fillet feature. |
| Method | ISetSetbackVertices | Sets the setback vertices for this simple fillet feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the simple fillet feature. |
| Method | RepairMissingReferences | Finds missing references in this fillet/chamfer and reassigns them to new edges. |
| Method | SetConicRhoOrRadius | Sets the conic rho or radius of this fillet/chamfer. |
| Method | SetDistance | Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer. |
| Method | SetFaces | Sets the faces on which to create a simple fillet. |
| Method | SetPartialEdgeFilletData | Sets the partial edge fillet data for the specified edge. |
| Method | SetRadius | Sets the radius at the specified fillet item. |
| Method | SetSetbackVertexDistance | Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature. |
| Method | SetSetbackVertices | Sets the setback vertices for this simple fillet feature. |

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
