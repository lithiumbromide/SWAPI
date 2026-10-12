---
title: "PartConfigurationGrouping Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "PartConfigurationGrouping"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~PartConfigurationGrouping.html"
---

# PartConfigurationGrouping Property (IBomFeature)

Gets and sets the part configuration grouping for this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartConfigurationGrouping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.PartConfigurationGrouping = value

value = instance.PartConfigurationGrouping
```

### C#

```csharp
System.int PartConfigurationGrouping {get; set;}
```

### C++/CLI

```cpp
property System.int PartConfigurationGrouping {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Grouping as defined in [swPartConfigurationGroupingOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartConfigurationGroupingOption_e.html)

## VBA Syntax

See [BomFeature::PartConfigurationGrouping](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~PartConfigurationGrouping.html).

## Remarks

This property corresponds to the Part Configuration Grouping section in the Bill of Materials PropertyManager, which displays when you create or edit a BOM table in an assembly drawing.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.html)
[IBomTableAnnotation::IGetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html)
[IBomTableAnnotation::GetComponentsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.html)
[IBomFeature::DisplayAsOneItem Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DisplayAsOneItem.html)

## Availability

SOLIDWORKS 2011 SP03 , Revision Number 19.3
