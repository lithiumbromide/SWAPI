---
title: "SetBordersVisibility Method (ITable)"
project: ""
interface: "ITable"
member: "SetBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html"
---

# SetBordersVisibility Method (ITable)

Sets the visibility of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetBordersVisibility( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal Visible As System.Boolean _
)
```

### C#

```csharp
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### JScript

```
function SetBordersVisibility(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   Visible : System.boolean
);
```

### Managed Extensions for C++

```
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### C++/CLI

```cpp
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `Visible`: True to show the specified type of Line for the border of the specified type of cell in this Table, false to hide it

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)

## Availability

DraftSight V1R6.0
