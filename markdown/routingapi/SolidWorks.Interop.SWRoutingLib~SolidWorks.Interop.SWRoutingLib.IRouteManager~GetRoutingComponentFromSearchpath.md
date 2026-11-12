---
title: "GetRoutingComponentFromSearchpath Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetRoutingComponentFromSearchpath"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetRoutingComponentFromSearchpath.html"
---

# GetRoutingComponentFromSearchpath Method (IRouteManager)

Gets the path and file name of the routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingComponentFromSearchpath( _
   ByVal __MIDL__IRouteManager0000 As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim __MIDL__IRouteManager0000 As System.String
Dim value As System.String

value = instance.GetRoutingComponentFromSearchpath(__MIDL__IRouteManager0000)
```

### C#

```csharp
System.string GetRoutingComponentFromSearchpath(
   System.string __MIDL__IRouteManager0000
)
```

### C++/CLI

```cpp
System.String^ GetRoutingComponentFromSearchpath(
   System.String^ __MIDL__IRouteManager0000
)
```

### Parameters

- `__MIDL__IRouteManager0000`: File name of the routing component for which to search

### Return Value

Path and file name of the routing component

## VBA Syntax

See [RouteManager::GetRoutingComponentFromSearchpath](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetRoutingComponentFromSearchpath.html).

## Remarks

If the specified routing component is not found, then the return value is empty.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2007 FCS
