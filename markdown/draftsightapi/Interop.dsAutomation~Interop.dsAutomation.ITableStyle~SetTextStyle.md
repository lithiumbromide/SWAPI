---
title: "SetTextStyle Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html"
---

# SetTextStyle Method (ITableStyle)

Sets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetTextStyle( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As System.String _
)
```

### C#

```csharp
void SetTextStyle(
   dsTableCellType_e CellType,
   System.string NewVal
)
```

### JScript

```
function SetTextStyle(
   CellType : dsTableCellType_e,
   NewVal : System.String
);
```

### Managed Extensions for C++

```
void SetTextStyle(
   dsTableCellType_e CellType,
   System.string* NewVal
)
```

### C++/CLI

```cpp
void SetTextStyle(
   dsTableCellType_e CellType,
   System.String^ NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Name of the TextStyle for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html)
[ITableStyle::GetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)
[ITableStyle::GetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html)
[ITableStyle::SetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html)
[ITableStyle::SetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html)

## Availability

DraftSight V1R3.0
