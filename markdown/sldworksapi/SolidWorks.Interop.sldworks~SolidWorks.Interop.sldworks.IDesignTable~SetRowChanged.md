---
title: "SetRowChanged Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "SetRowChanged"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.html"
---

# SetRowChanged Method (IDesignTable)

Sets the number of the row that was changed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRowChanged( _
   ByVal RowIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim RowIndex As System.Integer

instance.SetRowChanged(RowIndex)
```

### C#

```csharp
void SetRowChanged(
   System.int RowIndex
)
```

### C++/CLI

```cpp
void SetRowChanged(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Number of row that changed

## VBA Syntax

See [DesignTable::SetRowChanged](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~SetRowChanged.html).

## Remarks

Setting the number of the row that changed provides significant performance gains for products like CD Catalog Viewer, a component of 3D PartStream.NET.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
