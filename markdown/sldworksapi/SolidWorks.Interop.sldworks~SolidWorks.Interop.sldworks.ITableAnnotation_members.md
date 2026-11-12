---
title: "ITableAnnotation Interface Members"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html"
---

# ITableAnnotation Interface Members

The following tables list the members exposed by [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Anchored | Gets or sets whether this table is attached to its anchor. |
| Property | AnchorType | Gets or sets the anchor point for this table annotation. |
| Property | BorderLineWeight | Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table. |
| Property | BorderLineWeightCustom | Gets or sets the line weight of the border lines to the specified custom weight for this table. |
| Property | CellTextHorizontalJustification | Gets or sets the horizontal justification for the text in the specified cell. |
| Property | CellTextVerticalJustification | Gets or sets the vertical justification for the text in the specified cell. |
| Property | ColumnCount | Gets the number of columns in this table. |
| Property | ColumnHidden | Hides or shows the specified column in this table annotation. |
| Property | DisplayedText | Obsolete. Superseded by ITableAnnotation::DisplayedText2 . |
| Property | DisplayedText2 | Gets the actual text displayed in the specified cell in this table. |
| Property | GeneralTableFeature | Gets the general table feature for this general table annotation. |
| Property | GridLineWeight | Gets or sets the line weight of the inner lines to the SOLIDWORKS-supplied weight for this table. |
| Property | GridLineWeightCustom | Gets or sets the line weight of the inner lines to the specified custom weight for this table. |
| Property | RowCount | Gets the number of rows in this table. |
| Property | RowHidden | Gets or sets whether the specified row is hidden in this table. |
| Property | StopAutoSplitting | Stops the automatic horizontal splitting of this table. |
| Property | Text | Obsolete. Superseded by ITableAnnotation::Text2 . |
| Property | Text2 | Gets or sets the parametrized string of text for the specified cell of this table. |
| Property | TextHorizontalJustification | Gets or sets the horizontal justification setting for the text in this table. |
| Property | TextVerticalJustification | Gets or sets the vertical justification for the text in this table. |
| Property | Title | Gets or sets the title for this table. |
| Property | TitleVisible | Gets or sets whether the title of the table is visible. |
| Property | TotalColumnCount | Gets the total number of visible and hidden columns in this table. |
| Property | TotalRowCount | Gets the total number of visible and hidden rows in this table. |
| Property | Type | Gets the type of table. |
| Property | UpperCase | Gets or sets whether text in the table is all upper case. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | DeleteColumn | Obsolete. Superseded by ITableAnnotation::DeleteColumn2 . |
| Method | DeleteColumn2 | Deletes the specified column in this table. |
| Method | DeleteRow | Obsolete. Superseded by ITableAnnotation::DeleteRow2 . |
| Method | DeleteRow2 | Deletes the specified row from this table. |
| Method | EvaluateCellEquation | Solves the specified equation in the specified cell of this BOM table. |
| Method | GetAnnotation | Gets the annotation for this table annotation. |
| Method | GetCellEquation | Gets the equation and its solved value for the specified row and column of this BOM table. |
| Method | GetCellRange | Gets the selected table cells' row and column index ranges. |
| Method | GetCellTextFormat | Gets the text format for the specified cell in this table. |
| Method | GetCellTextOrientation | Gets the text orientation in the specified cell of this table. |
| Method | GetCellUseDocTextFormat | Gets whether this cell uses the document setting for its text format. |
| Method | GetColumnTitle | Obsolete. Superseded by ITableAnnotation::GetColumnTitle2 . |
| Method | GetColumnTitle2 | Gets the title of the specified column. |
| Method | GetColumnType | Obsolete. Superseded by ITableAnnotation::GetColumnType2 . |
| Method | GetColumnType2 | Obsolete. Superseded by ITableAnnotation::GetColumnType3 . |
| Method | GetColumnType3 | Gets the type and property data for the specified BOM table column. |
| Method | GetColumnWidth | Gets the width of the specified column of this table annotation. |
| Method | GetHeaderCount | Gets the number of rows or columns in the header of this table. |
| Method | GetHeaderStyle | Gets the header style of this table. |
| Method | GetLockColumnWidth | Gets whether the width of the specified column is locked in this table annotation. |
| Method | GetLockRowHeight | Gets whether the height of the specified row is locked in this table annotation. |
| Method | GetNext | Gets the next table annotation in this drawing view. |
| Method | GetRowHeight | Gets the height of the specified row of this table. |
| Method | GetRowVerticalGap | Gets the gap between the text and the top or bottom of the specified row of this table. |
| Method | GetSplitInformation | Gets information about any splits in this table. |
| Method | GetTextFormat | Gets the text format for this table. |
| Method | GetUseDocTextFormat | Gets whether this table uses the document setting for text formatting. |
| Method | HorizontalAutoSplit | Starts the automatic horizontal splitting of this table using the specified options. |
| Method | InsertColumn | Obsolete. Superseded by ITableAnnnotation::InsertColumn2 . |
| Method | InsertColumn2 | Inserts a column into this table. |
| Method | InsertRow | Inserts a row into this table. |
| Method | IsCellMerged | Gets whether the specified cell is merged with other cells. |
| Method | IsCellTextEditable | Gets whether the text in this cell can be edited. |
| Method | Merge | Merges the display of this table. |
| Method | MergeCells | Merges the cells in the specified range. |
| Method | MoveColumn | Moves a column in this table annotation. |
| Method | MoveRow | Moves a row in this table either up one row or down one row. |
| Method | SaveAsPDF | Saves this table to a PDF file. |
| Method | SaveAsTemplate | Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same. |
| Method | SaveAsText | Obsolete. Superseded by ITableAnnotation::SaveAsText2 . |
| Method | SaveAsText2 | Saves this table to a text data file. |
| Method | SetCellEquation | Sets the specified equation for the specified row and column of this BOM table. |
| Method | SetCellRange | Sets the current range of cells. |
| Method | SetCellTextFormat | Sets the text format for the text in the specified cell. |
| Method | SetCellTextOrientation | Sets the text orientation in the specified table cell. |
| Method | SetColumnTitle | Obsolete. Superseded by ITableAnnotation::SetColumnTitle2 . |
| Method | SetColumnTitle2 | Sets the title of the specified column. |
| Method | SetColumnType | Obsolete. Superseded by ITableAnnotation::SetColumnType2 . |
| Method | SetColumnType2 | Obsolete. Superseded by ITableAnnotation::SetColumnType3 . |
| Method | SetColumnType3 | Sets the type and property data for the specified BOM table column. |
| Method | SetColumnWidth | Sets the width of the specified column in this table. |
| Method | SetHeader | Sets the header for this table. |
| Method | SetLockColumnWidth | Sets whether to lock the width of the specified column in this table annotation. |
| Method | SetLockRowHeight | Sets whether to lock the height of the specified row in this table annotation. |
| Method | SetRowHeight | Sets the height of the specified row in this table. |
| Method | SetRowVerticalGap | Sets the gap between the text and the top or bottom of the specified row of this table. |
| Method | SetTextFormat | Sets the text format for this table. |
| Method | Split | Splits the table at the specified location. |
| Method | UnmergeCells | Splits the specified previously merged cell in this table. |

[Top](#topBookmark)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
