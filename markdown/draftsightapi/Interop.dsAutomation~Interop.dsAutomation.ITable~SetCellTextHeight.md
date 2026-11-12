---
title: "SetCellTextHeight Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellTextHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html"
---

# SetCellTextHeight Method (ITable)

Sets the height of the text for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellTextHeight( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal Height As System.Double _
)
```

### C#

```csharp
void SetCellTextHeight(
   System.int Row,
   System.int Column,
   System.double Height
)
```

### JScript

```
function SetCellTextHeight(
   Row : System.int,
   Column : System.int,
   Height : System.double
);
```

### Managed Extensions for C++

```
void SetCellTextHeight(
   System.int Row,
   System.int Column,
   System.double Height
)
```

### C++/CLI

```cpp
void SetCellTextHeight(
   System.int Row,
   System.int Column,
   System.double Height
)
```

### Parameters

- `Row`: Index of the row of the cell whose text height to set (see **Remarks**)
- `Column`: Index of the column of the cell whose text height to set (see **Remarks**)
- `Height`: Height of the text for the specified cell in this Table

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)

## Availability

DraftSight V1R6.0
