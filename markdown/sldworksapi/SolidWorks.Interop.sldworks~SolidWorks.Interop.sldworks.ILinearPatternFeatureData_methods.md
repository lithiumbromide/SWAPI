---
title: "ILinearPatternFeatureData Interface Methods"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_methods.html"
---

# ILinearPatternFeatureData Interface Methods

For a list of all members of this type, see [ILinearPatternFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the linear pattern feature. |
| Method | GetD1AxisType | Gets the type of geometry used to determine Direction 1 of this linear pattern feature. |
| Method | GetD2AxisType | Gets the type of geometry used to determine Direction 2 of this linear pattern feature. |
| Method | GetInstanceToVaryOptions | Gets the options for varying the spacing of pattern instances in this linear pattern feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in this linear pattern feature. |
| Method | GetPatternFaceCount | Gets the number of seed faces in this linear pattern feature. |
| Method | GetPatternFeatureCount | Gets the number of seed features in this linear pattern feature. |
| Method | GetSkippedItemCount | Gets the number of instances skipped in this linear pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this linear pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ILinearPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections used to define the linear pattern feature. |
| Method | IGetPatternBodyArray | Gets the seed bodies for this linear pattern feature. |
| Method | IGetPatternFaceArray | Gets the seed faces in this linear pattern feature. |
| Method | IGetPatternFeatureArray | Gets the seed features used to create this linear pattern feature. |
| Method | IGetSkippedItemArray | Gets the items skipped in this linear pattern feature. |
| Method | IsDirection2Specified | Gets whether direction 2 is specified for this linear pattern feature. |
| Method | ISetPatternBodyArray | Sets the seed bodies for this linear pattern feature. |
| Method | ISetPatternFaceArray | Sets the list of patterned faces for this linear pattern feature. |
| Method | ISetPatternFeatureArray | Sets a list of pattern features for this linear pattern feature. |
| Method | ISetSkippedItemArray | Sets the list of items skipped for this linear pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this linear pattern. |
| Method | SetFeatureScope | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this linear pattern feature. |
| Method | SetInstanceToVaryOptions | Sets the options for varying the spacing of pattern instances in this circular pattern feature. |

[Top](#topBookmark)

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
