---
title: "SetTextColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html"
---

# SetTextColor Method (ITableStyle)

Sets the Color of the text for the specified type of cell in this TableStyle.

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

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the text for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)
[ITableStyle::GetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html)
[ITableStyle::GetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html)
[ITableStyle::SetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html)
[ITableStyle::SetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html)

## Availability

DraftSight V1R3.0
