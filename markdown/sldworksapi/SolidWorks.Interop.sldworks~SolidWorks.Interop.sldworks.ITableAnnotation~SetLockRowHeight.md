---
title: "SetLockRowHeight Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetLockRowHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html"
---

# SetLockRowHeight Method (ITableAnnotation)

Sets whether to lock the height of the specified row in this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLockRowHeight( _
   ByVal Index As System.Integer, _
   ByVal LockRowHeight As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim LockRowHeight As System.Boolean
Dim value As System.Boolean

value = instance.SetLockRowHeight(Index, LockRowHeight)
```

### C#

```csharp
System.bool SetLockRowHeight(
   System.int Index,
   System.bool LockRowHeight
)
```

### C++/CLI

```cpp
System.bool SetLockRowHeight(
   System.int Index,
   System.bool LockRowHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the row (see **Remarks**)
- `LockRowHeight`: True to lock this row's height, false to not

### Return Value

True if setting whether to lock the height of the specified row is successful, false if not

## VBA Syntax

See [TableAnnotation::SetLockRowHeight](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetLockRowHeight.html).

## Remarks

Call [ITableAnnotation::RowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html) to get the number of visible rows or [ITableAnnotation::TotalRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html) to get the number of visible and hidden rows in this table annotation.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetLockRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html)
[ITableAnnotation::DeleteRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::GetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html)
[ITableAnnotation::InsertRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::MoveRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::SetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html)
[ITableAnnotation::RowHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
