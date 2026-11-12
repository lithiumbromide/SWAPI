---
title: "GetColumnNames Method (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "GetColumnNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~GetColumnNames.html"
---

# GetColumnNames Method (IHoleDataTable)

Gets the names of all the columns in this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnNames( _
   ByRef ColumnNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim ColumnNames As System.Object
Dim value As System.Boolean

value = instance.GetColumnNames(ColumnNames)
```

### C#

```csharp
System.bool GetColumnNames(
   out System.object ColumnNames
)
```

### C++/CLI

```cpp
System.bool GetColumnNames(
   [Out] System.Object^ ColumnNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColumnNames`: Array of column names

### Return Value

True if column names successfully retrieved, false if not

## VBA Syntax

See [HoleDataTable::GetColumnNames](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~GetColumnNames.html).

## Examples

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html) example.

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
