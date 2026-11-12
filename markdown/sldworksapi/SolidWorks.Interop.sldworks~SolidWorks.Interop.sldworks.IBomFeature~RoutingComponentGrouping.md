---
title: "RoutingComponentGrouping Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "RoutingComponentGrouping"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~RoutingComponentGrouping.html"
---

# RoutingComponentGrouping Property (IBomFeature)

Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoutingComponentGrouping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.RoutingComponentGrouping = value

value = instance.RoutingComponentGrouping
```

### C#

```csharp
System.int RoutingComponentGrouping {get; set;}
```

### C++/CLI

```cpp
property System.int RoutingComponentGrouping {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Routing component grouping options as defined in [swRoutingComponentGroupOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRoutingComponentGroupingOption_e.html)

## VBA Syntax

See [BomFeature::RoutingComponentGrouping](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~RoutingComponentGrouping.html).

## Examples

[Get and Set Routing Component Grouping Options for BOM Table (C#)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_CSharp.htm)
[Get and Set Routing Component Grouping Options for BOM Table (VB.NET)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_VBNET.htm)
[Get and Set Routing Component Grouping Options for BOM Table (VBA)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_VB.htm)

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
