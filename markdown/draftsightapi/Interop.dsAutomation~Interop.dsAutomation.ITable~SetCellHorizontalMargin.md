---
title: "SetCellHorizontalMargin Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellHorizontalMargin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellHorizontalMargin.html"
---

# SetCellHorizontalMargin Method (ITable)

Sets the size of the horizontal margin of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellHorizontalMargin( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal Margin As System.Double _
)
```

### C#

```csharp
void SetCellHorizontalMargin(
   System.int Row,
   System.int Column,
   System.double Margin
)
```

### JScript

```
function SetCellHorizontalMargin(
   Row : System.int,
   Column : System.int,
   Margin : System.double
);
```

### Managed Extensions for C++

```
void SetCellHorizontalMargin(
   System.int Row,
   System.int Column,
   System.double Margin
)
```

### C++/CLI

```cpp
void SetCellHorizontalMargin(
   System.int Row,
   System.int Column,
   System.double Margin
)
```

### Parameters

- `Row`: Index of the row of the cell whose horizontal margin to set (see **Remarks**)
- `Column`: Index of the column of the cell whose horizontal margin to set (see **Remarks**)
- `Margin`: Size of the horizontal margin of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellHorizontalMargin.html)
[ITable::GetHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetHorizontalMargin.html)
[ITable::SetHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetHorizontalMargin.html)
[ITable::SetCellVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellVerticalMargin.html)
[ITable::SetVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetVerticalMargin.html)
[ITable::GetCellVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellVerticalMargin.html)
[ITable::GetVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetVerticalMargin.html)

## Availability

DraftSight V1R6.0
