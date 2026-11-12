---
title: "ICenterMark Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICenterMark_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html"
---

# ICenterMark Interface Members

The following tables list the members exposed by [ICenterMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CenterLineFont | Gets or sets whether the centerline font is used for the lines in this center mark. |
| Property | ConnectionLines | Gets or sets the visibility of the connection line of this center mark. |
| Property | Gap | Gets or sets the gap between this center mark and extension line. |
| Property | GroupCount | Gets the number of center marks in a center mark set. |
| Property | IsGrouped | Gets whether a center mark is in a center mark set. |
| Property | RotationAngle | Gets or sets the angle for this center mark. |
| Property | ShowLines | Gets or sets whether the extension lines are shown in this center mark. |
| Property | Size | Gets or sets the length of the lines in this center mark. |
| Property | Style | Gets the style of this center mark. |
| Property | UseDocDisplaySettings | Gets or sets whether to use the document defaults for this center mark's display settings. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddToCenterMarkGroup | Adds a center mark for the selected entity in an existing center mark set. |
| Method | GetAnnotation | Gets the annotation for this center mark. |
| Method | GetExtendedLength | Gets the extended length of the specified arm (handle) of this center mark. |
| Method | GetNext | Gets the next center mark. |
| Method | GetPosition | Gets the x, y, and z coordinates for the specified center mark. |
| Method | HasDetachCenterMark | Gets whether the selected center mark set contains any detached center marks. |
| Method | IsDeleted | Gets whether the specified center mark is deleted in this center mark set. |
| Method | IsDetached | Gets whether the specified center mark is detached. |
| Method | ReattachToCenterMarkGroup | Reattaches the specified center mark to the selected entity in a center mark set. |
| Method | Select | Selects the center mark. |
| Method | SetExtendedLength | Sets the extended length of this center mark. |

[Top](#topBookmark)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.html)
