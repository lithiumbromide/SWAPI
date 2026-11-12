---
title: "ISketchHatch Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html"
---

# ISketchHatch Interface Members

The following tables list the members exposed by [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the hatch angle. |
| Property | Color | Gets or sets the sketch hatch line color. |
| Property | Layer | Gets or sets the layer used by this sketch hatch. |
| Property | LayerOverride | Gets or sets whether the sketch hatch has properties that override the default properties of the layer. |
| Property | Pattern | Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the sldwks.ptn file. |
| Property | PatternId | Gets the pattern ID for this sketch hatch. |
| Property | Scale | Obsolete. Superseded by ISketchHatch::Scale2 . |
| Property | Scale2 | Gets or sets the hatch pattern scale. |
| Property | SolidFill | Gets or sets whether to enable solid fill for the sketch hatch. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | DeSelect | Deselects the sketch hatch. |
| Method | GetFace | Gets the face associated with this sketch hatch. |
| Method | GetID | Gets the ID for this sketch hatch. |
| Method | GetSketch | Gets the sketch for the current sketch hatch. |
| Method | IGetFace | Obsolete. Superseded by ISketchHatch::IGetFace2 . |
| Method | IGetFace2 | Gets the face associated with this sketch hatch. |
| Method | IGetID | Gets the ID for this sketch hatch. |
| Method | Select | Obsolete. Superseded by ISketchHatch::Select4 . |
| Method | Select2 | Obsolete. Superseded by ISketchHatch::Select4 . |
| Method | Select3 | Obsolete. Superseded by ISketchHatch::Select4 . |
| Method | Select4 | Selects the sketch hatch and marks it. |
| Method | SelectByMark | Obsolete. Superseded by ISketchHatch::Select4 . |

[Top](#topBookmark)

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.html)
