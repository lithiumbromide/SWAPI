---
title: "SetBackgroundColor Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "SetBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetBackgroundColor.html"
---

# SetBackgroundColor Method (ITableStyle)

Sets the background Color for the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Sub SetBackgroundColor( _
   ByVal CellType As dsTableCellType_e, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetBackgroundColor(
   dsTableCellType_e CellType,
   Color NewVal
)
```

### JScript

```
function SetBackgroundColor(
   CellType : dsTableCellType_e,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetBackgroundColor(
   dsTableCellType_e CellType,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetBackgroundColor(
   dsTableCellType_e CellType,
   Color^ NewVal
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Background [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetBackgroundColor Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetBackgroundColor.html)

## Availability

DraftSight V1R3.0
