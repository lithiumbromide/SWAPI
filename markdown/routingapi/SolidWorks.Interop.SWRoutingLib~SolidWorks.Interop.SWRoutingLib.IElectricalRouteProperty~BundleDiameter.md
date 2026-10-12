---
title: "BundleDiameter Property (IElectricalRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRouteProperty"
member: "BundleDiameter"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~BundleDiameter.html"
---

# BundleDiameter Property (IElectricalRouteProperty)

Gets or sets the cumulative diameter of all wires in the route segment.

## Syntax

### Visual Basic (Declaration)

```vb
Property BundleDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRouteProperty
Dim value As System.Double

instance.BundleDiameter = value

value = instance.BundleDiameter
```

### C#

```csharp
System.double BundleDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double BundleDiameter {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cumulative diameter of all wires in the route segment

## VBA Syntax

See [ElectricalRouteProperty::BundleDiameter](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRouteProperty~BundleDiameter.html).

## Remarks

You can use this property to determine if the diameter is too small to contain all of the wires in the route segment.

## See Also

[IElectricalRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty.html)
[IElectricalRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
