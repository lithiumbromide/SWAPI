---
title: "GetCellTextColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html"
---

# GetCellTextColor Method (ITable)

Gets the Color of the text of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellTextColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As Color
```

### C#

```csharp
Color GetCellTextColor(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellTextColor(
   Row : System.int,
   Column : System.int
) : Color;
```

### Managed Extensions for C++

```
Color* GetCellTextColor(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
Color^ GetCellTextColor(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell whose text Color to get (see **Remarks**)
- `Column`: Index of the column of the cell whose text Color to get (see **Remarks**)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of text of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)

## Availability

DraftSight V1R6.0
