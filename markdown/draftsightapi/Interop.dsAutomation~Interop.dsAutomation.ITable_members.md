---
title: "ITable Interface Members"
project: ""
interface: "ITable_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable_members.html"
---

# ITable Interface Members

The following tables list the members exposed by [ITable](Interop.dsAutomation~Interop.dsAutomation.ITable.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Table. |
| Property | Direction | Gets or sets the header orientation of the table. |
| Property | Erased | Gets or sets whether to erase or restore the Table. |
| Property | Handle | Gets the value of the handle for the Table. |
| Property | Layer | Gets or sets the name of the Layer of the Table. |
| Property | LineScale | Gets or sets the scale factor for the Table's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Table. |
| Property | LineWeight | Gets or sets the LineWeight for the Table. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Table. |
| Property | TableStyle | Gets or sets the TableStyle for this Table. |
| Property | Transparency | Gets or sets the transparency object for this Table. |
| Property | Visible | Gets or sets whether to show this Table. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Table. |
| Method | DeleteColumn | Deletes the column at the specified index from the Table. |
| Method | DeleteCustomData | Deletes the specified custom data from the Table. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Table. |
| Method | DeleteRow | Deletes the specified row from the Table. |
| Method | GetAlignment | Gets the justification and alignment of the text in the specified type of cell in this Table. |
| Method | GetBackgroundColor | Gets the background color for the specified type of cell in this Table. |
| Method | GetBordersColor | Gets the color of the specified type of Line for the border of the specified type of cell in this Table. |
| Method | GetBordersLineWeight | Gets the LineWeight of the specified type of Line for the border of the specified type of cell in this Table. |
| Method | GetBordersVisibility | Sets the visibility of the specified type of Line for the border of the specified type of cell in this Table. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Table. |
| Method | GetCellAlignment | Gets the justification and alignment of the text in the specified cell in this Table. |
| Method | GetCellBackgroundColor | Gets the background Color of the specified cell in this Table. |
| Method | GetCellBordersColor | Gets the Color of the specified type of Line for the border for the specified cell in this Table. |
| Method | GetCellBordersLineWeight | Gets the LineWeight of the specified type of Line of the border for the specified cell in this Table. |
| Method | GetCellBordersVisibility | Gets the visibility of the specified type of Line for the border of the specified cell in this Table. |
| Method | GetCellHorizontalMargin | Gets the size of the horizontal margin of the specified cell in this Table. |
| Method | GetCellTextColor | Gets the Color of the text of the specified cell in this Table. |
| Method | GetCellTextHeight | Gets the height of the text of the specified cell in this Table. |
| Method | GetCellTextStyle | Gets the name of the TextStyle for the specified cell in this Table. |
| Method | GetCellType | Gets the type of the specified table cell, row, or column. |
| Method | GetCellVerticalMargin | Gets the size of the vertical margin for the specified cell in this Table. |
| Method | GetColumnWidth | Gets the width of the specified column in the Table. |
| Method | GetCustomData | Gets the specified custom data for the Table. |
| Method | GetExtensionDictionary | Gets the dictionary for the Table. |
| Method | GetHorizontalMargin | Gets the size of the horizontal margin of this Table. |
| Method | GetHyperLink | Gets the hyperlink attached to the Table. |
| Method | GetNormal | Gets the vector normal to this Table. |
| Method | GetPosition | Gets the point in the drawing where the Table was inserted. |
| Method | GetRowHeight | Gets the height of the specified row in this Table. |
| Method | GetSimplifiedText | Gets the raw text in the specified cell. |
| Method | GetText | Gets the formatted text in the specified cell. |
| Method | GetTextColor | Gets the Color of the text for the specified type of cell in this Table. |
| Method | GetTextHeight | Gets the height of the text of the specified type of cell in this Table. |
| Method | GetTextStyle | Gets the name of the TextStyle of the specified type of cell in this Table. |
| Method | GetVerticalMargin | Gets the size of the vertical margin of this Table. |
| Method | InsertColumn | Inserts a column of the specified width at the specified index in the Table. |
| Method | InsertRow | Inserts a row of the specified height at the specified index in the Table. |
| Method | MergeCells | Merges the specified rectangular region of cells in this Table. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Table, if the dictionary exists and is empty. |
| Method | SaveAsCSVFile | Saves the content of the Table as a .csv (comma-separated values) file. |
| Method | Select | Adds or removes the selected Table to or from the current selection set. |
| Method | SetAlignment | Sets the justification and alignment of the text in the specified type of cell in this Table. |
| Method | SetBackgroundColor | Sets the background Color of the specified type of cell in this Table. |
| Method | SetBordersColor | Sets the Color of the specified type of Line for the border of the specified type of cell in this Table. |
| Method | SetBordersLineWeight | Sets the LineWeight of the specified type of Line for the border of the specified type cell in this Table. |
| Method | SetBordersVisibility | Sets the visibility of the specified type of Line for the border of the specified type of cell in this Table. |
| Method | SetCellAlignment | Sets the justification and alignment of the text in the specified cell in this Table. |
| Method | SetCellBackgroundColor | Sets the background Color of the specified cell in this Table. |
| Method | SetCellBordersColor | Sets the Color of the specified type of Line for the border of the specified cell in this Table. |
| Method | SetCellBordersLineWeight | Sets the LineWeight of the specified type of Line for the border of the specified cell in this Table. |
| Method | SetCellBordersVisibility | Sets the visibility of the specified type of Line for the border of the specified cell in this Table. |
| Method | SetCellHorizontalMargin | Sets the size of the horizontal margin of the specified cell in this Table. |
| Method | SetCellTextColor | Sets the Color of the text for the specified cell in this Table. |
| Method | SetCellTextHeight | Sets the height of the text for the specified cell in this Table. |
| Method | SetCellTextStyle | Sets the name of the TextStyle for the specified cell in this Table. |
| Method | SetCellType | Sets the type for the specified table cell, row, or column. |
| Method | SetCellVerticalMargin | Sets the size of the vertical margin of the specified cell in this Table. |
| Method | SetColumnWidth | Sets the width of the columns in the Table. |
| Method | SetColumnWidthAt | Sets the width of the specified column in the Table. |
| Method | SetCustomData | Sets the custom data for the Table. |
| Method | SetHorizontalMargin | Sets the size of the horizontal margin for this Table. |
| Method | SetHyperLink | Attaches a hyperlink to the Table. |
| Method | SetNormal | Sets the vector normal to the Table. |
| Method | SetPosition | Sets the point in the drawing where to insert the Table. |
| Method | SetRowHeight | Sets the height of the rows in the Table. |
| Method | SetRowHeightAt | Sets the height of the specified row in the Table. |
| Method | SetText | Sets the text of the specified cell. |
| Method | SetTextColor | Sets the Color of the text for the specified type of cell in this Table. |
| Method | SetTextHeight | Sets the height of the specified type of cell in this Table. |
| Method | SetTextStyle | Sets the name of the TextStyle for the specified type of cell in this Table. |
| Method | SetVerticalMargin | Sets the size of the vertical margin for this Table. |
| Method | TotalColumnCount | Gets the total number of columns in the Table. |
| Method | TotalRowCount | Gets the total number of rows in the Table. |
| Method | UnmergeCells | Unmerges a previously merged rectangular region of cells in this Table. |

[Top](#topBookmark)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager.html)
