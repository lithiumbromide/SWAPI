---
title: "GetTextHeight Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetTextHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html"
---

# GetTextHeight Method (ITableStyle)

Gets the height of the text for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetTextHeight( _
   ByVal CellType As dsTableCellType_e _
) As System.Double
```

### C#

```csharp
System.double GetTextHeight(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetTextHeight(
   CellType : dsTableCellType_e
) : System.double;
```

### Managed Extensions for C++

```
System.double GetTextHeight(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
System.double GetTextHeight(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Height of the text for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html)
[ITableStyle::GetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)
[ITableStyle::GetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html)
[ITableStyle::SetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html)
[ITableStyle::SetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html)

## Availability

DraftSight V1R3.0
