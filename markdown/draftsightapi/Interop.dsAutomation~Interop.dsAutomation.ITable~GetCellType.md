---
title: "GetCellType Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellType.html"
---

# GetCellType Method (ITable)

Gets the type of the specified table cell, row, or column.

## Syntax

### Visual Basic

```vb
Function GetCellType( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As dsTableCellType_e
```

### C#

```csharp
dsTableCellType_e GetCellType(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellType(
   Row : System.int,
   Column : System.int
) : dsTableCellType_e;
```

### Managed Extensions for C++

```
dsTableCellType_e GetCellType(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
dsTableCellType_e GetCellType(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Row in which the table cell is located or -1 for the entire row in which the table cell is located
- `Column`: Column in which the table cell is located or -1 for the entire column in which the table cell is located

### Return Value

Type of table cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellType Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellType.html)

## Availability

DraftSight V1R5.0
