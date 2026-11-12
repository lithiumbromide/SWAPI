---
title: "IPartingSurfaceFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html"
---

# IPartingSurfaceFeatureData Interface Members

The following tables list the members exposed by [IPartingSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Knit | Gets or sets whether to knit all surfaces. |
| Property | OffsetAngle | Gets or sets the angle for this parting surface feature. |
| Property | OffsetDistance | Gets or sets the distance that this parting surface feature extends. |
| Property | PartingLines | Gets or sets the entities for the parting lines for this parting surface feature. |
| Property | PartingType | Gets or sets the type of parting surface. |
| Property | PullDirectionBase | Gets or sets the entity that defines the direction of pull for this parting surface feature. |
| Property | PullDirectionType | Gets the type of entity that specifies the direction of pull for this parting surface feature. |
| Property | ReverseAlignment | Gets or sets whether to reverse alignment of this parting surface feature. |
| Property | ReverseOffsetDirection | Gets or sets whether to reverse the direction of this parting surface feature. |
| Property | TransitionDistance | Gets or sets the distance to set between adjacent edges for this parting surface feature. |
| Property | TransitionType | Gets or sets the type of transition between adjacent edges for this parting surface feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this parting surface feature. |
| Method | GetPartingLinesCount | Gets the number of parting lines for this parting surface feature. |
| Method | GetPartingLinesType | Gets the type of entity to use for parting lines for this parting surface feature. |
| Method | IGetPartingLines | Gets the parting lines for this parting surface feature. |
| Method | ISetPartingLines | Sets the parting lines for this parting surface feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this parting surface feature. |

[Top](#topBookmark)

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMoldPartingSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface.html)
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
