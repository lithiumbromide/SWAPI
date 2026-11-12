---
title: "BundleMinimumBendRadius Property (IElectricalRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRouteProperty"
member: "BundleMinimumBendRadius"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~BundleMinimumBendRadius.html"
---

# BundleMinimumBendRadius Property (IElectricalRouteProperty)

Gets the maximum bend radius of the individual wires in a bundle of wires that are routed through the same route segment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BundleMinimumBendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRouteProperty
Dim value As System.Double

value = instance.BundleMinimumBendRadius
```

### C#

```csharp
System.double BundleMinimumBendRadius {get;}
```

### C++/CLI

```cpp
property System.double BundleMinimumBendRadius {
   System.double get();
}
```

### Property Value

Maximum bend radius of the individual wires in a bundle of wires that are routed through the same route segment

## VBA Syntax

See [ElectricalRouteProperty::BundleMinimumBendRadius](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRouteProperty~BundleMinimumBendRadius.html).

## Examples

[Get Minimum Bend Radii of Wires (C#)](Get_Minimum_Bend_Radii_of_Wires_Example_CSharp.htm)
[Get Minimum Bend Radii of Wires (VB.NET)](Get_Minimum_Bend_Radii_of_Wires_Example_VBNET.htm)
[Get Minimum Bend Radii of Wires (VBA)](Get_Minimum_Bend_Radii_of_Wires_Example_VB.htm)

## Remarks

The minimum bend radius for a bundle of wires routed through the same route segment is the maximum bend radius of the individual wires.

## See Also

[IElectricalRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty.html)
[IElectricalRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty_members.html)
[IRouteProperty::MinimumBendRadius Property ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~MinimumBendRadius.html)
[IRouteProperty::BendRadius Property ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~BendRadius.html)

## Availability

SOLIDWORKS Routing 2014 FCS
