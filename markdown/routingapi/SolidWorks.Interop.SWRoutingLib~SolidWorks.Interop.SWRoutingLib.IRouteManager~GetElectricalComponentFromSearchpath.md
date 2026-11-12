---
title: "GetElectricalComponentFromSearchpath Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetElectricalComponentFromSearchpath"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetElectricalComponentFromSearchpath.html"
---

# GetElectricalComponentFromSearchpath Method (IRouteManager)

Gets the path and file name of the electrical component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElectricalComponentFromSearchpath( _
   ByVal __MIDL__IRouteManager0001 As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim __MIDL__IRouteManager0001 As System.String
Dim value As System.String

value = instance.GetElectricalComponentFromSearchpath(__MIDL__IRouteManager0001)
```

### C#

```csharp
System.string GetElectricalComponentFromSearchpath(
   System.string __MIDL__IRouteManager0001
)
```

### C++/CLI

```cpp
System.String^ GetElectricalComponentFromSearchpath(
   System.String^ __MIDL__IRouteManager0001
)
```

### Parameters

- `__MIDL__IRouteManager0001`: File name of the routing component for which to search

### Return Value

Path and file name of the electrical component

## VBA Syntax

See [RouteManager::GetElectricalComponentFromSearchpath](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetElectricalComponentFromSearchpath.html).

## Remarks

If the specified routing component is not found, then the return value is empty.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2007 FCS
