---
title: "MinimumBendRadius Property (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "MinimumBendRadius"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~MinimumBendRadius.html"
---

# MinimumBendRadius Property (IRouteProperty)

Gets the minimum bend radius in this route segment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MinimumBendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As System.Double

value = instance.MinimumBendRadius
```

### C#

```csharp
System.double MinimumBendRadius {get;}
```

### C++/CLI

```cpp
property System.double MinimumBendRadius {
   System.double get();
}
```

### Property Value

Minimum bend radius in this route segment

## VBA Syntax

See [RouteProperty::MinimumBendRadius](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~MinimumBendRadius.html).

## Examples

[Get Minimum Bend Radii of Wires (C#)](Get_Minimum_Bend_Radii_of_Wires_Example_CSharp.htm)
[Get Minimum Bend Radii of Wires (VB.NET)](Get_Minimum_Bend_Radii_of_Wires_Example_VBNET.htm)
[Get Minimum Bend Radii of Wires (VBA)](Get_Minimum_Bend_Radii_of_Wires_Example_VB.htm)

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[IRouteProperty::BendRadius Property ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~BendRadius.html)
[IElectricalRouteProperty::BundleMinimumBendRadius Property ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~BundleMinimumBendRadius.html)

## Availability

SOLIDWORKS Routing 2014 FCS
