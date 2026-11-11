---
title: "GetCellBordersColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html"
---

# GetCellBordersColor Method (ITable)

Gets the Color of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellBordersColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e _
) As Color
```

### C#

```csharp
Color GetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetCellBordersColor(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
Color^ GetCellBordersColor(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose Color to get (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose Color to get (see **Remarks**)
- `LineType`: Type of Line as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border for the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetBordersVisibility ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)

## Availability

DraftSight V1R6.0
