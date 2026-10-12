---
title: "IsOuterDiameterFixed Property (IElectricalRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalRouteProperty"
member: "IsOuterDiameterFixed"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty~IsOuterDiameterFixed.html"
---

# IsOuterDiameterFixed Property (IElectricalRouteProperty)

Gets or sets whether to fix the outer diameter to the outer diameter value.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsOuterDiameterFixed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalRouteProperty
Dim value As System.Boolean

instance.IsOuterDiameterFixed = value

value = instance.IsOuterDiameterFixed
```

### C#

```csharp
System.bool IsOuterDiameterFixed {get; set;}
```

### C++/CLI

```cpp
property System.bool IsOuterDiameterFixed {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to fix the value of the outer diameter of the route to that of [IElectricalRouteProperty::OuterDiameter](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRouteProperty~OuterDiameter.html), false to enable diameter updates based on the diameters of the cables and wires that you route

## VBA Syntax

See [ElectricalRouteProperty::IsOuterDiameterFixed](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalRouteProperty~IsOuterDiameterFixed.html).

## See Also

[IElectricalRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty.html)
[IElectricalRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
