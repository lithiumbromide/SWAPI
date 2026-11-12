---
title: "DeleteColumn Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "DeleteColumn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html"
---

# DeleteColumn Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::DeleteColumn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteColumn( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.DeleteColumn(Index)
```

### C#

```csharp
System.bool DeleteColumn(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteColumn(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the column you want to delete

### Return Value

True if column is deleted successfully, false if not

## VBA Syntax

See [TableAnnotation::DeleteColumn](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~DeleteColumn.html).

## Remarks

The index for both the rows and columns is 0-based.

This method deletes the entire table if you try to delete the only column in the table.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
