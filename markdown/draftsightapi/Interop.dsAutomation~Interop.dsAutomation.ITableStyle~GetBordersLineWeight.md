---
title: "GetBordersLineWeight Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetBordersLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersLineWeight.html"
---

# GetBordersLineWeight Method (ITableStyle)

Gets the LineWeight of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetBordersLineWeight( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e _
) As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e GetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetBordersLineWeight(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e
) : dsLineWeight_e;
```

### Managed Extensions for C++

```
dsLineWeight_e GetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
dsLineWeight_e GetBordersLineWeight(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

LineWeight of the specified type of line for the border of the specified type of cell in this TableStyle as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersLineWeight.html)
[ITableStyle::GetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersColor.html)
[ITableStyle::GetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersVisibility.html)
[ITableStyle::SetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersColor.html)
[ITableStyle::SetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersVisibility.html)

## Availability

DraftSight V1R3.0
