---
title: "GetHorizontalMargin Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetHorizontalMargin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetHorizontalMargin.html"
---

# GetHorizontalMargin Method (ITableStyle)

Gets the size of the horizontal margin for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetHorizontalMargin( _
   ByVal CellType As dsTableCellType_e _
) As System.Double
```

### C#

```csharp
System.double GetHorizontalMargin(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetHorizontalMargin(
   CellType : dsTableCellType_e
) : System.double;
```

### Managed Extensions for C++

```
System.double GetHorizontalMargin(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
System.double GetHorizontalMargin(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Size of the horizontal margin for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetHorizontalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetHorizontalMargin.html)
[ITableStyle::GetVerticalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetVerticalMargin.html)
[ITableStyle::SetVerticalMargin Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetVerticalMargin.html)

## Availability

DraftSight V1R3.0
