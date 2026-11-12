---
title: "GetTextColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html"
---

# GetTextColor Method (ITable)

Gets the Color of the text for the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetTextColor( _
   ByVal CellType As dsTableCellType_e _
) As Color
```

### C#

```csharp
Color GetTextColor(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetTextColor(
   CellType : dsTableCellType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetTextColor(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
Color^ GetTextColor(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the text for the specified type of cell in this Table

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
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
