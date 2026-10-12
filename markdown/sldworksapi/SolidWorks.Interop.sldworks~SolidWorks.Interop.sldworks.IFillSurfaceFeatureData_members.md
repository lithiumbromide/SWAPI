---
title: "IFillSurfaceFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html"
---

# IFillSurfaceFeatureData Interface Members

The following tables list the members exposed by [IFillSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Merge | Gets or sets whether or not to merge results. |
| Property | OptimizeSurface | Gets or sets whether or not to optimize the patch. |
| Property | ResolutionControl | Gets and sets the quality of the resolution of the fill-surface feature. |
| Property | ReverseDirection | Gets or sets whether or not to reverse direction while merging results. |
| Property | ReverseSurface | Gets or sets direction of the surface patch. |
| Property | TryToFormSolid | Gets or sets whether to form a solid. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this fill-surface feature. |
| Method | GetAlternateFace | Gets an alternate face to use as the boundary face for the curvature control of the patch. |
| Method | GetConstraintCurves | Gets the constraint curves for this fill-surface feature. |
| Method | GetConstraintCurvesCount | Gets the number of entities used to create the constraint curves for this fill-surface feature. |
| Method | GetCurvatureControl | Gets the contact type for the input boundary. |
| Method | GetPatchBoundary | Gets the entities used to define the patch boundary for this fill-surface feature. |
| Method | GetPatchBoundaryCount | Gets the number of entities used to define the patch boundary for this fill-surface feature. |
| Method | IAccessSelections | Gains access to the selections that define this fill-surface feature. |
| Method | IGetConstraintCurves | Gets the constraint curves for this fill-surface feature. |
| Method | IGetPatchBoundary | Gets the entities used to define the patch boundary for this fill-surface feature. |
| Method | ISetConstraintCurves | Sets the entities for the constraint curves. |
| Method | ISetPatchBoundary | Sets the patch boundary for this fill-surface feature. |
| Method | ReleaseSelectionAccess | Releases access to selections that define this fill-surface feature. |
| Method | SetConstraintCurves | Sets the entities for the constraint curves. |
| Method | SetCurvatureControl | Sets the contact type for this fill-surface feature. |
| Method | SetPatchBoundary | Sets the patch boundary for this fill-surface feature. |
| Method | ToggleAlternateFace | Switches the boundary face of the curvature control of the patch. |

[Top](#topBookmark)

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertFillSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface2.html)
