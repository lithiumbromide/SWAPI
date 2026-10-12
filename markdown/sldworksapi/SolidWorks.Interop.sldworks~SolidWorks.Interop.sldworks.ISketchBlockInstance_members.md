---
title: "ISketchBlockInstance Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html"
---

# ISketchBlockInstance Interface Members

The following tables list the members exposed by [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the angle around the insertion point which to rotate this block instance. |
| Property | BlockToSketchTransform | Gets the MathTransform required to transform coordinates from the sketch block space to the host sketch space. |
| Property | Definition | Gets or sets the block definition for this block instance. |
| Property | DimensionDisplay | Gets whether dimensions are displayed. |
| Property | InstancePosition | Gets or sets the position for this block instance. |
| Property | Layer | Gets or sets the name of the layer where this block is located. |
| Property | LockAngle | Gets or sets whether the angle around the insertion point which to rotate this block instance is locked. |
| Property | Name | Gets or sets the name of this block instance. |
| Property | Scale | Obsolete. Superseded by ISketchBlockInstance::Scale2 . |
| Property | Scale2 | Sets the scale for this block instance. |
| Property | TextDisplay | Gets or sets whether to display text for this block instance. |
| Property | Visible | Gets or sets the visibility of this block instance. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetArrowHeadStyle | Gets the arrowhead style of the leader on this block instance. |
| Method | GetAttachedEntities | Gets the entities to which this block instance is attached. |
| Method | GetAttributeCount | Gets the number of attributes for this block instance. |
| Method | GetAttributes | Gets the attributes for this block instance. |
| Method | GetAttributeValue | Gets the value of the specified attribute for this block instance. |
| Method | GetLeaderPoints | Gets the coordinate information for the leader on this block instance. |
| Method | GetLeaderStyle | Gets the leader style of this block instance. |
| Method | GetScale3 | Gets the scale for this block instance. |
| Method | GetSketch | Gets the sketch in which this block instance is present. |
| Method | IGetAttributes | Gets the attributes for this block instance. |
| Method | IGetLeaderPoints | Gets the coordinate information for the leader on this block instance. |
| Method | IsNested | Gets whether this sketch block instance is nested within another block definition. |
| Method | Select | Selects and marks the block instance. |
| Method | SetAttributeValue | Sets the value of the specified attribute for this block instance. |
| Method | SetLeader | Sets the leader style for this block instance. |

[Top](#topBookmark)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
