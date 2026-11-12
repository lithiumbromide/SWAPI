---
title: "GetColumnTitle Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetColumnTitle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html"
---

# GetColumnTitle Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::GetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnTitle( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.String

value = instance.GetColumnTitle(Index)
```

### C#

```csharp
System.string GetColumnTitle(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetColumnTitle(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index indicating the column

### Return Value

Column title

## VBA Syntax

See [TableAnnotation::GetColumnTitle](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetColumnTitle.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
