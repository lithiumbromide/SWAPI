---
title: "SetTextStyle Method (ITable)"
project: ""
interface: "ITable"
member: "SetTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html"
---

# SetTextStyle Method (ITable)

Sets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) for the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetTextStyle( _
   ByVal CellType As dsTableCellType_e, _
   ByVal TextStyle As System.String _
)
```

### C#

```csharp
void SetTextStyle(
   dsTableCellType_e CellType,
   System.string TextStyle
)
```

### JScript

```
function SetTextStyle(
   CellType : dsTableCellType_e,
   TextStyle : System.String
);
```

### Managed Extensions for C++

```
void SetTextStyle(
   dsTableCellType_e CellType,
   System.string* TextStyle
)
```

### C++/CLI

```cpp
void SetTextStyle(
   dsTableCellType_e CellType,
   System.String^ TextStyle
)
```

### Parameters

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `TextStyle`: Name of the TextStyle for the specified type of cell in this Table

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
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
