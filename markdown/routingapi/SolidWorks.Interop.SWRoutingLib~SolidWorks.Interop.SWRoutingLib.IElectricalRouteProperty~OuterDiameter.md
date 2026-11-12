---
title: "OuterDiameter Property (IElectricalRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRouteProperty"
member: "OuterDiameter"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~OuterDiameter.html"
---

# OuterDiameter Property (IElectricalRouteProperty)

Gets or sets the outer diameter of the route.

## Syntax

### Visual Basic (Declaration)

```vb
Property OuterDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRouteProperty
Dim value As System.Double

instance.OuterDiameter = value

value = instance.OuterDiameter
```

### C#

```csharp
System.double OuterDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double OuterDiameter {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Outer diameter of route

## VBA Syntax

See [ElectricalRouteProperty::OuterDiameter](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRouteProperty~OuterDiameter.html).

## Remarks

You can make this value static using [IElectricalRouteProperty::IsOuterDiameterFlixed](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRouteProperty~IsOuterDiameterFixed.html).

## See Also

[IElectricalRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty.html)
[IElectricalRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
