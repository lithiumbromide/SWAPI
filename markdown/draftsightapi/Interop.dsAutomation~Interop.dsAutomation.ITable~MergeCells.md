---
title: "MergeCells Method (ITable)"
project: ""
interface: "ITable"
member: "MergeCells"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~MergeCells.html"
---

# MergeCells Method (ITable)

Merges the specified rectangular region of cells in this Table.

## Syntax

### Visual Basic

```vb
Sub MergeCells( _
   ByVal MinRow As System.Integer, _
   ByVal MaxRow As System.Integer, _
   ByVal MinColumn As System.Integer, _
   ByVal MaxColumn As System.Integer _
)
```

### C#

```csharp
void MergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### JScript

```
function MergeCells(
   MinRow : System.int,
   MaxRow : System.int,
   MinColumn : System.int,
   MaxColumn : System.int
);
```

### Managed Extensions for C++

```
void MergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### C++/CLI

```cpp
void MergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### Parameters

- `MinRow`: Minimum index of the row of cells to merge
- `MaxRow`: Maximum index of the row of cells to merge
- `MinColumn`: Minimum index of the column of cells to merge
- `MaxColumn`: Maximum index of the column of cells to merge

## Remarks

To determine a valid index for a row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::UnmergeCells Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~UnmergeCells.html)

## Availability

DraftSight V1R6.0
