---
title: "ICWMeshControl Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html"
---

# ICWMeshControl Interface Members

The following tables list the members exposed by [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BeamSelected | Obsolete. Superseded by ICWMeshControl::BeamSelected2 . |
| Property | BeamSelected2 | Gets and sets whether to select beams for this mesh control. |
| Property | ElementSize | Gets or sets the element size of the mesh. |
| Property | EntityCount | Gets the number of entities in the mesh control. |
| Property | Layers | Obsolete. Not superseded. |
| Property | MinimumElementSizeForBlendedCurveMesher | Gets and sets the minimum element size for a curvature-based mesh. |
| Property | MinNumOfElementsPerCircleForBlendedCurveMesher | Gets and sets the minimum number of elements in a circle to determine the maximum angle in a curvature-based mesh. |
| Property | Name | Gets the name of the mesh control. |
| Property | NumofElementsforBeams | Gets or sets the total number of mesh elements for selected beams. |
| Property | Ratio | Gets or sets the ratio of the average element size for element layer (i) to that of layer (i-1) for this mesh control. |
| Property | State | Gets whether the mesh control is suppressed. |
| Property | Units | Gets or sets the units for the mesh control. |
| Property | UseSameElementSize | Obsolete. Superseded by ICWMeshControl::UseSameElementSize2 . |
| Property | UseSameElementSize2 | Gets or sets whether to use the the same element for all selected components in this mesh control. |
| Property | WeightFactor | Gets or sets the component weight factor for the mesh control. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetEntityAt | Obsolete. Superseded by ICWMeshControl::GetEntityAt2 . |
| Method | GetEntityAt2 | Obsolete. Superseded by ICWMeshControl::GetEntityAt3 . |
| Method | GetEntityAt3 | Gets the entity at the specified index for this mesh control. |
| Method | InsertEntity | Adds an entity for mesh control. |
| Method | MeshControlBeginEdit | Starts editing the mesh control. |
| Method | MeshControlEndEdit | Ends editing a mesh control. |
| Method | RemoveEntity | Removes the specified entity from the mesh control. |
| Method | SuppressUnSuppress | Suppresses or unsuppresses the mesh control depending on its state . |

[Top](#topBookmark)

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
