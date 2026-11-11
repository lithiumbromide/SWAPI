---
title: "SetCellBackgroundColor Method (ITable)"
project: ""
interface: "ITable"
member: "SetCellBackgroundColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetCellBackgroundColor.html"
---

# SetCellBackgroundColor Method (ITable)

Sets the background Color of the specified cell in this Table.

## Syntax

### Visual Basic

```vb
Sub SetCellBackgroundColor( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetCellBackgroundColor(
   System.int Row,
   System.int Column,
   Color NewVal
)
```

### JScript

```
function SetCellBackgroundColor(
   Row : System.int,
   Column : System.int,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetCellBackgroundColor(
   System.int Row,
   System.int Column,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetCellBackgroundColor(
   System.int Row,
   System.int Column,
   Color^ NewVal
)
```

### Parameters

- `Row`: Index of the row of the cell whose background Color to set (see **Remarks**)
- `Column`: Index of the column of the cell whose background Color to set (see **Remarks**)
- `NewVal`: Background [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## Remarks

To determine a valid index for the row or column:

| Get the total number of... | Using... |
| --- | --- |
| Rows | ITable::TotalRowCount |
| Columns | ITable::TotalColumnCount |

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetCellBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCellBackgroundColor.html)
[ITable::GetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetBackgroundColor.html)
[ITable::SetBackgroundColor Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetBackgroundColor.html)

## Availability

DraftSight V1R6.0
