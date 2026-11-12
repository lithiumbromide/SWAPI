---
title: "CreateRouteLine Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "CreateRouteLine"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~CreateRouteLine.html"
---

# CreateRouteLine Method (IRouteManager)

Creates a routing line.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRouteLine( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim value As System.Object

value = instance.CreateRouteLine(P1x, P1y, P1z, P2x, P2y, P2z)
```

### C#

```csharp
System.object CreateRouteLine(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

### C++/CLI

```cpp
System.Object^ CreateRouteLine(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

### Parameters

- `P1x`: x coordinate for start point of the line
- `P1y`: y coordinate for start point of the line
- `P1z`: z coordinate for start point of the line
- `P2x`: x coordinate for end point of the line
- `P2y`: y coordinate for end point of the line
- `P2z`: z coordinate for end point of the line

### Return Value

[Line](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [RouteManager::CreateRouteLine](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~CreateRouteLine.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
