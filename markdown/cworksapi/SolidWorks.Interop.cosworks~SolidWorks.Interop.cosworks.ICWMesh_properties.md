---
title: "ICWMesh Interface Properties"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh_properties"
member: ""
kind: "properties"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_properties.html"
---

# ICWMesh Interface Properties

For a list of all members of this type, see [ICWMesh members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html).

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

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWStudy::CopyMeshFromStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::CreateMesh Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
