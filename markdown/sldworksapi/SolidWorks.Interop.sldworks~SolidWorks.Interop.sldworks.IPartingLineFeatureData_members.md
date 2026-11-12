---
title: "IPartingLineFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html"
---

# IPartingLineFeatureData Interface Members

The following tables list the members exposed by [IPartingLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the draft angle for the parting line. |
| Property | CoreCavitySplit | Gets or sets the core/cavity split option for a parting line. |
| Property | PartingLines | Gets and sets the edges for the parting lines. |
| Property | PullDirection | Gets whether the direction of pull is reversed. |
| Property | PullDirectionBase | Gets or sets the direction of pull for the parting line feature. |
| Property | PullDirectionType | Gets the type of entity indicating the direction of pull. |
| Property | SplitFaces | Gets or sets whether to split faces. |
| Property | SplitFacesOption | Gets or sets the split faces option for this parting line. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe the parting line feature. |
| Method | DraftAnalysis | Performs draft analysis for the input angle and the direction of pull. |
| Method | GetEntitiesToSplit | Gets the entities that are used to split a face. |
| Method | GetEntitiesToSplitCount | Gets the number of entities to use to split a face and add edges to the parting line feature. |
| Method | GetFacesByType | Gets the specified faces after performing a draft analysis of the parting line feature. |
| Method | GetFacesByTypeCount | Gets the number of faces of the specified type for this parting line. |
| Method | GetPartingLinesCount | Gets the number of edges used as parting lines. |
| Method | IGetEntitiesToSplit | Gets the entities that are used to split a face. |
| Method | IGetFacesByType | Gets the specified faces after performing a draft analysis of the parting line feature. |
| Method | IGetPartingLines | Gets the edges used as parting lines. |
| Method | ISetEntitiesToSplit | Sets the entities to use to split a face and add edges to the parting line feature. |
| Method | ISetPartingLines | Sets the edges to use as parting lines. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this parting line feature. |
| Method | SetEntitiesToSplit | Sets the entities to use to split a face and add edges to the parting line feature. |
| Method | Status | Gets the status of this parting line feature. |

[Top](#topBookmark)

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.html)
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
