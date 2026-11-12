---
title: "SetCellRange Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetCellRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html"
---

# SetCellRange Method (ITableAnnotation)

Sets the current range of cells.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCellRange( _
   ByVal FirstRow As System.Integer, _
   ByVal LastRow As System.Integer, _
   ByVal FirstColumn As System.Integer, _
   ByVal LastColumn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer

instance.SetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

### C#

```csharp
void SetCellRange(
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
)
```

### C++/CLI

```cpp
void SetCellRange(
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstRow`: First row in the range
- `LastRow`: Last row in the range
- `FirstColumn`: First column in the range
- `LastColumn`: Last column in the range

## VBA Syntax

See [TableAnnotation::SetCellRange](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetCellRange.html).

## Remarks

The index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::DisplayedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
