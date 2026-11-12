---
title: "SetCellBordersVisibility Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html"
---

# SetCellBordersVisibility Method (ITable)

Sets the visibility of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellBordersVisibility( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal Visible As System.Boolean _
)
```

### C#

```csharp
void SetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### JScript

```
function SetCellBordersVisibility(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e,
   Visible : System.boolean
);
```

### Managed Extensions for C++

```
void SetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### C++/CLI

```cpp
void SetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType,
   System.bool Visible
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose visibility to set (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose visibility to set (see **Remarks**)
- `LineType`: Type of Line as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `Visible`: True to show the specified type of Line for the border of the specified cell in this Table, false to hide it

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)

## Availability

DraftSight V1R6.0
