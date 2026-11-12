---
title: "SetHorizontalMargin Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetHorizontalMargin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetHorizontalMargin.html"
---

# SetHorizontalMargin Method (ITableStyle)

Sets the size of the horizontal margin for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetHorizontalMargin( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As System.Double _
)
```

### C#

```csharp
void SetHorizontalMargin(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### JScript

```
function SetHorizontalMargin(
   CellType : dsTableCellType_e,
   NewVal : System.double
);
```

### Managed Extensions for C++

```
void SetHorizontalMargin(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### C++/CLI

```cpp
void SetHorizontalMargin(
   dsTableCellType_e CellType,
   System.double NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Size of the horizontal margin for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetHorizontalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetHorizontalMargin.html)
[ITableStyle::SetVerticalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetVerticalMargin.html)
[ITableStyle::GetVerticalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetVerticalMargin.html)

## Availability

DraftSight V1R3.0
