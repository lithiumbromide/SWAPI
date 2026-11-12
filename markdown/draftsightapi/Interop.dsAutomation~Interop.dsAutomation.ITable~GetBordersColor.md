---
title: "GetBordersColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html"
---

# GetBordersColor Method (ITable)

Gets the color of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetBordersColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e _
) As Color
```

### C#

```csharp
Color GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetBordersColor(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
Color^ GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border for the specified type of cell

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetCellBordersColor](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetCellBordersLineWeight](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetCellBordersVisibility](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)

## Availability

DraftSight V1R6.0
