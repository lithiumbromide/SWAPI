---
title: "ColumnHidden Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "ColumnHidden"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html"
---

# ColumnHidden Property (IDesignTable)

Gets the visibility state of the specified column.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ColumnHidden( _
   ByVal Col As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Col As System.Integer
Dim value As System.Boolean

value = instance.ColumnHidden(Col)
```

### C#

```csharp
System.bool ColumnHidden(
   System.int Col
) {get;}
```

### C++/CLI

```cpp
property System.bool ColumnHidden {
   System.bool get(System.int Col);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Col`: Column for which to get its visibility state; 1 is the first column

### Property Value

True if hidden, false if visible

## VBA Syntax

See [DesignTable::ColumnHidden](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~ColumnHidden.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
