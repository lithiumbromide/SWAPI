---
title: "SetTextHeight Method (ITable)"
project: ""
interface: "ITable"
member: "SetTextHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html"
---

# SetTextHeight Method (ITable)

Sets the height of the specified type of cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetTextHeight( _
   ByVal CellType As dsTableCellType_e, _
   ByVal Height As System.Double _
)
```

### C#

```csharp
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double Height
)
```

### JScript

```
function SetTextHeight(
   CellType : dsTableCellType_e,
   Height : System.double
);
```

### Managed Extensions for C++

```
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double Height
)
```

### C++/CLI

```cpp
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double Height
)
```

### Parameters

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `Height`: Height of the specified type of cell in this Table

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)

## Availability

DraftSight V1R6.0
