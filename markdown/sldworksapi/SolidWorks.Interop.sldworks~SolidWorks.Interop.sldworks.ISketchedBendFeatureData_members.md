---
title: "ISketchedBendFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html"
---

# ISketchedBendFeatureData Interface Members

The following tables list the members exposed by [ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendAngle | Gets or sets the bend angle of this sketched bend. |
| Property | BendRadius | Gets or sets the bend radius of this sketched bend. |
| Property | OverrideValue | Gets whether the bend angle of this sketched bend is overridden by a custom bend angle. |
| Property | PositionType | Gets or sets the bend position of this sketched bend. |
| Property | ReverseDirection | Gets or sets whether the direction of the sketched bend angle is reversed. |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance for this sketched bend. |
| Property | UseDefaultBendRadius | Gets or sets whether to use the default bend radius of this sketched bend. |
| Property | UseGaugeTable | Gets or sets whether to use available bend radius values from a gauge table for this sketched bend. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this sketched bend. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for this sketched bend. |
| Method | GetFixedFace | Gets the fixed face from this sketched bend. |
| Method | IAccessSelections | Obsolete. Superseded by ISketchedBendFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that describe this sketched bend feature. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this sketched bend. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for this sketched bend. |
| Method | SetFixedFace | Sets the fixed face of this sketched bend. |

[Top](#topBookmark)

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
