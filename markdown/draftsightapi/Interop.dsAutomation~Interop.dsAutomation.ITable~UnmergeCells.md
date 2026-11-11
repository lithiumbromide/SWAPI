---
title: "UnmergeCells Method (ITable)"
project: ""
interface: "ITable"
member: "UnmergeCells"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~UnmergeCells.html"
---

# UnmergeCells Method (ITable)

Unmerges a previously merged rectangular region of cells in this Table.

## Syntax

### Visual Basic

```vb
Sub UnmergeCells( _
   ByVal MinRow As System.Integer, _
   ByVal MaxRow As System.Integer, _
   ByVal MinColumn As System.Integer, _
   ByVal MaxColumn As System.Integer _
)
```

### C#

```csharp
void UnmergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### JScript

```
function UnmergeCells(
   MinRow : System.int,
   MaxRow : System.int,
   MinColumn : System.int,
   MaxColumn : System.int
);
```

### Managed Extensions for C++

```
void UnmergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### C++/CLI

```cpp
void UnmergeCells(
   System.int MinRow,
   System.int MaxRow,
   System.int MinColumn,
   System.int MaxColumn
)
```

### Parameters

- `MinRow`: Minimum index of the row of cells to unmerge
- `MaxRow`: Maximum index of the row of the rectangular region of cells to unmerge
- `MinColumn`: Minimum index of the column of cells to unmerge
- `MaxColumn`: Minimum index of the column of cells to unmerge

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::MergeCells Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~MergeCells.html)

## Availability

DraftSight V1R6.0
