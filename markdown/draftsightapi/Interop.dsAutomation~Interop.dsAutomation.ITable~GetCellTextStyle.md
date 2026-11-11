---
title: "GetCellTextStyle Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html"
---

# GetCellTextStyle Method (ITable)

Gets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) for the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellTextStyle( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetCellTextStyle(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellTextStyle(
   Row : System.int,
   Column : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetCellTextStyle(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.String^ GetCellTextStyle(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell whose TextStyle name to get (see **Remarks**)
- `Column`: Index of the column of the cell whose TextStyle name to get (see **Remarks**)

### Return Value

TextStyle name of the specified cell

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
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
