---
title: "GetCellBordersVisibility Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html"
---

# GetCellBordersVisibility Method (ITable)

Gets the visibility of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellBordersVisibility( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal LineType As dsTableBordersLineType_e _
) As System.Boolean
```

### C#

```csharp
System.bool GetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetCellBordersVisibility(
   Row : System.int,
   Column : System.int,
   LineType : dsTableBordersLineType_e
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
System.bool GetCellBordersVisibility(
   System.int Row,
   System.int Column,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `Row`: Index of the row of the cell with the specified type of Line for its border whose visibility to get (see **Remarks**)
- `Column`: Index of the column of the cell with the specified type of Line for its border whose visibility to get (see **Remarks**)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

True to show the specified type of Line for the border of the specified cell in this Table, false to hide it

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::GetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)

## Availability

DraftSight V1R6.0
