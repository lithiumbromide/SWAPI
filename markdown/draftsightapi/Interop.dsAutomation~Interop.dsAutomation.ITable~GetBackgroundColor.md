---
title: "GetBackgroundColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetBackgroundColor.html"
---

# GetBackgroundColor Method (ITable)

Gets the background color for the specified type of cell in this Table.

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

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Background [color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBackgroundColor.html)
[ITable::GetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBackgroundColor.html)
[ITable::SetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBackgroundColor.html)

## Availability

DraftSight V1R6.0
