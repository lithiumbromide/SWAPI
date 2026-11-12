---
title: "DisplayAsOneItem Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "DisplayAsOneItem"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DisplayAsOneItem.html"
---

# DisplayAsOneItem Property (IBomFeature)

Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayAsOneItem As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.DisplayAsOneItem = value

value = instance.DisplayAsOneItem
```

### C#

```csharp
System.bool DisplayAsOneItem {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayAsOneItem {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if different configurations are displayed as the same item number, false if not

## VBA Syntax

See [BomFeature::DisplayAsOneItem](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~DisplayAsOneItem.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## Remarks

This property corresponds to the Part Configuration Grouping **> Display as one item number** check box in the Bill of Materials PropertyManager, which displays when you create or edit a BOM table in an assembly drawing.

This property applies to top-level only BOM tables. Use [IBomFeature::TableType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~TableType.html) to determine the BOM table type.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::PartConfigurationGrouping Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~PartConfigurationGrouping.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12
