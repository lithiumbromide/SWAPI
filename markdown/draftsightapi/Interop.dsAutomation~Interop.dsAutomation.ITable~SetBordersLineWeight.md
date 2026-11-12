---
title: "SetBordersLineWeight Method (ITable)"
project: ""
interface: "ITable"
member: "SetBordersLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html"
---

# SetBordersLineWeight Method (ITable)

Sets the LineWeight of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetBordersLineWeight( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal LineWeight As dsLineWeight_e _
)
```

### C#

```csharp
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### JScript

```
function SetBordersLineWeight(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   LineWeight : dsLineWeight_e
);
```

### Managed Extensions for C++

```
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### C++/CLI

```cpp
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `LineWeight`: LineWeight of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type of cell in this Table as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)

## Availability

DraftSight V1R6.0
