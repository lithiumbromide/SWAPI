---
title: "GetText Method (ITable)"
project: ""
interface: "ITable"
member: "GetText"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html"
---

# GetText Method (ITable)

Gets the formatted text in the specified cell.

## Syntax

### Visual Basic

```vb
Function GetText( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetText(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetText(
   Row : System.int,
   Column : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetText(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Row in which the cell exists
- `Column`: Column in which the cell exists

### Return Value

Text in the cell

## Remarks

Before calling this method, call [ITable::TotalRowCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalRowCount.html) and [ITable::TotalColumnCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalColumnCount.html) to get valid values for Row and Column.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)
[ITable::GetSimplifiedText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetSimplifiedText.html)

## Availability

DraftSight V1R4.0
