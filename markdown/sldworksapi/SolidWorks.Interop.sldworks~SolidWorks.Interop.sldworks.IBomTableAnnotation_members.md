---
title: "IBomTableAnnotation Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html"
---

# IBomTableAnnotation Interface Members

The following tables list the members exposed by [IBomTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BomFeature | Gets the BOM for this table annotation. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ApplySavedSortScheme | Sorts this BOM table using the sort data that was previously saved in the table. |
| Method | Collapse | Collapses the specified item. |
| Method | Dissolve | Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation. |
| Method | Expand | Expands the specified item. |
| Method | GetAllCustomProperties | Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | GetAllCustomPropertiesCount | Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | GetBomTableSortData | Gets an instance of IBomTableSortData . |
| Method | GetColumnCustomProperty | Gets the custom property used to fill the values in a specified user-defined column. |
| Method | GetColumnUseTitleAsPartNumber | Gets whether the document title is being used for the specified part-number column. |
| Method | GetComponents | Obsolete. Superseded by IBomTableAnnotation::GetComponents2 . |
| Method | GetComponents2 | Gets the components in the specified row for the specified configuration in this BOM table annotation. |
| Method | GetComponentsCount | Obsolete. Superseded by IBomTableAnnotation::GetComponentsCount2 . |
| Method | GetComponentsCount2 | Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation. |
| Method | GetModelPathNames | Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row. |
| Method | GetModelPathNamesCount | Gets the number of model pathnames in the specified row of this BOM table annotation. |
| Method | IGetAllCustomProperties | Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation. |
| Method | IGetComponents | Obsolete. Superseded by IBomTableAnnotation::IGetComponents2 . |
| Method | IGetComponents2 | Gets the components in the specified row for the specified configuration in this BOM table annotation. |
| Method | IGetModelPathNames | Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row. |
| Method | RestoreRestructuredComponents | Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation. |
| Method | SaveAsExcel | Saves this BOM table annotation as a Microsoft Excel document with the specified properties. |
| Method | SetColumnCustomProperty | Sets the custom property used to fill the values in a specified user-defined column. |
| Method | SetColumnUseTitleAsPartNumber | Sets whether to use the document title for the specified part-number column. |
| Method | Sort | Sorts this BOM table using the specified sorting data. |

[Top](#topBookmark)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
