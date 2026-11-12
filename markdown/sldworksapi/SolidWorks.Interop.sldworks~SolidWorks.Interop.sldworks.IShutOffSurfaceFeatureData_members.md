---
title: "IShutOffSurfaceFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html"
---

# IShutOffSurfaceFeatureData Interface Members

The following tables list the members exposed by [IShutOffSurfaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Edges | Gets or sets the edges that form closed loops for the patches. |
| Property | Knit | Gets or sets whether to knit the patches in this shut-off surface feature. |
| Property | LoopEdges | Gets the edges in the specified loop in this shut-off surface feature. |
| Property | LoopPatchType | Gets and sets the type of patch for the specified loop for this shut-off surface feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this shut-off surface feature. |
| Method | FlipFaceTangentTo | Indicates to create the patch on the opposite tangent face. |
| Method | GetEdgeCount | Gets the number of edges that form a closed loop. |
| Method | GetFaceTangentTo | Gets the tangent face for the specified loop where to create the patch. |
| Method | GetLoopCount | Gets the number of closed loops for all of the patches. |
| Method | GetLoopEdgeCount | Gets the number of edges in the specified loop. |
| Method | IGetEdges | Gets the edges that form closed loops to use for the patches. |
| Method | IGetLoopEdges | Gets the edges in the specified loop. |
| Method | ISetEdges | Sets the edges to use to form closed loops for patches. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this shut-off surface feature. |
| Method | SetAllPatchTypes | Sets the type of patch for all loops for this shut-off surface feature. |
| Method | Status | Gets the status of the shut-off surface feature. |

[Top](#topBookmark)

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.html)
