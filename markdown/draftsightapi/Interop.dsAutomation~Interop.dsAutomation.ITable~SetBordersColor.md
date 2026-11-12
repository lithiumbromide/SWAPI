---
title: "SetBordersColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html"
---

# SetBordersColor Method (ITable)

Sets the Color of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetBordersColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color NewVal
)
```

### JScript

```
function SetBordersColor(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color^ NewVal
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `NewVal`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border for the specified type of cell

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)

## Availability

DraftSight V1R6.0
