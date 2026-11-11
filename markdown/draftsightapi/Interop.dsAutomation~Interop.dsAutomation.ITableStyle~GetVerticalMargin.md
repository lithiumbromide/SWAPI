---
title: "GetVerticalMargin Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetVerticalMargin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetVerticalMargin.html"
---

# GetVerticalMargin Method (ITableStyle)

Gets the size of the vertical margin for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetVerticalMargin( _
   ByVal CellType As dsTableCellType_e _
) As System.Double
```

### C#

```csharp
System.double GetVerticalMargin(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetVerticalMargin(
   CellType : dsTableCellType_e
) : System.double;
```

### Managed Extensions for C++

```
System.double GetVerticalMargin(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
System.double GetVerticalMargin(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Size of the vertical margin for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetVerticalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetVerticalMargin.html)
[ITableStyle::GetHorizontalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetHorizontalMargin.html)
[ITableStyle::SetHorizontalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetHorizontalMargin.html)

## Availability

DraftSight V1R3.0
