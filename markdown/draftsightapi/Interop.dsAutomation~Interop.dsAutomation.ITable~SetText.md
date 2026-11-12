---
title: "SetText Method (ITable)"
project: ""
interface: "ITable"
member: "SetText"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html"
---

# SetText Method (ITable)

Sets the text of the specified cell.

## Syntax

### Visual Basic

```vb
Sub SetText( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal CellText As System.String _
)
```

### C#

```csharp
void SetText(
   System.int Row,
   System.int Column,
   System.string CellText
)
```

### JScript

```
function SetText(
   Row : System.int,
   Column : System.int,
   CellText : System.String
);
```

### Managed Extensions for C++

```
void SetText(
   System.int Row,
   System.int Column,
   System.string* CellText
)
```

### C++/CLI

```cpp
void SetText(
   System.int Row,
   System.int Column,
   System.String^ CellText
)
```

### Parameters

- `Row`: Row in which the cell exists
- `Column`: Column in which the cell exists
- `CellText`: Text for the cell

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
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

## Availability

DraftSight V1R4.0
