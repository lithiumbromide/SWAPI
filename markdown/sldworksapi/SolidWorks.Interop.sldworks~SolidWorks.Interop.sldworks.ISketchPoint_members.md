---
title: "ISketchPoint Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html"
---

# ISketchPoint Interface Members

The following tables list the members exposed by [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the color of this sketch point. |
| Property | Layer | Gets or sets the layer for this sketch point. |
| Property | LayerOverride | Gets or sets whether the sketch point has properties that override the default properties of the layer. |
| Property | Status | Gets or sets the status of the associated relation for this sketch point. |
| Property | Type | Gets or sets the type of sketch point. |
| Property | X | Gets or sets the x coordinate of the sketch point. |
| Property | Y | Gets or sets the y coordinate of the sketch point. |
| Property | Z | Gets or sets the z coordinate of the sketch point. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | DeSelect | Deselects the sketch point. |
| Method | GetCoords | Gets the x coordinate of the sketch point. |
| Method | GetFramePointTangent | Obsolete. Not superseded. |
| Method | GetID | Gets the sketch point ID for this sketch point. |
| Method | GetRelations | Gets the sketch relations for this sketch point. |
| Method | GetRelationsCount | Gets the number of sketch relations for this sketch point. |
| Method | GetSketch | Gets the sketch for the current sketch point. |
| Method | GetSketchSlot | Gets sketch slot with which this sketch point is associated. |
| Method | IGetFramePointTangent | Obsolete. Not superseded. |
| Method | IGetID | Gets the sketch point ID for this sketch point. |
| Method | IGetRelations | Gets the sketch relations for this sketch point. |
| Method | ISetFramePointTangent | Obsolete. Not superseded. |
| Method | Select | Obsolete. Superseded by ISketchPoint::Select4 . |
| Method | Select2 | Obsolete. Superseded by ISketchPoint::Select4 . |
| Method | Select3 | Obsolete. Superseded by ISketchPoint::Select4 . |
| Method | Select4 | Selects the sketch point and marks it. |
| Method | SelectByMark | Obsolete. Superseded by ISketchPoint::Select4 . |
| Method | SetCoords | Sets the location of this sketch point. |
| Method | SetFramePointTangent | Obsolete. Not superseded. |

[Top](#topBookmark)

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.html)
[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.html)
[IRefPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)
