---
title: "IBreakCornerFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html"
---

# IBreakCornerFeatureData Interface Members

The following tables list the members exposed by [IBreakCornerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BreakType | Gets or sets the break corner type. |
| Property | CenteredOnBendLines | Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature. |
| Property | Distance | Gets or sets the chamfer length or fillet radius, depending on the break corner type. |
| Property | Entities | Gets or sets the faces or edges to which this break corner is applied. |
| Property | InternalCornersOnly | Gets or sets whether to add or subtract material from break corner/corner trim features. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this break corner feature. |
| Method | GetEntitiesCount | Gets the number of faces or edges associated with this break corner feature. |
| Method | IAccessSelections | Gains access to the selections that describe this break corner feature. |
| Method | IGetEntities | Gets the faces or edges to which this break corner is applied. |
| Method | ISetEntities | Sets the faces or edges to which this break corner is applied. |
| Method | ReleaseSelectionAccess | Releases access to selections for this break corner feature. |

[Top](#topBookmark)

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSheetMetalCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalCornerTrim.html)
[IModelDoc2::InsertSheetMetalBreakCorner Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBreakCorner.html)
