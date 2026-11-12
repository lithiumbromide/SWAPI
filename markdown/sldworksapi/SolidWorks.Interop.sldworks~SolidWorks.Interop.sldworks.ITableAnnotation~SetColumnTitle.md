---
title: "SetColumnTitle Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetColumnTitle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html"
---

# SetColumnTitle Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::SetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnTitle( _
   ByVal Index As System.Integer, _
   ByVal Title As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Title As System.String
Dim value As System.Boolean

value = instance.SetColumnTitle(Index, Title)
```

### C#

```csharp
System.bool SetColumnTitle(
   System.int Index,
   System.string Title
)
```

### C++/CLI

```cpp
System.bool SetColumnTitle(
   System.int Index,
   System.String^ Title
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the column whose title to set
- `Title`: Column title

### Return Value

True if title is set, false if not

## VBA Syntax

See [TableAnnotation::SetColumnTitle](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetColumnTitle.html).

## Remarks

The index for both rows and columns is 0-based.

False is returned if the table does not have a header enabled. The title cannot be set to empty text.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::SetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
