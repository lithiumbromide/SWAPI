---
title: "GetTextStyle Method (ITable)"
project: ""
interface: "ITable"
member: "GetTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextStyle.html"
---

# GetTextStyle Method (ITable)

Gets the name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) of the specified type of cell in this Table.

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

- `CellType`: Type of cell as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Name of the [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) of the specified type of cell in this Table

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextStyle.html)
[ITable::SetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextStyle.html)
[ITable::GetCellTextStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextStyle.html)
[ITable::GetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextColor.html)
[ITable::GetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellTextHeight.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)
[ITable::GetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextColor.html)
[ITable::GetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetTextHeight.html)
[ITable::SetCellTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextColor.html)
[ITable::SetCellTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellTextHeight.html)
[ITable::SetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetText.html)
[ITable::SetTextColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextColor.html)
[ITable::SetTextHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetTextHeight.html)

## Availability

DraftSight V1R6.0
