---
title: "RowHidden Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "RowHidden"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html"
---

# RowHidden Property (IDesignTable)

Gets the visibility state of the specified row.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RowHidden( _
   ByVal Row As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Row As System.Integer
Dim value As System.Boolean

value = instance.RowHidden(Row)
```

### C#

```csharp
System.bool RowHidden(
   System.int Row
) {get;}
```

### C++/CLI

```cpp
property System.bool RowHidden {
   System.bool get(System.int Row);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row for which to get its visibility state; 1 is the first row

### Property Value

True if hidden, false if visible

## VBA Syntax

See [DesignTable::RowHidden](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~RowHidden.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
