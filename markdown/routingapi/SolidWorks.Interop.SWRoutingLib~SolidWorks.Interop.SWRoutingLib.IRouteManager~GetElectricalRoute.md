---
title: "GetElectricalRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetElectricalRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetElectricalRoute.html"
---

# GetElectricalRoute Method (IRouteManager)

Gets the electrical route for a selected route assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElectricalRoute() As ElectricalRoute
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As ElectricalRoute

value = instance.GetElectricalRoute()
```

### C#

```csharp
ElectricalRoute GetElectricalRoute()
```

### C++/CLI

```cpp
ElectricalRoute^ GetElectricalRoute();
```

### Return Value

Pointer to [IElectricalRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IElectricalRoute.html) object

## VBA Syntax

See [RouteManager::GetElectricalRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetElectricalRoute.html).

## Examples

[Get RouteManager and Electrical Route (VBA)](Get_RouteManager_and_Electrical_Route_Example_VB.htm)
[Get Wires (VBA)](Get_Wires_Example_VB.htm)
[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)
[Set New Route Paths for Wires (C#)](Set_New_Route_Paths_for_Wires_Example_CSharp.htm)
[Set New Route Paths for Wires (VB.NET)](Set_New_Route_Paths_for_Wires_Example_VBNET.htm)
[Set New Route Paths for Wires (VBA)](Set_New_Route_Paths_for_Wires_Example_VB.htm)

## Remarks

Before calling this method, you must call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html) to place the routing assembly in edit mode.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
