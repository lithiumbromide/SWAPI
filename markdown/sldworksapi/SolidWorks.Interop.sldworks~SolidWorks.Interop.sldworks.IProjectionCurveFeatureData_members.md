---
title: "IProjectionCurveFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html"
---

# IProjectionCurveFeatureData Interface Members

The following tables list the members exposed by [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Bidirectional | Gets or sets whether the sketch is projected bidirectionally. |
| Property | FaceArray | Gets or sets the target faces for this projected curve. |
| Property | Reverse | Reverses the direction that the curve is projected. |
| Property | Sketch | Gets or sets the sketch to project in this projection curve feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define the projected curve. |
| Method | GetFaceArrayCount | Gets the number of target faces for this projected curve. |
| Method | IAccessSelections | Obsolete. Superseded by IProjectionCurveFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections used to define the projected curve. |
| Method | IGetFaceArray | Gets a list of target faces for the projected curve. |
| Method | ISetFaceArray | Sets the target faces for the projected curve. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this projected curve. |

[Top](#topBookmark)

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
