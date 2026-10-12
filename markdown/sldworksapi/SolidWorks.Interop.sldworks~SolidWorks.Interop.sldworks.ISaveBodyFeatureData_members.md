---
title: "ISaveBodyFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html"
---

# ISaveBodyFeatureData Interface Members

The following tables list the members exposed by [ISaveBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AssemblyPath | Gets or sets the path and filename of the assembly (*. sldasm ) of save bodies. |
| Property | ConsumeBody | Gets or sets whether to consume all bodies in the original part. |
| Property | CopyCustomProperties | Gets or sets whether to copy custom properties to the new parts. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this Save Bodies feature. |
| Method | AddSaveBodies | Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk. |
| Method | GetSaveBodies | Gets the save bodies in this Save Bodies feature. |
| Method | GetSaveBodiesCount | Gets the number of save bodies in this Save Bodies feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this Save Bodies feature. |
| Method | RemoveSaveBodies | Removes the specified bodies from this Save Bodies feature. |

[Top](#topBookmark)

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::CreateSaveBodyFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateSaveBodyFeature.html)
