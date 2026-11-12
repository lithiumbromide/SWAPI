---
title: "SetCellRange Method (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "SetCellRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~SetCellRange.html"
---

# SetCellRange Method (ISelectData)

Sets the specified range of table cells for this selection.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCellRange( _
   ByVal FirstRow As System.Integer, _
   ByVal LastRow As System.Integer, _
   ByVal FirstColumn As System.Integer, _
   ByVal LastColumn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer

instance.SetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

### C#

```csharp
void SetCellRange(
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
)
```

### C++/CLI

```cpp
void SetCellRange(
   System.int FirstRow,
   System.int LastRow,
   System.int FirstColumn,
   System.int LastColumn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstRow`: 0-based row number at the beginning of the selection range
- `LastRow`: 0-based row number at the end of the selection range
- `FirstColumn`: 0-based row column at the beginning of the selection range
- `LastColumn`: 0-based row column at the end of the selection range

## VBA Syntax

See [SelectData::SetCellRange](ms-its:sldworksapivb6.chm::/Sldworks~SelectData~SetCellRange.html).

## Remarks

The range of table cells are only used for a selection made in a table. For all other types of selections, these values are ignored.

By default, the value for FirstRow, LastRow, FirstColumn, and LastColumn is -1, which indicates that the entire table is selected.

| To select an entire... | Set... |
| --- | --- |
| Row | FirstColumn and LastColumn to value values FirstRow LastRow to -1 |
| Column | FirstRow and LastRow to valid values FirstColumn and LastColumn to -1 |

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)
[ISelectData::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~GetCellRange.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
