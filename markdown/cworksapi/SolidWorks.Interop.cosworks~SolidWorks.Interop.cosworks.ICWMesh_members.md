---
title: "ICWMesh Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html"
---

# ICWMesh Interface Members

The following tables list the members exposed by [ICWMesh](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutomaticLooping | Obsolete. Superseded by ICWMesh::AutomaticLooping2 . |
| Property | AutomaticLooping2 | Gets or sets whether to automatically retry to mesh the model using a different global element size for solids. |
| Property | AutomaticTransition | Obsolete. Superseded by ICWMesh::AutomaticTransition2 . |
| Property | AutomaticTransition2 | Gets or sets whether mesh controls are automatically applied to small features, holes, fillets, and other fine details in the model. |
| Property | ElementCount | Gets the number of elements in the mesh. |
| Property | ElementSize | Gets or sets the global element size. |
| Property | ElementSizeFactorForEachLoop | Obsolete. Not superseded. |
| Property | GrowthRatio | Gets or sets the global element size growth ratio starting from regions of highest curvatures in all directions in a curvature-based mesh. |
| Property | IsMeshFailed | Obsolete. Superseded by ICWMesh::IsMeshFailed2 . |
| Property | IsMeshFailed2 | Checks the status of the mesh. |
| Property | JacobianPoints | Gets or sets the number of points to be used in calculating a Jacobian ratio. |
| Property | MaxAspectRatio | Gets the maximum aspect ratio for all elements in the mesh. |
| Property | MaxElementSize | Gets the maximum element size used for boundaries with lowest curvature in a curvature-based mesh. |
| Property | MeshControlCount | Gets the number of mesh controls defined in the active study. |
| Property | MesherType | Gets or sets the type of mesh. |
| Property | MeshState | Gets the mesh state. |
| Property | MeshType | Returns the mesh type. |
| Property | MinElementsInCircle | Gets or sets the minimum number of elements around a circle to determine the maximum angle in a curvature-based mesh. |
| Property | MinElementSize | Gets the minimum element size used for boundaries with highest curvature in a curvature-based mesh. |
| Property | NegativeJacobianRatioCheck | Obsolete. Superseded by ICWMesh::NegativeJacobianRatioCheck2 . |
| Property | NegativeJacobianRatioCheck2 | Gets or sets whether to check for a negative Jacobian ratio while meshing. |
| Property | NodeCount | Gets the number of nodes in the active study. |
| Property | NumberOfLoops | Gets or sets the number of loops for automatic mesh looping. |
| Property | Quality | Gets or sets the mesh quality. |
| Property | SaveSettingsWithoutMeshing | Obsolete. Superseded by ICWMesh::SaveSettingsWithoutMeshing2 . |
| Property | SaveSettingsWithoutMeshing2 | Gets or sets whether to save mesh settings without meshing. |
| Property | SmoothSurface | Obsolete. Not superseded. |
| Property | SmoothSurface2 | Obsolete. Not superseded. |
| Property | TimeToCompleteMesh | Gets the estimated time to complete the mesh. |
| Property | Tolerance | Gets the tolerance value for mesh loops. |
| Property | ToleranceFactorForEachLoop | Obsolete. Not superseded. |
| Property | Unit | Gets the units for the mesh. |
| Property | UseJacobianCheckForShells | Obsolete. Superseded by ICWMesh::UseJacobianCheckForShells2 . |
| Property | UseJacobianCheckForShells2 | Gets or sets whether to perform a Jacobian check for shells. |
| Property | UseJacobianCheckForSolids | Gets or sets whether to perform a Jacobian check for solids. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ApplyMeshControl | Creates a mesh control. |
| Method | DeleteMeshControl | Deletes a mesh control. |
| Method | FlipShellElements | Flips shell elements associated with the selected shells (i.e., top face becomes the bottom face and vice versa). |
| Method | GetConnectivity | Gets the connectivity of nodes on the surface of the model. |
| Method | GetDefaultElementSizeAndTolerance | Gets the default element size and tolerance. |
| Method | GetDefaultMaxAndMinElementSize | Gets the default maximum and minimum element sizes used for boundaries in a curvature-based mesh. |
| Method | GetElementDataFromEntity | Gets the element associated with an entity. |
| Method | GetElementList | Gets the elements of the specified type. |
| Method | GetElementLocation | Gets the coordinates of an element's center. |
| Method | GetElements | Gets the elements of the mesh. |
| Method | GetFailedComponents | Gets the components that failed to mesh. |
| Method | GetFailedEdges | Gets the edges that failed to mesh. |
| Method | GetFailedFaces | Gets the faces that failed to mesh. |
| Method | GetMeshControlAt | Gets mesh control at the specified index. |
| Method | GetNodeDataFromEntity | Gets the node data associated with an entity. |
| Method | GetNodeList | Gets the nodes of elements of the specified type. |
| Method | GetNodeLocation | Gets the coordinates of the specified node. |
| Method | GetNodeOutwardDirections | Gets the normal directions at all of the nodes on the surface of this mesh. |
| Method | GetNodes | Gets all of the nodes in the mesh. |
| Method | GetNoOfFailedComponents | Gets the number of components that failed to mesh. |
| Method | GetPoorMeshQualityElementList | Obsolete. Superseded by ICWMesh::GetPoorMeshQualityElementList2 . |
| Method | GetPoorMeshQualityElementList2 | Gets the Mesh Quality Diagnostics element list. |
| Method | GetShellElementNormalAt | Gets shell normal for a face. |
| Method | GetSolidElementList | Gets the elements at the specified depth of this solid mesh. |
| Method | GetSolidNodeList | Gets the nodes at the specified depth of this solid mesh. |
| Method | GetSurfaceNodesAndNormals | Gets the nodes and normal vectors at the surface of this solid mesh. |
| Method | GetWorstJacobianRatio | Gets the worst Jacobian ratio for this mesh. |
| Method | IsComponentFailed | Obsolete. Superseded by ICWMesh::IsComponentFailed2 . |
| Method | IsComponentFailed2 | Checks the status of the specified component. |
| Method | SetMeshAndParamsForDefaultBCB | Sets the mesher to be blended curvature based. |

[Top](#topBookmark)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWStudy::CopyMeshFromStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::CreateMesh Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
