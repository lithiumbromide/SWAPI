---
title: "SetCellTextStyle Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html"
---

# SetCellTextStyle Method (ITable)

Sets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellTextStyle( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal TextStyle As System.String _
)
```

### C#

```csharp
void SetCellTextStyle(
   System.int Row,
   System.int Column,
   System.string TextStyle
)
```

### JScript

```
function SetCellTextStyle(
   Row : System.int,
   Column : System.int,
   TextStyle : System.String
);
```

### Managed Extensions for C++

```
void SetCellTextStyle(
   System.int Row,
   System.int Column,
   System.string* TextStyle
)
```

### C++/CLI

```cpp
void SetCellTextStyle(
   System.int Row,
   System.int Column,
   System.String^ TextStyle
)
```

### Parameters

- `Row`: Index of the row of the cell whose TextStyle name to set (see **Remarks**)
- `Column`: Index of the column of the cell whose TextStyle name to set (see **Remarks**)
- `TextStyle`: TextStyle name to set for the specified cell in this Table

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)

## Availability

DraftSight V1R6.0
