---
title: "InsertTable Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertTable"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertTable.html"
---

# InsertTable Method (ISketchManager)

Inserts a Table.

## Syntax

### Visual Basic

```vb
Function InsertTable( _
   ByVal Left As System.Double, _
   ByVal Top As System.Double, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer, _
   ByVal RowHeight As System.Double, _
   ByVal ColumnWidth As System.Double, _
   ByVal FirstRowStyle As dsTableCellType_e, _
   ByVal SecondRowStyle As dsTableCellType_e, _
   ByVal OtherRowStyle As dsTableCellType_e _
) As Table
```

### C#

```csharp
Table InsertTable(
   System.double Left,
   System.double Top,
   System.int Rows,
   System.int Columns,
   System.double RowHeight,
   System.double ColumnWidth,
   dsTableCellType_e FirstRowStyle,
   dsTableCellType_e SecondRowStyle,
   dsTableCellType_e OtherRowStyle
)
```

### JScript

```
function InsertTable(
   Left : System.double,
   Top : System.double,
   Rows : System.int,
   Columns : System.int,
   RowHeight : System.double,
   ColumnWidth : System.double,
   FirstRowStyle : dsTableCellType_e,
   SecondRowStyle : dsTableCellType_e,
   OtherRowStyle : dsTableCellType_e
) : Table;
```

### Managed Extensions for C++

```
Table* InsertTable(
   System.double Left,
   System.double Top,
   System.int Rows,
   System.int Columns,
   System.double RowHeight,
   System.double ColumnWidth,
   dsTableCellType_e FirstRowStyle,
   dsTableCellType_e SecondRowStyle,
   dsTableCellType_e OtherRowStyle
)
```

### C++/CLI

```cpp
Table^ InsertTable(
   System.double Left,
   System.double Top,
   System.int Rows,
   System.int Columns,
   System.double RowHeight,
   System.double ColumnWidth,
   dsTableCellType_e FirstRowStyle,
   dsTableCellType_e SecondRowStyle,
   dsTableCellType_e OtherRowStyle
)
```

### Parameters

- `Left`: x coordinate of the upper-left corner point of the Table
- `Top`: y coordinate of the upper-left corner point of the Table
- `Rows`: Number of rows in the Table
- `Columns`: Number of columns in the Table
- `RowHeight`: Height of the rows in the Table
- `ColumnWidth`: Width of the columns in the Table
- `FirstRowStyle`: Style for first row as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `SecondRowStyle`: Style for second row as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)
- `OtherRowStyle`: Style for all other rows as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

[Table](Interop.dsAutomation~Interop.dsAutomation.ITable.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager.html)

## Availability

DraftSight V1R3.0
