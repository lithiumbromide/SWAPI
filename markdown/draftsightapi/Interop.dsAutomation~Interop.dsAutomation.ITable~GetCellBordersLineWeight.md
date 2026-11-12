---
title: "GetCellBordersLineWeight Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellBordersLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html"
---

# GetCellBordersLineWeight Method (ITable)

Gets the LineWeight of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) of the border for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellBordersLineWeight( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e _
) As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e GetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetCellBordersLineWeight(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e
) : dsLineWeight_e;
```

### Managed Extensions for C++

```
dsLineWeight_e GetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
dsLineWeight_e GetCellBordersLineWeight(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose LineWeight to get (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose LineWeight to get (see **Remarks**)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

LineWeight of the specified type of Line for the border for the specified cell in this Table as defined by [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
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
