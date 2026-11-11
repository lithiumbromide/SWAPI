---
title: "GetBordersColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetBordersColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersColor.html"
---

# GetBordersColor Method (ITableStyle)

Gets the Color of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetBordersColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e _
) As Color
```

### C#

```csharp
Color GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetBordersColor(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
Color^ GetBordersColor(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the specified type of Line for the border for the specified type of cell

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersColor.html)
[ITableStyle::GetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersLineWeight.html)
[ITableStyle::GetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersVisibility.html)
[ITableStyle::SetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersLineWeight.html)
[ITableStyle::SetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersVisibility.html)

## Availability

DraftSight V1R3.0
