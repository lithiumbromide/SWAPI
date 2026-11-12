---
title: "GetTextColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetTextColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html"
---

# GetTextColor Method (ITableStyle)

Gets the Color of the text for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetTextColor( _
   ByVal CellType As dsTableCellType_e _
) As Color
```

### C#

```csharp
Color GetTextColor(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetTextColor(
   CellType : dsTableCellType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetTextColor(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
Color^ GetTextColor(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) of the text for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html)
[ITableStyle::GetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html)
[ITableStyle::SetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html)
[ITableStyle::SetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html)
[ITableStyle::GetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html)

## Availability

DraftSight V1R3.0
