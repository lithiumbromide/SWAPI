---
title: "TotalColumnCount Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "TotalColumnCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html"
---

# TotalColumnCount Property (ITableAnnotation)

Gets the total number of visible and hidden columns in this table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TotalColumnCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.TotalColumnCount
```

### C#

```csharp
System.int TotalColumnCount {get;}
```

### C++/CLI

```cpp
property System.int TotalColumnCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total number of visible and hidden columns in this table

## VBA Syntax

See [TableAnnotation::TotalColumnCount](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~TotalColumnCount.html).

## Examples

[Get the Total Number of Columns and Rows in a Table (VBA)](Get_Total_Columns_Rows_Example_VB.htm)
[Get the Total Number of Columns and Rows in a Table (VB.NET)](Get_Total_Columns_Rows_Example_VBNET.htm)
[Get the Total Number of Columns and Rows in a Table (C#)](Get_Total_Columns_Rows_Example_CSharp.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::SetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2011 SP05, Revision Number 19.5
