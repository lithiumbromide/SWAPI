---
title: "SetTextHeight Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetTextHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html"
---

# SetTextHeight Method (ITableStyle)

Sets the height of the text for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetTextHeight( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As System.Double _
)
```

### C#

```csharp
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### JScript

```
function SetTextHeight(
   CellType : dsTableCellType_e,
   NewVal : System.double
);
```

### Managed Extensions for C++

```
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### C++/CLI

```cpp
void SetTextHeight(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Height of the text for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html)
[ITableStyle::GetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)
[ITableStyle::GetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html)
[ITableStyle::SetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html)
[ITableStyle::SetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html)

## Availability

DraftSight V1R3.0
