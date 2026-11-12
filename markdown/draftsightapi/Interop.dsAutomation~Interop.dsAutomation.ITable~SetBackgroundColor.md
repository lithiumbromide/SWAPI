---
title: "SetBackgroundColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetBackgroundColor.html"
---

# SetBackgroundColor Method (ITable)

Sets the background Color of the specified type of cell in this Table.

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

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `NewVal`: Background [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBackgroundColor.html)
[ITable::GetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBackgroundColor.html)
[ITable::SetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBackgroundColor.html)

## Availability

DraftSight V1R6.0
