---
title: "ColumnCount Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "ColumnCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html"
---

# ColumnCount Property (ITableAnnotation)

Gets the number of columns in this table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ColumnCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.ColumnCount
```

### C#

```csharp
System.int ColumnCount {get;}
```

### C++/CLI

```cpp
property System.int ColumnCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of columns in this table

## VBA Syntax

See [TableAnnotation::ColumnCount](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~ColumnCount.html).

## Examples

[Get Custom Properties for Bom Table Columns (VBA)](Get_Custom_Properties_for_BOM_Table_Columns_Example_VB.htm)
[Get Revision Table (VBA)](Get_Revision_Table_Example_VB.htm)
[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)
[Insert Table (VBA)](Insert_Table_Example_VB.htm)
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::SetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
