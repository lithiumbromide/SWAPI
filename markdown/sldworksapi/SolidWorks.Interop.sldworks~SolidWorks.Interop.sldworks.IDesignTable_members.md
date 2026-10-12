---
title: "IDesignTable Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDesignTable_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html"
---

# IDesignTable Interface Members

The following tables list the members exposed by [IDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoAddNewConfigs | Gets or sets whether to automatically add rows or columns to the design table when new configurations are added to the model. |
| Property | AutoAddNewParams | Gets or sets whether or not to automatically add rows or columns to the design table when new parameters are added to the model. |
| Property | ColumnHidden | Gets the visibility state of the specified column. |
| Property | EnableCellDropdownLists | Gets or sets whether to enable cell drop-down lists in the design table. |
| Property | FileName | Gets or sets the Microsoft Excel file for this design table. |
| Property | LastError | Gets or sets the last error that occurred in this design table. |
| Property | LinkToFile | Gets or sets whether to link the design table to the model. |
| Property | RowHidden | Gets the visibility state of the specified row. |
| Property | SourceType | Gets or sets the type of source file for this design table. |
| Property | Updatable | Gets or sets whether edits to the model update the design table. |
| Property | Warn | Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table. |
| Property | Worksheet | Gets the Microsoft Excel worksheet for this design table. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddRow | Adds a row to the design table. |
| Method | Attach | Activates the design table within the part or assembly document. |
| Method | Detach | Detaches the design table from the Microsoft Excel sheet. |
| Method | EditFeature | Lets you change the characteristics of the design table. |
| Method | EditTable | Obsolete. Superseded by IDesignTable::EditTable2 . |
| Method | EditTable2 | Lets you edit the design table. |
| Method | GetColumnCount | Gets the number of columns in the design table that are currently visible in the model view. |
| Method | GetEntryText | Gets the contents of the specified cell as a string regardless of the cell's data type. |
| Method | GetEntryValue | Gets the contents of the specified cell. |
| Method | GetHeaderText | Gets the header text for the specified column. |
| Method | GetRowCount | Gets the number of rows in the design table that are currently visible in the model view. |
| Method | GetStartColumnNumber | Gets the number of the first column in which a dimension is displayed. |
| Method | GetStartRowNumber | Gets the number of the first row in which dimensions are displayed. |
| Method | GetTitle | Gets the design table title. |
| Method | GetTotalColumnCount | Gets the number of columns in the design table. |
| Method | GetTotalRowCount | Gets the number of rows in the design table. |
| Method | GetVisibleColumnCount | Gets the number of columns visible in this design table. |
| Method | GetVisibleLeftColumnNumber | Gets the number of the leftmost visible column. |
| Method | GetVisibleRowCount | Gets the number of rows visible in the design table. |
| Method | GetVisibleTopRowNumber | Gets the number of the topmost visible row. |
| Method | IsActive | Gets whether the design table is currently being edited. |
| Method | SaveAsExcelFile | Saves the design table to a Microsoft Excel file. |
| Method | SetEntryText | Sets the text value of the specified entry. |
| Method | SetEntryValue | Sets the data type and value in the specified cell. |
| Method | SetRowChanged | Sets the number of the row that was changed. |
| Method | UpdateFeature | Updates the characteristics of the design table. |
| Method | UpdateModel | Applies the edits to the design table to the model. |
| Method | UpdateTable | Applies the changes made to the design table to the model. |

[Top](#topBookmark)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
