---
title: "GetCellData Method (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "GetCellData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetCellData.html"
---

# GetCellData Method (IHoleDataTable)

Gets data from the specified table cell of this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellData( _
   ByVal ColumnName As System.String, _
   ByVal RowIndex As System.Integer, _
   ByRef CellData As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim ColumnName As System.String
Dim RowIndex As System.Integer
Dim CellData As System.String
Dim value As System.Boolean

value = instance.GetCellData(ColumnName, RowIndex, CellData)
```

### C#

```csharp
System.bool GetCellData(
   System.string ColumnName,
   System.int RowIndex,
   out System.string CellData
)
```

### C++/CLI

```cpp
System.bool GetCellData(
   System.String^ ColumnName,
   System.int RowIndex,
   [Out] System.String^ CellData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColumnName`: Column name (see **Remarks**)
- `RowIndex`: 0-based row index
- `CellData`: Cell data

### Return Value

True if cell data successfully retrieved, false if not

## VBA Syntax

See [HoleDataTable::GetCellData](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~GetCellData.html).

## Examples

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html) example.

## Remarks

To set:

- ColumnName, use [IHoleDataTable::GetColumnNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetColumnNames.html).
- RowIndex, use [IHoleDataTable::GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount.html).

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
