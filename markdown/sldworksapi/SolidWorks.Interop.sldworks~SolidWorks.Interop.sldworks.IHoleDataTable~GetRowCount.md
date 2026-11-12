---
title: "GetRowCount Method (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "GetRowCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowCount.html"
---

# GetRowCount Method (IHoleDataTable)

Gets the number of rows in this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRowCount( _
   ByRef RowCount As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim RowCount As System.Integer
Dim value As System.Boolean

value = instance.GetRowCount(RowCount)
```

### C#

```csharp
System.bool GetRowCount(
   out System.int RowCount
)
```

### C++/CLI

```cpp
System.bool GetRowCount(
   [Out] System.int RowCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowCount`: Number of rows

### Return Value

True if number of rows successfully retrieved, false if not

## VBA Syntax

See [HoleDataTable::GetRowCount](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~GetRowCount.html).

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)
[IHoleDataTable::GetCellData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetCellData.html)
[IHoleDataTable::GetRowData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetRowData.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
