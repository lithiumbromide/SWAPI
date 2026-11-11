---
title: "SetTextColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html"
---

# SetTextColor Method (ITable)

Sets the Color of the text for the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetTextColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetTextColor(
   dsTableCellType_e CellType,
   Color NewVal
)
```

### JScript

```
function SetTextColor(
   CellType : dsTableCellType_e,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetTextColor(
   dsTableCellType_e CellType,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetTextColor(
   dsTableCellType_e CellType,
   Color^ NewVal
)
```

### Parameters

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of specified type of cell

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
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
