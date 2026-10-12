---
title: "ISurfaceKnitFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html"
---

# ISurfaceKnitFeatureData Interface Members

The following tables list the members exposed by [ISurfaceKnitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Entities | Gets or sets the knitted faces and surfaces. |
| Property | KnitTolerance | Gets or sets the knit tolerance for this Surface-Knit feature. |
| Property | MaxValueForGapRange | Gets or sets the maximum gap range for this Surface-Knit feature. |
| Property | MinValueForGapRange | Gets or sets the minimum gap range for this Surface-Knit feature. |
| Property | SeedFace | Gets or sets the seed face for this surface knit feature. |
| Property | UseGapFilters | Gets or sets whether to use gap filters for this Surface-Knit feature. |
| Property | UseMergeEntities | Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature. |
| Property | UseTryToFormSolid | Gets or sets whether to try to form a solid body when creating the Surface-Knit feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections that define this Surface-Knit feature. |
| Method | GetEntitiesCount | Gets the number of knit faces and surfaces for this Surface-Knit feature. |
| Method | IAccessSelections | Accesses the selections that define this Surface-Knit feature. |
| Method | IGetEntities | Gets the knitted faces and surfaces for this Surface-Knit feature. |
| Method | ISetEntities | Sets the faces and surfaces to knit. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this Surface-Knit feature. |

[Top](#topBookmark)

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSewRefSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSewRefSurface.html)
