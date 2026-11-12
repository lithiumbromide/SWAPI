---
title: "GetCellHorizontalMargin Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellHorizontalMargin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellHorizontalMargin.html"
---

# GetCellHorizontalMargin Method (ITable)

Gets the size of the horizontal margin of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellHorizontalMargin( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetCellHorizontalMargin(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellHorizontalMargin(
   Row : System.int,
   Column : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetCellHorizontalMargin(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.double GetCellHorizontalMargin(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell whose horizontal margin to get (see **Remarks**)
- `Column`: Index of the column of the cell whose horizontal margin to get (see **Remarks**)

### Return Value

Size of the horizontal margin of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellHorizontalMargin.html)
[ITable::SetHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetHorizontalMargin.html)
[ITable::GetHorizontalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetHorizontalMargin.html)
[ITable::GetCellVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellVerticalMargin.html)
[ITable::GetVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetVerticalMargin.html)
[ITable::SetCellVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellVerticalMargin.html)
[ITable::SetVerticalMargin Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetVerticalMargin.html)

## Availability

DraftSight V1R6.0
