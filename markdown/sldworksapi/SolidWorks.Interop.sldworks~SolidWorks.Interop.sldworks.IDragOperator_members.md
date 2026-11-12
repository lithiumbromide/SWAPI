---
title: "IDragOperator Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDragOperator_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html"
---

# IDragOperator Interface Members

The following tables list the members exposed by [IDragOperator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ApplyToThisConfiguration | Gets or sets the configurations to which to apply the movement of the components. |
| Property | Clearance | Gets the clearance distance between the components. |
| Property | CollisionDetectionEnabled | Gets or sets the collision detection setting. |
| Property | DragCorrected | Gets whether or not the drag operation was corrected. |
| Property | DragMode | Gets or sets the drag mode for this drag operation. |
| Property | DynamicClearanceEnabled | Gets or sets the dynamic clearance setting. |
| Property | GraphicsRedrawEnabled | Gets or sets whether or not to update the graphics display after moving components. |
| Property | HearClashes | Gets or sets whether sound is associated with entity clashes. |
| Property | HighlightClashes | Gets or sets whether to highlight clashes. |
| Property | IgnoreComplexSurfaces | Gets or sets whether complex surfaces are ignored. |
| Property | IsDragByRay | Gets or sets the drag-by-ray setting. |
| Property | IsDragSpecific | Gets or sets the drag-specific setting. |
| Property | IsRelaxationEval | Gets or sets the relaxation evaluation. |
| Property | SmartMating | Gets or sets SmartMates. |
| Property | TransformType | Gets or sets the type of transformation. |
| Property | UseAbsoluteTransform | Gets or sets whether the transforms to use with IDragOperator::Drag or IDragOperator::IDrag are absolute or relative. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddComponent | Adds a component to the list of components to drag. |
| Method | AddDynamicClearance | Adds a dynamic clearance detector. |
| Method | BeginDrag | Initiates the drag operation. |
| Method | CollisionDetection | Sets the collision detection parameters. |
| Method | Drag | Sets the transform matrix for this drag operation. |
| Method | DragAsUI | Sets the transform matrix for this drag operation. |
| Method | EndDrag | Terminates the drag operation. |
| Method | GetDragPoint | Gets the drag point. |
| Method | IAddComponent | Adds a component to the list of components to drag. |
| Method | IAddDynamicClearance | Adds a dynamic clearance detector. |
| Method | ICollisionDetection | Sets the collision detection parameters. |
| Method | IDrag | Sets the transform matrix for this drag operation. |
| Method | IGetDragPoint | Gets the drag point. |
| Method | ISetDragPoint | Sets the drag point. |
| Method | SetDragPoint | Sets the drag point. |

[Top](#topBookmark)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
