---
title: "EnableCellDropdownLists Property (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "EnableCellDropdownLists"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EnableCellDropdownLists.html"
---

# EnableCellDropdownLists Property (IDesignTable)

Gets or sets whether to enable cell drop-down lists in the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableCellDropdownLists As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Boolean

instance.EnableCellDropdownLists = value

value = instance.EnableCellDropdownLists
```

### C#

```csharp
System.bool EnableCellDropdownLists {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableCellDropdownLists {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable cell drop-down lists in the design table, false to disable them

## VBA Syntax

See [DesignTable::EnableCellDropdownLists](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~EnableCellDropdownLists.html).

## Examples

[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

## Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.html) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.html) after setting this property.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
