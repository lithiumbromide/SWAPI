---
title: "ILocalSketchPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html"
---

# ILocalSketchPatternFeatureData Interface Members

The following tables list the members exposed by [ILocalSketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local sketch pattern feature. |
| Property | PatternComponentArray | Gets or sets the components to pattern for this sketch-driven component pattern feature. |
| Property | ReferencePoint | Gets or sets the type of reference point for this sketch-driven component pattern feature. |
| Property | SelectedPoint | Gets or sets the selected point for this sketch-driven component pattern feature. |
| Property | Sketch | Gets or sets the sketch for this sketch-driven component pattern feature. |
| Property | SkippedItemArray | Gets or sets the array of skipped components in this sketch-driven component pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define this sketch-driven component pattern feature. |
| Method | GetBasePoint | Gets the data for the base point from which this sketch-driven component pattern feature is created. |
| Method | GetPatternComponentCount | Gets the number of components in this sketch-driven component pattern feature. |
| Method | GetReferencePointType | Gets the type of reference point of this sketch-driven component pattern feature. |
| Method | GetSkippedItemCount | Gets the number of components skipped in this sketch-driven component pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance in this sketch-driven component pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this sketch-driven component pattern feature. |

[Top](#topBookmark)

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
