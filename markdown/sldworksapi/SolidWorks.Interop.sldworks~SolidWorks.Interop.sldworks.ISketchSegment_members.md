---
title: "ISketchSegment Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html"
---

# ISketchSegment Interface Members

The following tables list the members exposed by [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the color of this sketch segment. Sketch segment color is only supported in drawing documents. |
| Property | ConstructionGeometry | Gets or sets whether this sketch segment is construction geometry, for example, a centerline for a feature revolve operation. |
| Property | Layer | gets or sets the layer used by this sketch segment. |
| Property | LayerOverride | Gets or sets whether the sketch segment has properties that override the default properties of the layer. |
| Property | Status | Gets the constraint status for this sketch segment. NOTE: This property is a get-only property. Set is not implemented. |
| Property | Style | Gets or sets the line style for this sketch segment. |
| Property | Width | Gets or sets the line width for this sketch segment. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateWireBody | Creates a wire body using the selected sketch segment. |
| Method | DeSelect | Deselects the sketch segment. |
| Method | EqualSegment | Divides this sketch segment into equally spaced sketch segments or points. |
| Method | GetConstraints | Gets the constraints for this sketch segment. |
| Method | GetCurve | Gets the underlying curve for this sketch segment. |
| Method | GetID | Gets the for this sketch segment. |
| Method | GetLength | Gets the length of this sketch segment. |
| Method | GetName | Gets the name of this sketch segment. |
| Method | GetRelations | Gets the sketch relations for this sketch segment. |
| Method | GetRelationsCount | Gets the number of sketch relations for this sketch segment. |
| Method | GetSketch | Gets the sketch for the current sketch segment. |
| Method | GetSketchPathCount | Gets the number of sketch paths for this sketch segment |
| Method | GetSketchPaths | Gets the sketch paths for this sketch segment. |
| Method | GetSketchSlot | Gets sketch slot with which this sketch segment is associated. |
| Method | GetType | Gets the type of sketch segment. |
| Method | IGetConstraints | Gets the constraints for this sketch segment. |
| Method | IGetConstraintsCount | Gets the number of constraints on the sketch segment. |
| Method | IGetCurve | Gets the underlying curve for this sketch segment. |
| Method | IGetID | Gets the ID for this sketch segment. |
| Method | IGetRelations | Gets the sketch relations for this sketch segment. |
| Method | IGetSketchPaths | Gets the sketch paths in this sketch segment. |
| Method | IsBendLine | Gets whether the sketch segment is a bendline. |
| Method | JogLine | Creates rectangular jog on the specified line. |
| Method | Select | Obsolete. Superseded by ISketchSegment::Select4 . |
| Method | Select2 | Obsolete. Superseded by ISketchSegment::Select4 . |
| Method | Select3 | Obsolete. Superseded by ISketchSegment::Select4 . |
| Method | Select4 | Selects this sketch segment and marks it. |
| Method | SelectByMark | Obsolete. Superseded by ISketchSegment::Select4 . |
| Method | SelectChain | Selects chains of entities attached to this sketch segment. |
| Method | SplitEntity | Splits the selected sketch entity at the specified point. |

[Top](#topBookmark)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
