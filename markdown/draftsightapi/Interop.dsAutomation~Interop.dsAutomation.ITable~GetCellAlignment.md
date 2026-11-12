---
title: "GetCellAlignment Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellAlignment.html"
---

# GetCellAlignment Method (ITable)

Gets the justification and alignment of the text in the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellAlignment( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As dsTableCellAlignment_e
```

### C#

```csharp
dsTableCellAlignment_e GetCellAlignment(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellAlignment(
   Row : System.int,
   Column : System.int
) : dsTableCellAlignment_e;
```

### Managed Extensions for C++

```
dsTableCellAlignment_e GetCellAlignment(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
dsTableCellAlignment_e GetCellAlignment(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell in which to get the justification and alignment of the text (see **Remarks**)
- `Column`: Index of the column of the cell in which to get the justification and alignment of the text (see **Remarks**)

### Return Value

Justification and alignment of the text in the specified cell in this Table as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellAlignment.html)
[ITable::GetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetAlignment.html)
[ITable::SetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetAlignment.html)

## Availability

DraftSight V1R6.0
