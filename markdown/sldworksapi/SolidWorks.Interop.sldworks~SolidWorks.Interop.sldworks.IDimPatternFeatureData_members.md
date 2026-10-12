---
title: "IDimPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html"
---

# IDimPatternFeatureData Interface Members

The following tables list the members exposed by [IDimPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | PropagateVisualProperties | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Allows access to the selections that describe this variable pattern feature. |
| Method | AddDimension | Adds the selected dimension as a column to the pattern table for this variable pattern feature. |
| Method | AddInstanceAt | Adds a pattern instance to this variable pattern feature. |
| Method | DeleteDimension | Deletes the specified column of dimensions in the pattern table in this variable pattern feature. |
| Method | DeleteInstanceAt | Deletes the specified pattern instance in this variable pattern feature. |
| Method | ExportToExcel | Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature. |
| Method | GetControllingDimensionCount | Gets the number of controlling dimensions in this variable pattern feature. |
| Method | GetControllingDimensionName | Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature. |
| Method | GetInstanceCount | Gets the number of pattern instances in this variable pattern feature. |
| Method | GetInstanceDimensionName | Gets the name of the pattern dimension for the pattern instance in this variable pattern feature. |
| Method | GetInstanceIndex | Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature. |
| Method | GetInstanceNameByIndex | Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature. |
| Method | GetInstanceSuppressStateByIndex | Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature. |
| Method | GetInstanceSuppressStateByName | Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature. |
| Method | GetTableRowIndex | Gets the index of the specified pattern instance in the pattern table in this variable pattern feature. |
| Method | ImportFromExcel | Imports a table from the specified Microsoft Excel file for this variable pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define this variable pattern feature. |
| Method | SetInstanceDimensionValue | Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature. |
| Method | SetInstanceSuppressStateByIndex | Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature. |
| Method | SetInstanceSuppressStateByName | Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature. |

[Top](#topBookmark)

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureAdvancedTableDrivenPattern Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.html)
