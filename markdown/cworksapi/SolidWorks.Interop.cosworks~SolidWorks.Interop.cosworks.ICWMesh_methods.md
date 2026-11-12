---
title: "ICWMesh Interface Methods"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh_methods"
member: ""
kind: "methods"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_methods.html"
---

# ICWMesh Interface Methods

For a list of all members of this type, see [ICWMesh members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html).

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
