---
title: "SetAlignment Method (ITable)"
project: ""
interface: "ITable"
member: "SetAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetAlignment.html"
---

# SetAlignment Method (ITable)

Sets the justification and alignment of the text in the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetAlignment( _
   ByVal CellType As dsTableCellType_e, _
   ByVal Alignment As dsTableCellAlignment_e _
)
```

### C#

```csharp
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e Alignment
)
```

### JScript

```
function SetAlignment(
   CellType : dsTableCellType_e,
   Alignment : dsTableCellAlignment_e
);
```

### Managed Extensions for C++

```
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e Alignment
)
```

### C++/CLI

```cpp
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e Alignment
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `Alignment`: Justification and alignment of the text in the specified type of cell in this Table as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetAlignment.html)
[ITable::SetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellAlignment.html)
[ITable::GetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellAlignment.html)

## Availability

DraftSight V1R6.0
