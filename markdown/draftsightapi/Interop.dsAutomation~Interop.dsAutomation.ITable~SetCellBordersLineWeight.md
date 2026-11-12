---
title: "SetCellBordersLineWeight Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellBordersLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html"
---

# SetCellBordersLineWeight Method (ITable)

Sets the LineWeight of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellBordersLineWeight( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal LineWeight As dsLineWeight_e _
)
```

### C#

```csharp
void SetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### JScript

```
function SetCellBordersLineWeight(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e,
   LineWeight : dsLineWeight_e
);
```

### Managed Extensions for C++

```
void SetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### C++/CLI

```cpp
void SetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e LineWeight
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose LineWeight to set (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose LineWeight to set (see **Remarks**)
- `LineType`: Type of Line as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `LineWeight`: LineWeight of the specified type of Line for the border for the specified cell in this Table as defined by [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
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
