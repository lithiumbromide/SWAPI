---
title: "GetRouteProperty Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetRouteProperty"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetRouteProperty.html"
---

# GetRouteProperty Method (IRouteManager)

Gets the [IRouteProperty](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteProperty.html) object for the selected sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteProperty() As RouteProperty
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As RouteProperty

value = instance.GetRouteProperty()
```

### C#

```csharp
RouteProperty GetRouteProperty()
```

### C++/CLI

```cpp
RouteProperty^ GetRouteProperty();
```

### Return Value

Pointer to [IRouteProperty](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteProperty.html) object

## VBA Syntax

See [RouteManager::GetRouteProperty](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetRouteProperty.html).

## Examples

[Get Route Properties of Selected Sketch Segment (VBA)](Get_RouteProperty_from_Selected_Sketch_Segment_Example_VB.htm)
[Get Route Properties of Selected Sketch Segment (VB.NET)](Get_RouteProperty_from_Selected_Sketch_Segment_Example_VBNET.htm)
[Get Route Properties of Selected Sketch Segment (C#)](Get_RouteProperty_from_Selected_Sketch_Segment_Example_CSharp.htm)

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)

## Availability

SOLIDWORKS Routing 2006 FCS
