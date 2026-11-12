---
title: "GetRowData Method (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "GetRowData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowData.html"
---

# GetRowData Method (IHoleDataTable)

Gets data for the specified row of this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRowData( _
   ByVal RowIndex As System.Integer, _
   ByRef RowData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim RowIndex As System.Integer
Dim RowData As System.Object
Dim value As System.Boolean

value = instance.GetRowData(RowIndex, RowData)
```

### C#

```csharp
System.bool GetRowData(
   System.int RowIndex,
   out System.object RowData
)
```

### C++/CLI

```cpp
System.bool GetRowData(
   System.int RowIndex,
   [Out] System.Object^ RowData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: 0-based index of row
- `RowData`: Row data

### Return Value

True if row data successfully retrieved, false if not

## VBA Syntax

See [HoleDataTable::GetRowData](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~GetRowData.html).

## Remarks

To set RowIndex, use [IHoleDataTable::GetRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount.html).

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
