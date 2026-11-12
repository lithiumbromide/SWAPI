---
title: "ISketchLine Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchLine_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html"
---

# ISketchLine Interface Members

The following tables list the members exposed by [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the angle of the line. |
| Property | Infinite | Gets whether the line is infinite or finite. NOTE: This property is a get-only property. Set is not implemented . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetBendLineDirection | Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline. |
| Method | GetEndPoint | Obsolete. Superseded by ISketchLine::GetEndPoint2 and ISketchLine::IGetEndPoint2 . |
| Method | GetEndPoint2 | Gets the sketch point for the end point of the line. |
| Method | GetStartPoint | Obsolete. Superseded by ISketchLine::GetStartPoint2 and ISketchLine::IGetStartPoint2 . |
| Method | GetStartPoint2 | Gets the sketch point for the start point of the line. |
| Method | IGetEndPoint | Obsolete. Superseded by ISketchLine::GetEndPoint2 and ISketchLine::IGetEndPoint2 . |
| Method | IGetEndPoint2 | Gets the sketch point for the end point of the line. |
| Method | IGetStartPoint | Obsolete. Superseded by ISketchLine::GetStartPoint2 and ISketchLine::IGetStartPoint2 . |
| Method | IGetStartPoint2 | Gets the sketch point for the start point of the line. |
| Method | MakeInfinite | Makes a line infinite. |

[Top](#topBookmark)

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
