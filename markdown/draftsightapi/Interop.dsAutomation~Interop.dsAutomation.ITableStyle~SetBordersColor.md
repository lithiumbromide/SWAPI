---
title: "SetBordersColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersColor.html"
---

# SetBordersColor Method (ITableStyle)

Sets the Color of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetBordersColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color NewVal
)
```

### JScript

```
function SetBordersColor(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   Color^ NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `NewVal`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border for the specified type of cell

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersColor.html)

## Availability

DraftSight V1R3.0
