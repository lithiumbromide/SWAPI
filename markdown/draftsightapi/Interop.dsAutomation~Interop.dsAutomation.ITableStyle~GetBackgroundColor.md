---
title: "GetBackgroundColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBackgroundColor.html"
---

# GetBackgroundColor Method (ITableStyle)

Gets the background Color for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetBackgroundColor( _
   ByVal CellType As dsTableCellType_e _
) As Color
```

### C#

```csharp
Color GetBackgroundColor(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetBackgroundColor(
   CellType : dsTableCellType_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetBackgroundColor(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
Color^ GetBackgroundColor(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Background [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetBackgroundColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBackgroundColor.html)

## Availability

DraftSight V1R3.0
