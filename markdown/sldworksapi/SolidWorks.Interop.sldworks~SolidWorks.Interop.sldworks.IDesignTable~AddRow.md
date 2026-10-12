---
title: "AddRow Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "AddRow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html"
---

# AddRow Method (IDesignTable)

Adds a row to the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRow( _
   ByVal CellValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim CellValues As System.Object
Dim value As System.Boolean

value = instance.AddRow(CellValues)
```

### C#

```csharp
System.bool AddRow(
   System.object CellValues
)
```

### C++/CLI

```cpp
System.bool AddRow(
   System.Object^ CellValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CellValues`: Array of the cell values

### Return Value

True if the row was successfully added, false if not

## VBA Syntax

See [DesignTable::AddRow](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~AddRow.html).

## Examples

[Add Row to Design Table (VBA)](Add_Row_to_Design_Table_Example_VB.htm)

## Remarks

Do not use [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) or [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html) with this method. Instead, use [IDesignTable::EditTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~EditTable2.html) and [IDesignTable::UpdateTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~UpdateTable.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::SetRowChanged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)
[IDesignTable::AutoAddNewConfigs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewConfigs.html)
[IDesignTable::AutoAddNewParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewParams.html)

## Availability

SOLIDWORKS 2001 SP01, Revision Number 8.1
