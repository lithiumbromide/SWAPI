---
title: "SetBordersVisibility Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersVisibility.html"
---

# SetBordersVisibility Method (ITableStyle)

Sets the visibility of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetBordersVisibility( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal NewVal As System.Boolean _
)
```

### C#

```csharp
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool NewVal
)
```

### JScript

```
function SetBordersVisibility(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   NewVal : System.boolean
);
```

### Managed Extensions for C++

```
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool NewVal
)
```

### C++/CLI

```cpp
void SetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   System.bool NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `NewVal`: True to show the specified type of Line for the border of the specified type of cell in this TableStyle, false to hide it

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersVisibility.html)

## Availability

DraftSight V1R3.0
