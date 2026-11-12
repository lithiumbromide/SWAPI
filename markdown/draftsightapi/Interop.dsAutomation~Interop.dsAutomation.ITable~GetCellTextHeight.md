---
title: "GetCellTextHeight Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellTextHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html"
---

# GetCellTextHeight Method (ITable)

Gets the height of the text of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellTextHeight( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetCellTextHeight(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellTextHeight(
   Row : System.int,
   Column : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetCellTextHeight(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.double GetCellTextHeight(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell whose text height to get (see **Remarks**)
- `Column`: Index of the column of the cell whose text height to get (see **Remarks**)

### Return Value

Height of the text of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)

## Availability

DraftSight V1R6.0
