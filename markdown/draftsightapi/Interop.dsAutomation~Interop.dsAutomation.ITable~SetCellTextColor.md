---
title: "SetCellTextColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html"
---

# SetCellTextColor Method (ITable)

Sets the Color of the text for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellTextColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal NewColor As Color _
)
```

### C#

```csharp
void SetCellTextColor(
   System.int Row,
   System.int Column,
   Color NewColor
)
```

### JScript

```
function SetCellTextColor(
   Row : System.int,
   Column : System.int,
   NewColor : Color
);
```

### Managed Extensions for C++

```
void SetCellTextColor(
   System.int Row,
   System.int Column,
   Color* NewColor
)
```

### C++/CLI

```cpp
void SetCellTextColor(
   System.int Row,
   System.int Column,
   Color^ NewColor
)
```

### Parameters

- `Row`: Index of the row of the cell whose Color to set (see **Remarks**)
- `Column`: Index of the column of the cell whose Color to set (see **Remarks**)
- `NewColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the text for the specified cell in this Table

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
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
