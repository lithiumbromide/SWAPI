---
title: "GetAllRouteSegmentCount Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetAllRouteSegmentCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetAllRouteSegmentCount.html"
---

# GetAllRouteSegmentCount Method (IRouteManager)

Gets the number of route segments for active route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllRouteSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim value As System.Integer

value = instance.GetAllRouteSegmentCount()
```

### C#

```csharp
System.int GetAllRouteSegmentCount()
```

### C++/CLI

```cpp
System.int GetAllRouteSegmentCount();
```

### Return Value

Number of route segments for active route

## VBA Syntax

See [RouteManager::GetAllRouteSegmentCount](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetAllRouteSegmentCount.html).

## Remarks

Call this method before calling [IRouteManager::IGetAllRouteSegmentIDs](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~IGetAllRouteSegmentIDs.html) to get the size of the array for that method.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager::GetAllRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetAllRouteSegmentIDs.html)

## Availability

SOLIDWORKS Routing 2008 FCS
