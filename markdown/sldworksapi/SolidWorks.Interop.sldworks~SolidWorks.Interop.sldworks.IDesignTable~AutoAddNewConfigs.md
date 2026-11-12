---
title: "AutoAddNewConfigs Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "AutoAddNewConfigs"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewConfigs.html"
---

# AutoAddNewConfigs Property (IDesignTable)

Gets or sets whether to automatically add rows or columns to the design table when new configurations are added to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoAddNewConfigs As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

instance.AutoAddNewConfigs = value

value = instance.AutoAddNewConfigs
```

### C#

```csharp
System.bool AutoAddNewConfigs {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoAddNewConfigs {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically add rows or columns, false to not

## VBA Syntax

See [DesignTable::AutoAddNewConfigs](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~AutoAddNewConfigs.html).

## Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html) after setting this property.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)
[IDesignTable::AutoAddNewParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AutoAddNewParams.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
