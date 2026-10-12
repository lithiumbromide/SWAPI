---
title: "SetLockColumnWidth Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetLockColumnWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html"
---

# SetLockColumnWidth Method (ITableAnnotation)

Sets whether to lock the width of the specified column in this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLockColumnWidth( _
   ByVal Index As System.Integer, _
   ByVal LockColumnWidth As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim LockColumnWidth As System.Boolean
Dim value As System.Boolean

value = instance.SetLockColumnWidth(Index, LockColumnWidth)
```

### C#

```csharp
System.bool SetLockColumnWidth(
   System.int Index,
   System.bool LockColumnWidth
)
```

### C++/CLI

```cpp
System.bool SetLockColumnWidth(
   System.int Index,
   System.bool LockColumnWidth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the column (see **Remarks**)
- `LockColumnWidth`: True to lock this column's width, false to not

### Return Value

True if setting whether to lock the width of the specified column is successful, false if not

## VBA Syntax

See [TableAnnotation::SetLockColumnWidth](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetLockColumnWidth.html).

## Remarks

Call [ITableAnnotation::ColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html) to get the number of visible columns or [ITableAnnotation::TotalColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html) to get the number of visible and hidden columns in this table annotation.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetLockColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::DeleteColumn Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.html)
[ITableAnnotation::MoveColumn Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::SetColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html)
[ITableAnnotation::ColumnHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
