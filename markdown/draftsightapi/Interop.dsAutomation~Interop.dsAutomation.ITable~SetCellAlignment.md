---
title: "SetCellAlignment Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellAlignment.html"
---

# SetCellAlignment Method (ITable)

Sets the justification and alignment of the text in the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellAlignment( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal Alignment As dsTableCellAlignment_e _
)
```

### C#

```csharp
void SetCellAlignment(
   System.int Row,
   System.int Column,
   dsTableCellAlignment_e Alignment
)
```

### JScript

```
function SetCellAlignment(
   Row : System.int,
   Column : System.int,
   Alignment : dsTableCellAlignment_e
);
```

### Managed Extensions for C++

```
void SetCellAlignment(
   System.int Row,
   System.int Column,
   dsTableCellAlignment_e Alignment
)
```

### C++/CLI

```cpp
void SetCellAlignment(
   System.int Row,
   System.int Column,
   dsTableCellAlignment_e Alignment
)
```

### Parameters

- `Row`: Index of the row of the cell in which to set the justification and alignment of the text (see **Remarks**)
- `Column`: Index of the column of the cell in which to set the justification and alignment of the text (see **Remarks**)
- `Alignment`: Justification and alignment of the text in the specified cell in this Table as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellAlignment.html)
[ITable::SetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetAlignment.html)
[ITable::GetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetAlignment.html)

## Availability

DraftSight V1R6.0
