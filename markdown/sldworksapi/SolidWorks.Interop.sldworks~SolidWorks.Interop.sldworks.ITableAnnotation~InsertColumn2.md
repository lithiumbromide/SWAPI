---
title: "InsertColumn2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "InsertColumn2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.html"
---

# InsertColumn2 Method (ITableAnnotation)

Inserts a column into this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertColumn2( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer, _
   ByVal Name As System.String, _
   ByVal WidthStyle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim Name As System.String
Dim WidthStyle As System.Integer
Dim value As System.Boolean

value = instance.InsertColumn2(Where, Index, Name, WidthStyle)
```

### C#

```csharp
System.bool InsertColumn2(
   System.int Where,
   System.int Index,
   System.string Name,
   System.int WidthStyle
)
```

### C++/CLI

```cpp
System.bool InsertColumn2(
   System.int Where,
   System.int Index,
   System.String^ Name,
   System.int WidthStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Where`: Where to insert the column as specified in [swTableItemInsertPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableItemInsertPosition_e.html)
- `Index`: Index of the column where to insert the new column
- `Name`: Column name
- `WidthStyle`: Style of the width of the column as defined in [swInsertTableColumnWidthStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertTableColumnWidthStyle_e.html)

### Return Value

True if column is inserted successfully, false if not

## VBA Syntax

See [TableAnnotation::InsertColumn2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~InsertColumn2.html).

## Examples

[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)

## Remarks

Index:

- is 0-based.
- is valid only if Where is set to swTableItemInsertPosition_e.swTableItemInsertPosition_After or swTableItemInsertPosition_e.swTableItemInsertPosition_Before.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::SetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
