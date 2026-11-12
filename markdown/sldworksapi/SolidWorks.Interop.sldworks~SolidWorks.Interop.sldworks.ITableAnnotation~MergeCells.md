---
title: "MergeCells Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "MergeCells"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html"
---

# MergeCells Method (ITableAnnotation)

Merges the cells in the specified range.

## Syntax

### Visual Basic (Declaration)

```vb
Function MergeCells( _
   ByVal RowStart As System.Integer, _
   ByVal ColumnStart As System.Integer, _
   ByVal RowEnd As System.Integer, _
   ByVal ColumnEnd As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim RowStart As System.Integer
Dim ColumnStart As System.Integer
Dim RowEnd As System.Integer
Dim ColumnEnd As System.Integer
Dim value As System.Boolean

value = instance.MergeCells(RowStart, ColumnStart, RowEnd, ColumnEnd)
```

### C#

```csharp
System.bool MergeCells(
   System.int RowStart,
   System.int ColumnStart,
   System.int RowEnd,
   System.int ColumnEnd
)
```

### C++/CLI

```cpp
System.bool MergeCells(
   System.int RowStart,
   System.int ColumnStart,
   System.int RowEnd,
   System.int ColumnEnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowStart`: Index of row at which start the merge
- `ColumnStart`: Index of column at which to start the merge
- `RowEnd`: Index of row at which to end the merge
- `ColumnEnd`: Index of column at which to end the merge

### Return Value

True if the cells in the specified range merge successfully, false if not

## VBA Syntax

See [TableAnnotation::MergeCells](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~MergeCells.html).

## Remarks

The index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
