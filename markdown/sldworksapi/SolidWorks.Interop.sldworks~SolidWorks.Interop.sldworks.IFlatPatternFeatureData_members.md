---
title: "IFlatPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html"
---

# IFlatPatternFeatureData Interface Members

The following tables list the members exposed by [IFlatPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BreakCornerRadius | Gets or sets the radius of the break corner for the Flat-Pattern feature. |
| Property | BreakCornerType | Gets or sets the type of break corner for the Flat-Pattern feature. |
| Property | CornerTreatment | Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature. |
| Property | CornerTrimRatioToThickness | Gets or sets the ratio of the relief thickness of the corner trim for the Flat-Pattern feature. |
| Property | CornerTrimReliefDistance | Gets or sets the distance of the relief for the corner trim for the Flat-Pattern feature. |
| Property | CornerTrimReliefType | Gets or sets the type of relief for the corner trim for the Flat-Pattern feature. |
| Property | ExcludedFaces | Gets and sets the faces to exclude from this Flat-Pattern feature. |
| Property | FixedFace | Obsolete. Superseded by IFlatPatternFeatureData::FixedFace2 . |
| Property | FixedFace2 | Gets or sets the fixed face of this Flat-Pattern feature. |
| Property | MergeFace | Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature. |
| Property | ShowSlitInCornerRelief | Get or set whether to show the slit in the corner relief of this Flat-Pattern feature. |
| Property | SimplifyBends | Gets or sets whether to simplify bends in this Flat-Pattern feature. |
| Property | UseRatioToThickness | Gets or sets whether to use the ratio to thickness setting for the corner trim for the Flat-Pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this Flat-Pattern feature. |
| Method | GetAddCornerTrim | Gets whether to add a corner trim to the Flat-Pattern feature. |
| Method | GetBreakCorners | Gets whether to add break corners to the Flat-Pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by IFlatPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that describe this Flat-Pattern feature. |
| Method | IGetExcludedFaces | Gets the faces that are excluded from this Flat-Pattern feature. |
| Method | IGetExcludedFacesCount | Gets the number of faces that are excluded from this Flat-Pattern feature. |
| Method | ISetExcludedFaces | Sets the faces to exclude from this Flat-Pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this Flat-Pattern feature. |
| Method | SetAddCornerTrim | Sets whether to add corner trims to the Flat-Pattern feature. |
| Method | SetBreakCorners | Sets whether to add break corners to the Flat-Pattern feature. |

[Top](#topBookmark)

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[IFeatureManager::FinishCornerRelief Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishCornerRelief.html)
