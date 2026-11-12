---
title: "SetBordersLineWeight Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetBordersLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersLineWeight.html"
---

# SetBordersLineWeight Method (ITableStyle)

Sets the LineWeight of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetBordersLineWeight( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e, _
   ByVal NewVal As dsLineWeight_e _
)
```

### C#

```csharp
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e NewVal
)
```

### JScript

```
function SetBordersLineWeight(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e,
   NewVal : dsLineWeight_e
);
```

### Managed Extensions for C++

```
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e NewVal
)
```

### C++/CLI

```cpp
void SetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType,
   dsLineWeight_e NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)
- `NewVal`: Line weight of the specified type of Line for the border of the specified type of cell in this TableStyle as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersLineWeight.html)

## Availability

DraftSight V1R3.0
