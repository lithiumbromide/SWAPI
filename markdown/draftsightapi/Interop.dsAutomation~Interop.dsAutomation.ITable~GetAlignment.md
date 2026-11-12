---
title: "GetAlignment Method (ITable)"
project: ""
interface: "ITable"
member: "GetAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetAlignment.html"
---

# GetAlignment Method (ITable)

Gets the justification and alignment of the text in the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetAlignment( _
   ByVal CellType As dsTableCellType_e _
) As dsTableCellAlignment_e
```

### C#

```csharp
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetAlignment(
   CellType : dsTableCellType_e
) : dsTableCellAlignment_e;
```

### Managed Extensions for C++

```
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Justification and alignment of the text in the specified type of cell in this Table as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetAlignment.html)
[ITable::GetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellAlignment.html)
[ITable::SetCellAlignment Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellAlignment.html)

## Availability

DraftSight V1R6.0
