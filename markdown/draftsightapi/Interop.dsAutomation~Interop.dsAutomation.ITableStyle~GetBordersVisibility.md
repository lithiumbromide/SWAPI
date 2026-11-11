---
title: "GetBordersVisibility Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersVisibility.html"
---

# GetBordersVisibility Method (ITableStyle)

Gets the visibility of the specified type of Line for the border of the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetBordersVisibility( _
   ByVal CellType As dsTableCellType_e, _
   ByVal LineType As dsTableBordersLineType_e _
) As System.Boolean
```

### C#

```csharp
System.bool GetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### JScript

```
function GetBordersVisibility(
   CellType : dsTableCellType_e,
   LineType : dsTableBordersLineType_e
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### C++/CLI

```cpp
System.bool GetBordersVisibility(
   dsTableCellType_e CellType,
   dsTableBordersLineType_e LineType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

True if the specified type of Line for the border of the specified type of cell in this TableStyle is visible, false if it is hidden

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetBordersVisibility Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersVisibility.html)
[ITableStyle::GetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersColor.html)
[ITableStyle::GetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBordersLineWeight.html)
[ITableStyle::SetBordersColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersColor.html)
[ITableStyle::SetBordersLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBordersLineWeight.html)

## Availability

DraftSight V1R3.0
