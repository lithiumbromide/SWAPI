---
title: "IChamferFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html"
---

# IChamferFeatureData2 Interface Members

The following tables list the members exposed by [IChamferFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | EdgeChamferAngle | Gets or sets the angle on the edge of the chamfer feature. |
| Property | Edges | Gets or sets a list of the edges to which a chamfer is applied. |
| Property | EqualDistance | Gets or sets whether to specify a single value for distance or vertex. |
| Property | Faces | Gets and sets a list of the faces to which a chamfer is applied. |
| Property | IVertex | Gets or sets the vertex to which a chamfer is applied. |
| Property | KeepFeatures | Gets or sets whether to keep existing features on the entities selected for the chamfer. |
| Property | LoopCount | Gets the number of loops to which a chamfer is applied. |
| Property | Loops | Gets and sets the loops to which a chamfer is applied. |
| Property | PropagateFeatureToParts | Gets or sets whether to extend the chamfer feature to all affected parts in the assembly. |
| Property | TangentPropagation | Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges. |
| Property | Type | Gets or sets the type of chamfer feature. |
| Property | Vertex | Gets or sets the vertex to which a chamfer is applied. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this chamfer feature. |
| Method | GetEdgeChamferDistance | Gets the edge chamfer distance on either side of the edge. |
| Method | GetEdgeCount | Gets the number of edges that are chamfered. |
| Method | GetFaceCount | Gets the number of faces that are chamfered. |
| Method | GetIsFlipped | Gets whether the chamfer feature is flipped. |
| Method | GetVertexChamferDistance | Gets the vertex chamfer distance. |
| Method | IAccessSelections | Accesses the selections that define this chamfer feature. |
| Method | IGetEdges | Gets the edges to which a chamfer is applied. |
| Method | IGetFaces | Gets the faces to which a chamfer is applied. |
| Method | IGetLoops | Gets the loops to which a chamfer is applied. |
| Method | ISetEdges | Sets the edges to which a chamfer is applied. |
| Method | ISetFaces | Gets the faces to which a chamfer is applied. |
| Method | ISetLoops | Sets the loops to which a chamfer is applied. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this chamfer feature. |
| Method | SetEdgeChamferDistance | Sets the edge chamfer distance on either side of the edge. |
| Method | SetIsFlipped | Gets whether the chamfer feature is flipped. |
| Method | SetVertexChamferDistance | Sets the vertex chamfer distance. |

[Top](#topBookmark)

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::FeatureChamfer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamfer.html)
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[IFeatureManager::InsertFeatureChamfer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureChamfer.html)
