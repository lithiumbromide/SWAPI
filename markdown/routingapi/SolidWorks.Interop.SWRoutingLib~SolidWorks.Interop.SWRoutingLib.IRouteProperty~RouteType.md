---
title: "RouteType Property (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "RouteType"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~RouteType.html"
---

# RouteType Property (IRouteProperty)

Gets the type of route.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RouteType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As System.Integer

value = instance.RouteType
```

### C#

```csharp
System.int RouteType {get;}
```

### C++/CLI

```cpp
property System.int RouteType {
   System.int get();
}
```

### Property Value

Type of route as defined in [swRouteType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swRouteType_e.html)

## VBA Syntax

See [RouteProperty::RouteType](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~RouteType.html).

## Examples

[Get Minimum Bend Radii of Wires (C#)](Get_Minimum_Bend_Radii_of_Wires_Example_CSharp.htm)
[Get Minimum Bend Radii of Wires (VB.NET)](Get_Minimum_Bend_Radii_of_Wires_Example_VBNET.htm)
[Get Minimum Bend Radii of Wires (VBA)](Get_Minimum_Bend_Radii_of_Wires_Example_VB.htm)

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
