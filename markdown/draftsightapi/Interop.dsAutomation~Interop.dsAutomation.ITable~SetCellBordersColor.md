---
title: "SetCellBordersColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html"
---

# SetCellBordersColor Method (ITable)

Sets the Color of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellBordersColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   Color NewVal
)
```

### JScript

```
function SetCellBordersColor(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   Color^ NewVal
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose Color to set (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose Color to set (see **Remarks**)
- `LineType`: Type of Line as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `NewVal`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)

## Availability

DraftSight V1R6.0
