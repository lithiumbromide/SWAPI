---
title: "SetAlignment Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetAlignment.html"
---

# SetAlignment Method (ITableStyle)

Sets the justification and alignment of the text in the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetAlignment( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As dsTableCellAlignment_e _
)
```

### C#

```csharp
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e NewVal
)
```

### JScript

```
function SetAlignment(
   CellType : dsTableCellType_e,
   NewVal : dsTableCellAlignment_e
);
```

### Managed Extensions for C++

```
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e NewVal
)
```

### C++/CLI

```cpp
void SetAlignment(
   dsTableCellType_e CellType,
   dsTableCellAlignment_e NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Justification and alignment of the text in the specified type of cell in this TableStyle as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetAlignment Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetAlignment.html)

## Availability

DraftSight V1R3.0
