---
title: "GetBordersVisibility Method (ITable)"
project: ""
interface: "ITable"
member: "GetBordersVisibility"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersVisibility.html"
---

# GetBordersVisibility Method (ITable)

Sets the visibility of the specified type of [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html) for the border of the specified type of cell in this Table.

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

- `CellType`: Type of cell in the Table as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `LineType`: Type of Line for the border as defined in [dsTableBordersLineType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableBordersLineType_e.html)

### Return Value

True to show the specified type of Line for the border of the specified type of cell in this Table, false to hide it

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersVisibility.html)
[ITable::SetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersVisibility.html)
[ITable::GetCellBordersVisibility Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersVisibility.html)
[ITable::GetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersColor.html)
[ITable::GetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBordersLineWeight.html)
[ITable::GetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersColor.html)
[ITable::GetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBordersLineWeight.html)
[ITable::SetBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersColor.html)
[ITable::SetBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBordersLineWeight.html)
[ITable::SetCellBordersColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersColor.html)
[ITable::SetCellBordersLineWeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBordersLineWeight.html)

## Availability

DraftSight V1R6.0
