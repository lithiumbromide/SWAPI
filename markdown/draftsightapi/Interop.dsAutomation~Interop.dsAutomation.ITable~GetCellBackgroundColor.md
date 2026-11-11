---
title: "GetCellBackgroundColor Method (ITable)"
project: ""
interface: "ITable"
member: "GetCellBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBackgroundColor.html"
---

# GetCellBackgroundColor Method (ITable)

Gets the background Color of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Function GetCellBackgroundColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As Color
```

### C#

```csharp
Color GetCellBackgroundColor(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetCellBackgroundColor(
   Row : System.int,
   Column : System.int
) : Color;
```

### Managed Extensions for C++

```
Color* GetCellBackgroundColor(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
Color^ GetCellBackgroundColor(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Index of the row of the cell whose background Color to get (see **Remarks**)
- `Column`: Index of the column of the cell whose background Color to get (see **Remarks**)

### Return Value

Background [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBackgroundColor.html)
[ITable::SetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBackgroundColor.html)
[ITable::GetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBackgroundColor.html)

## Availability

DraftSight V1R6.0
