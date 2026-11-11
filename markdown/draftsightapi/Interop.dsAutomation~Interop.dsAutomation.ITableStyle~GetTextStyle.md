---
title: "GetTextStyle Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextStyle.html"
---

# GetTextStyle Method (ITableStyle)

Gets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetTextStyle( _
   ByVal CellType As dsTableCellType_e _
) As System.String
```

### C#

```csharp
System.string GetTextStyle(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetTextStyle(
   CellType : dsTableCellType_e
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetTextStyle(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
System.String^ GetTextStyle(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Name of the TextStyle for the specified type of cell in this TableStyle

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextStyle.html)
[ITableStyle::GetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextColor.html)
[ITableStyle::GetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetTextHeight.html)
[ITableStyle::SetTextColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextColor.html)
[ITableStyle::SetTextHeight Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetTextHeight.html)

## Availability

DraftSight V1R3.0
