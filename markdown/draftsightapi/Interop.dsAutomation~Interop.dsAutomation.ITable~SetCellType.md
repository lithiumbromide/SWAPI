---
title: "SetCellType Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellType.html"
---

# SetCellType Method (ITable)

Sets the type for the specified table cell, row, or column.

## Syntax

### Visual Basic

```vb
Sub SetCellType( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal CellType As dsTableCellType_e _
)
```

### C#

```csharp
void SetCellType(
   System.int Row,
   System.int Column,
   dsTableCellType_e CellType
)
```

### JScript

```
function SetCellType(
   Row : System.int,
   Column : System.int,
   CellType : dsTableCellType_e
);
```

### Managed Extensions for C++

```
void SetCellType(
   System.int Row,
   System.int Column,
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
void SetCellType(
   System.int Row,
   System.int Column,
   dsTableCellType_e CellType
)
```

### Parameters

- `Row`: Row in which the table cell is located or -1 for the entire row in which the table cell is located
- `Column`: Column in which the table cell is located or -1 for the entire column in which the table cell is located
- `CellType`: Type of table cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellType Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellType.html)

## Availability

DraftSight V1R5.0
